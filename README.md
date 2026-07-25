# Docker to Train 🐳

> Um repositório prático e progressivo para **dominar Docker** através de exercícios reais e desafios graduados.

Docker na prática com uma estrutura pedagógica bem organizada, seguindo um caminho de aprendizado que vai desde o básico até conceitos avançados.

---

## 📚 Sobre este Repositório

Este projeto é um **guia hands-on de Docker** com exercícios estruturados em 3 módulos que cobrem:

- **Módulo 1 - Básico**: Conceitos fundamentais e suas primeiras imagens Docker
- **Módulo 2 - Intermediário**: Aplicações reais, volumes, networks e otimizações
- **Módulo 3 - Avançado**: Orquestração, multi-stage builds, segurança e boas práticas

Cada exercício é independente e inclui um `README.md` com instruções, Dockerfile comentado e exemplos prontos para executar.

---

## 🎯 O que você vai aprender

- ✅ Criar e gerenciar **imagens Docker**
- ✅ Construir e rodar **containers**
- ✅ Dominar **Dockerfiles** (instruções, layers, otimizações)
- ✅ Trabalhar com **portas, volumes e variáveis de ambiente**
- ✅ Usar **Docker Compose** para aplicações multi-container
- ✅ Implementar **best practices** de segurança e performance
- ✅ Deploy em produção com **imagens otimizadas**

---

## 📦 Estrutura do Repositório

```
lab-pratico/
├── definicao_dockerfile_dockercompose/  # Guias teóricos
├── mod1-basico/                         # 10 exercícios (Hello World até portas)
├── mod2-intermediario/                  # 10 exercícios (Flask, volumes, nginx)
└── mod3-avancado/                       # 10 exercícios (Django, React, CI/CD, segurança)
```

---

## 🚀 Quick Start

### Pré-requisitos

- **Docker Desktop** (ou Docker Engine) instalado e rodando
- **Git** (para clonar o repositório)
- Editor de texto/código

### Instalação

```bash
git clone https://github.com/mariaandrezacs/docker-to-train.git
cd docker-to-train
```

---

## 📖 Guia de Aprendizado

### 🟢 Nível 1: Básico (mod1-basico)

Comece aqui se é seu primeiro contato com Docker!

| Ex. | Tema | Conteúdo |
|-----|------|----------|
| 01 | Hello Python | Seu primeiro container |
| 02 | Hello Node | Imagem com Node.js |
| 03 | HTML + Nginx | Servindo arquivos estáticos |
| 04 | Variáveis de Ambiente | ENV no Dockerfile |
| 05 | Alpine | Imagens leves e otimizadas |
| 06 | ENTRYPOINT vs CMD | Diferenças e uso |
| 07 | WORKDIR e COPY | Estruturando o container |
| 08 | RUN e instalações | Camadas de build |
| 09 | EXPOSE | Expondo portas |
| 10 | ENV avançado | Passando variáveis em runtime |

### 🟡 Nível 2: Intermediário (mod2-intermediario)

Integre aplicações reais e aprenda padrões de produção.

| Ex. | Tema | Conteúdo |
|-----|------|----------|
| 01 | Flask App | Aplicação web Python |
| 02 | Express App | Aplicação web Node.js |
| 03 | Multi-stage Build | Otimizando imagens Go |
| 04 | Logs e Volumes | Persistência de dados |
| 05 | Nginx customizado | Reverse proxy e configurações |
| 06 | Cron Jobs | Tarefas agendadas |
| 07 | ARG e build-time | Argumentos de construção |
| 08 | Git e ferramentas | Instalando tools adicionais |
| 09 | Usuário non-root | Segurança básica |
| 10 | RUN complexo | Otimizando layers |

### 🔴 Nível 3: Avançado (mod3-avancado)

Domine Docker Compose, segurança, e deploy em produção.

| Ex. | Tema | Conteúdo |
|-----|------|----------|
| 21 | Django Prod | Aplicação Django otimizada |
| 22 | React + Nginx | Frontend com build multi-stage |
| 23 | CI/CD Docker | Integração contínua |
| 24 | Permissões | Gerenciamento de usuários |
| 25 | Healthcheck | Verificação de saúde |
| 26 | Distroless | Imagens mínimas e seguras |
| 27 | Entrypoint Script | Scripts complexos de inicialização |
| 28 | OpenCV | Dependências complexas |
| 29 | Docker Compose | Orquestração multi-container |
| 30 | Build Cache | Otimizando o build |

---

## 💡 Dicas de Uso

### Explorar um exercício
```bash
cd lab-pratico/mod1-basico/ex01_hello_python
cat README.md    # Leia as instruções
cat Dockerfile   # Estude o Dockerfile
docker build -t ex01 .
docker run ex01
```

### Ver histórico de imagens
```bash
docker images | grep ex
docker rmi ex01  # Remove a imagem
```

### Entrar em um container (debugging)
```bash
docker run -it ex01 /bin/bash
# ou
docker run -it ex01 sh
```

### Limpar tudo (containers e imagens)
```bash
docker system prune -a
```

---

## 📚 Recursos Complementares

- [Documentação Oficial Docker](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---



🚀
