FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos do host para o contêiner
COPY . .

# Cria o diretório de logs dentro do contêiner
RUN mkdir -p /var/logs/app

# Instala as dependências (boa prática: usar um requirements.txt se houver)
RUN pip install --no-cache-dir flask

# Define o comando de execução
CMD ["python", "app.py"]
