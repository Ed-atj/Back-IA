# Use a imagem oficial do Python como base, com uma versão slim para produção
FROM python:3.12-slim as build

# Definir o diretório de trabalho
WORKDIR /app

# Copiar apenas os arquivos necessários para o contêiner
COPY requirements.txt /app/requirements.txt

# Instalar as dependências com a opção --no-cache-dir para reduzir o tamanho da imagem
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar o código-fonte da aplicação para dentro do contêiner
COPY . /app

# Definir variáveis de ambiente para evitar problemas de cache ou configurações
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Expor a porta que a aplicação vai rodar
EXPOSE 5000

# Usar um comando para iniciar a aplicação em modo de produção
CMD ["python", "src/main.py"]
