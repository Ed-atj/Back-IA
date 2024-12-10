from flask import Flask
from src.controller.user_controller import user_controller
from src.controller.agendamento_controller import agendamento_controller
from src.db.connection import init_db

app = Flask(__name__)

app.register_blueprint(user_controller)
app.register_blueprint(agendamento_controller)

@app.route('/')
def home():
    return "Welcome to the User Management API!"

def init_database():
    init_db()
    print("Banco de dados iniciado!")

if __name__ == '__main__':
    init_database()
    app.config['ENV'] = 'production'
    app.config['DEBUG'] = False
    app.run(host='0.0.0.0', port=5000)