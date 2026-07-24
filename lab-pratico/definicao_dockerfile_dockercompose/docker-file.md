🧱 1️⃣ Dockerfile – “Como construir a imagem”

📘 Função:
Define como criar a imagem do seu container — ou seja, as instruções de montagem (qual sistema usar, o que instalar, o que copiar, o que rodar).

👉 Pensa assim:

Dockerfile é o “receita do bolo”.
Ele explica como fazer o bolo (a imagem).

🍳 Exemplo de Dockerfile (para um app Flask):
        
        # Escolhe a base
        FROM python:3.11-slim

        # Define o diretório de trabalho
        WORKDIR /app

        # Copia o código para dentro da imagem
        COPY . .

        # Instala dependências
        RUN pip install flask

        # Expõe a porta
        EXPOSE 5000

        # Comando que roda o app
        CMD ["python", "app.py"]

Para usar:

    docker build -t meu_app_flask .
    docker run -p 5000:5000 meu_app_flask


🧩 Aqui o Dockerfile:

    Constrói a imagem
    Define o que vai dentro do container
    É individual (um container por vez)


🧩 Fluxo completo de um projeto Dockerfile

    # 1. Criar imagem
    docker build -t meu_app_flask .

    # 2. Ver imagens disponíveis
    docker images

    # 3. Rodar um container
    docker run -p 5000:5000 meu_app_flask

    # 4. (opcional) ver containers rodando
    docker ps