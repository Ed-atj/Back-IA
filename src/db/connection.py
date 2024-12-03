from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy()

def init_db(app):
    """
    Inicializa a conexão com o banco de dados.
    :param app: Instância do Flask.
    """
    db.init_app(app)
    with app.app_context():
        try:
            db.session.execute(text('SELECT 1'))
            print('\n\n----------- Connection successful !')
        except Exception as e:
            print('\n\n----------- Connection failed ! ERROR : ', e)
        # Cria todas as tabelas definidas nos modelos (se não existirem)
        Base.metadata.create_all(bind=db.engine)
        db.create_all()
