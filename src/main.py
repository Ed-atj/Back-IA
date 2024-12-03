from flask import Flask
import urllib.parse
from src.db.connection import db, init_db  # Importa a instância db já criada

app = Flask(__name__)

# Configurações de conexão com o banco
DATABASE_HOST = 'autorack.proxy.rlwy.net'
DATABASE_PORT = '25586'
DATABASE_NAME = 'railway'
DATABASE_USERNAME = 'root'
DATABASE_PASSWORD = 'RhECSoYuzufDsyfKcOFeBcBDiimphBkk'

# Escapa a senha para evitar erros de caracteres
DATABASE_PASSWORD_ESCAPED = urllib.parse.quote_plus(DATABASE_PASSWORD)

# Configuração da URI de conexão
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{DATABASE_USERNAME}:{DATABASE_PASSWORD_ESCAPED}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a instância do banco no Flask
init_db(app)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
