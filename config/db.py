
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

_hostname = 'cfls9h51f4i86c.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com'
_username = 'u1smtv9h92is8u'
_password = 'pdc051a3c3e1f80c716c40ea53e3ea3f2ef624249439a97deb2b3ed231711ac56'
_database = 'd1ptcm37j0hmpk' 

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