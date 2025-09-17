
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.pool import ThreadedConnectionPool



#---LOCAL DATABASE ----

# _hostname ='localhost'
# _username ='basedatos'
# _password ='basedatos'
# _database ='notario'

    #---HEROKU DATABASE ----

_hostname = 'caij57unh724n3.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com'
_username = 'u9ml07d3orsguo'
_password = 'p5f389676cec422b52dd30b5fe38ad36f8ae86bfe6b4cc72cfde48bcdc42e2865'
_database = 'deh7qudban17rr' 

DATABASE_URL = "postgresql://"+_username + ":"+ _password +"@"+ _hostname +":5432/" + _database

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


db_pool = ThreadedConnectionPool(
    1,
    30,
    dbname=_database,
    user=_username,
    password=_password,
    host=_hostname,
    port=5432
)


# def conn():
#     conn = psycopg2.connect(host=_hostname ,
#                     user=_username,
#                     password=_password,
#                     database=_database)
#     return conn