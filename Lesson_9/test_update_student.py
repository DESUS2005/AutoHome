import pytest
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert, update, delete

# Конфигурация соединения
DATABASE_URL = "postgresql://postgres:D123@localhost:5432/postgres"


@pytest.fixture(scope='module')
def engine():
    """Фикстура для создания движка SQLAlchemy."""
    engine = create_engine(DATABASE_URL)
    return engine


@pytest.fixture(scope='function')
def connection(engine):
    """Фикстура для получения соединения с БД для каждого теста."""
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope='function')
def student_table(engine):
    """Фикстура, которая возвращает объект таблицы 'student', предполагая ее существование."""
    metadata = MetaData()
    student = Table('student', metadata,
                    Column('user_id', Integer, primary_key=True, autoincrement=True),
                    Column('level', String(50)),
                    Column('education_form', String(50)),
                    Column('subject_id', Integer),
                    schema='public'
                    )
    return student


def test_update_student(connection, student_table):
    """Тест на изменение записи студента."""
    student = student_table
    test_subject_id = 456
    initial_level = 'Beginner'
    updated_level = 'Advanced'

    # 1. Вставляем тестовые данные (подготовка к обновлению)
    insert_stmt = student.insert().values(
        level=initial_level,
        education_form='Full-time',
        subject_id=test_subject_id
    )
    connection.execute(insert_stmt)

    # 2. Обновляем запись
    update_stmt = update(student).where(student.c.subject_id == test_subject_id).values(level=updated_level)
    connection.execute(update_stmt)

    # 3. Проверяем обновление
    select_stmt = select(student).where(student.c.subject_id == test_subject_id)
    rs = connection.execute(select_stmt).fetchone()

    assert rs is not None
    assert rs.level == updated_level
    assert rs.education_form == 'Full-time'  # Убедимся, что другие поля не изменились

    # 4. Удаляем тестовые данные, созданные для этого теста
    delete_stmt = delete(student).where(student.c.subject_id == test_subject_id)
    connection.execute(delete_stmt)

    # 5. Дополнительная проверка, что запись действительно удалена
    rs_after_delete = connection.execute(select_stmt).fetchone()
    assert rs_after_delete is None