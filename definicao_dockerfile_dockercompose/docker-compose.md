⚙️ 2️⃣ Docker Compose – “Como rodar vários containers juntos”

📘 Função:
É um orquestrador que define como rodar um ou mais containers juntos (cada um pode vir do seu Dockerfile).

👉 Pensa assim:

Docker Compose é o “forno” onde você assa vários bolos ao mesmo tempo, dizendo como e onde cada um vai.

🍽️ Exemplo de docker-compose.yml
    version: "3.9"

    services:
    web:
        build: .
        ports:
        - "5000:5000"
        depends_on:
        - db

    db:
        image: postgres:15
        environment:
        POSTGRES_USER: user
        POSTGRES_PASSWORD: senha
        POSTGRES_DB: meu_banco
        volumes:
        - dados_pg:/var/lib/postgresql/data

    volumes:
    dados_pg:

Para usar:

    docker-compose up

💡 Aqui o Compose:

    Lê o Dockerfile do serviço web
    Baixa a imagem postgres do serviço db
    Sobe os dois containers juntos, conectados
    Cria volumes e variáveis de ambiente
    Facilita o desenvolvimento e testes locais