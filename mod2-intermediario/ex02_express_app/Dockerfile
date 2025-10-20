FROM node:20-alpine

WORKDIR /app

# Copia apenas os arquivos de dependência primeiro (melhor para cache)
COPY package.json /app/

# Instala as dependências
RUN npm install express

# Copia o restante do código
COPY . .

# Expõe a porta usada pelo app
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["node", "app.js"]


# FROM node:20-alpine

# WORKDIR /app

# # Cria o package.json e instala o express dentro do container
# RUN npm init -y && npm install express

# # Copia o código da aplicação
# COPY . .

# # Expõe a porta
# EXPOSE 3000

# CMD ["node", "app.js"]
