FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app
ENV PYTHONPATH=/app/src:$PYTHONPATH
EXPOSE 5000

CMD ["python", "src/main.py"]