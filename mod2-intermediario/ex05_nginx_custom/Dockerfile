# Etapa 1: imagem base
FROM nginx:latest

# Etapa 2: remover a configuração padrão
RUN rm /etc/nginx/conf.d/default.conf

# Etapa 3: copiar a configuração customizada
COPY nginx.conf /etc/nginx/nginx.conf

# Etapa 4: copiar página HTML
COPY index.html /usr/share/nginx/html/index.html

# Expor a porta 80
EXPOSE 80

# Etapa 5: manter o Nginx em execução
CMD ["nginx", "-g", "daemon off;"]
