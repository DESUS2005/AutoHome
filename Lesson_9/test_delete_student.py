import pytest
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert

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
def setup_table(engine):
    """Фикстура для создания таблицы 'student' перед тестом."""
    metadata = MetaData()
    student = Table('student', metadata,
                    Column('user_id', Integer, primary_key=True, autoincrement=True),
                    Column('level', String(50)),
                    Column('education_form', String(50)),
                    Column('subject_id', Integer),
                    schema='public'
                    )
    metadata.create_all(engine)
    yield student
    # Тесты должны сами удалять свои данные.


def test_delete_student(connection, setup_table):
    """Тест на удаление записи студента."""
    student = setup_table
    test_subject_id = 789

    # Вставляем тестовые данные
    insert_stmt = student.insert().values(
        level='Beginner',
        education_form='Full-time',
        subject_id=test_subject_id
    )
    connection.execute(insert_stmt)

    # Проверка, что запись была вставлена перед удалением
    select_stmt_before = select(student).where(student.c.subject_id == test_subject_id)
    rs_before = connection.execute(select_stmt_before).fetchone()
    assert rs_before is not None

    # Удаляем запись
    delete_stmt = student.delete().where(student.c.subject_id == test_subject_id)
    connection.execute(delete_stmt)

    # Проверка: данные удалены
    select_stmt_after = select(student).where(student.c.subject_id == test_subject_id)
    rs_after = connection.execute(select_stmt_after).fetchone()
    assert rs_after is None