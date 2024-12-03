from flask import Flask, request, jsonify
from src.db.model import login_user

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Recebe as credenciais do corpo da requisição
    data = request.json
    email = data.get('email')
    senha = data.get('senha')

    if not email or not senha:
        return jsonify({"message": "Email e senha são obrigatórios"}), 400

    # Tenta fazer login
    usuario = login_user(email, senha)

    if usuario:
        return jsonify({
            "message": "Login bem-sucedido",
            "user": {
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email
            }
        }), 200
    else:
        return jsonify({"message": "Credenciais inválidas"}), 401

if __name__ == '__main__':
    app.run(debug=True)
