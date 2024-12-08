# GabiTelecras

TeleCras Backend: API para o Portal CRAS
Este repositório contém o backend do TeleCras, responsável por gerenciar as APIs que conectam o portal ao banco de dados e fornecem suporte às operações de CRUD e integração com o frontend.

O backend foi desenvolvido com foco em desempenho, escalabilidade e segurança, utilizando Python e tecnologias modernas para garantir uma experiência robusta para os usuários do portal.



🌟 Funcionalidades Principais
Gerenciamento de APIs:

Roteamento e integração com o frontend.
Suporte a operações de CRUD (Create, Read, Update, Delete) para:
Usuários.
Agendamentos.
Conexão com Banco de Dados:

🚀Banco de dados hospedado no Railway.
Gerenciamento eficiente utilizando SQLAlchemy para mapeamento objeto-relacional (ORM).

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.11.
Framework: Flask para criação de APIs rápidas e leves.
ORM: SQLAlchemy para manipulação do banco de dados.
IDE: PyCharm para desenvolvimento e debug.
Banco de Dados: Railway (MySQL/PostgreSQL).

📜 Estrutura de Rotas
Usuários
GET /users – Lista todos os usuários.
POST /users – Cria um novo usuário.
PUT /users/<id> – Atualiza informações de um usuário.
DELETE /users/<id> – Remove um usuário.
Agendamentos
GET /appointments – Lista todos os agendamentos.
POST /appointments – Cria um novo agendamento.
GET /appointments/<cpf> – Busca agendamentos por CPF.

## Acesse a Documentação

[![Acessar Documentação](https://via.placeholder.com/200x50/0056b3/FFFFFF?text=Acessar+Documentação)](https://leonardosilvapy.github.io/AssistenteGABI/)

📞 Contato
Para dúvidas ou sugestões, entre em contato pelo e-mail: gabitelecras@gmail.com

💡 Nota: Este projeto está em desenvolvimento ativo. Algumas funcionalidades ainda podem estar sujeitas a alterações ou melhorias.
