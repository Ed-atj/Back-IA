from flask import Flask
from src.controller.user_controller import user_controller
from src.controller.agendamento_controller import agendamento_controller

app = Flask(__name__)

app.register_blueprint(user_controller)
app.register_blueprint(agendamento_controller)

@app.route('/')
def home():
    return "Welcome to the User Management API!"

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)