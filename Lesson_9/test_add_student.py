import pytest
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert, delete

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
    # Отражаем существующую таблицу
    student = Table('student', metadata,
                    Column('user_id', Integer, primary_key=True, autoincrement=True),
                    Column('level', String(50)),
                    Column('education_form', String(50)),
                    Column('subject_id', Integer),
                    schema='public'
                    )
    return student


def test_add_student(connection, student_table):
    """Тест на добавление новой записи студента."""
    student = student_table
    test_subject_id = 123

    # 1. Вставляем новую запись
    insert_stmt = insert(student).values(
        level='Beginner',
        education_form='Full-time',
        subject_id=test_subject_id
    )
    connection.execute(insert_stmt)

    # 2. Проверяем, что запись добавилась
    select_stmt = select(student).where(student.c.subject_id == test_subject_id)
    result = connection.execute(select_stmt).fetchone()

    assert result is not None
    assert result.level == 'Beginner'
    assert result.education_form == 'Full-time'
    assert result.subject_id == test_subject_id

    # 3. Удаляем добавленную запись для чистоты теста, чтобы последующие тесты
    # не столкнулись с конфликтом ID или данными.
    delete_stmt = delete(student).where(student.c.subject_id == test_subject_id)
    connection.execute(delete_stmt)

    # 4. Дополнительная проверка, что запись действительно удалена
    result_after_delete = connection.execute(select_stmt).fetchone()
    assert result_after_delete is None