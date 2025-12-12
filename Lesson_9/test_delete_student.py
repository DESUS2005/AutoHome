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
    student = Table('student', metadata,
                    Column('user_id', Integer, primary_key=True, autoincrement=True),
                    Column('level', String(50)),
                    Column('education_form', String(50)),
                    Column('subject_id', Integer),
                    schema='public'
                    )
    return student

def test_delete_student(connection, student_table):
    """Тест на удаление записи студента."""
    student = student_table
    test_subject_id = 789

    # 1. Вставляем тестовые данные, которые будем удалять
    insert_stmt = student.insert().values(
        level='Beginner',
        education_form='Full-time',
        subject_id=test_subject_id
    )
    connection.execute(insert_stmt)

    # 2. Проверка, что запись была вставлена перед удалением
    select_stmt_before = select(student).where(student.c.subject_id == test_subject_id)
    rs_before = connection.execute(select_stmt_before).fetchone()
    assert rs_before is not None

    # 3. Удаляем запись
    delete_stmt = delete(student).where(student.c.subject_id == test_subject_id)
    connection.execute(delete_stmt)

    # 4. Проверка: данные удалены
    select_stmt_after = select(student).where(student.c.subject_id == test_subject_id)
    rs_after = connection.execute(select_stmt_after).fetchone()
    assert rs_after is None