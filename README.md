# Web App Docker

## 📌 Descrição
Aplicação web simples empacotada com Docker, com foco em boas práticas DevOps, reprodutibilidade e automação.

## 🏗️ Arquitetura
A aplicação é executada dentro de um container Docker e orquestrada localmente via Docker Compose.

Detalhes completos em: `docs/architecture.md`

## 🚀 Como executar

### Pré-requisitos
- Docker
- Docker Compose

### Passo a passo
```bash
git clone https://github.com/danielviana2127/web-app-docker.git
cd web-app-docker
./scripts/run.sh

### Acesse a aplicação em:
http://localhost:8000
