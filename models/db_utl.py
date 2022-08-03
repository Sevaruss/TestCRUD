import sqlalchemy
import databases

# URL
DB_USER = "test_crud"
DB_PASS = "1qaz!QAZ"
DB_HOST = "localhost"
DB_NAME = "test_crud"
SQLALCHEMY_DATABASE_URL = ( f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}" )

# ---------
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)
metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
    sqlalchemy.Column("email", sqlalchemy.String(150), unique=True, index=True)
)

# Таблица для теста
test_table = sqlalchemy.Table(
    "test_tab",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
    sqlalchemy.Column("descr", sqlalchemy.String(255))
)

#from os import environ
#DB_USER = environ.get("DB_USER", "test_crud")
#DB_PASS = environ.get("DB_PASS", "1qaz!QAZ")
#DB_HOST = environ.get("DB_HOST", "localhost")
#DB_NAME = "test_crud"
#SQLALCHEMY_DATABASE_URL = (f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}")

database = databases.Database(SQLALCHEMY_DATABASE_URL)

