import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_HOST = 'autorack.proxy.rlwy.net'
DATABASE_PORT = '25586'
DATABASE_NAME = 'railway'
DATABASE_USERNAME = 'root'
DATABASE_PASSWORD = 'RhECSoYuzufDsyfKcOFeBcBDiimphBkk'

DATABASE_PASSWORD_ESCAPED = urllib.parse.quote_plus(DATABASE_PASSWORD)

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DATABASE_USERNAME}:{DATABASE_PASSWORD_ESCAPED}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base = declarative_base()

Session = sessionmaker(bind=engine)

def SessionLocal():
    return Session()


def init_db():
    Base.metadata.create_all(engine)
    print("Banco de dados inicializado com sucesso!")
