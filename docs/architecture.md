# 🏗️ Arquitetura do Projeto

## 📌 Visão Geral

Este projeto implementa uma **aplicação web em Python** totalmente **containerizada com Docker** e executada localmente por meio do **Docker Compose**. A arquitetura foi pensada para ser **simples, clara e extensível**, servindo tanto para estudos quanto para uso como projeto de portfólio DevOps.

O foco principal é demonstrar:

* Separação clara entre aplicação e infraestrutura
* Reprodutibilidade de ambiente
* Facilidade de execução local
* Base pronta para evolução (CI/CD, cloud, múltiplos serviços)

---

## 🧩 Componentes da Arquitetura

### 1️⃣ Aplicação Web

* Desenvolvida em **Python**
* Responsável por atender requisições HTTP
* Executa dentro de um container Docker

### 2️⃣ Docker

* Empacota a aplicação e suas dependências
* Garante consistência entre ambientes (dev, CI, produção)
* Define como a aplicação é construída e iniciada

### 3️⃣ Docker Compose

* Orquestra a execução dos containers localmente
* Define portas, variáveis de ambiente e dependências
* Facilita o uso com um único comando (`docker compose up`)

### 4️⃣ CI (GitHub Actions)

* Executa automaticamente a cada push ou pull request
* Sobe o ambiente via Docker Compose
* Executa testes automatizados
* Garante qualidade e estabilidade do código

---

## 🔄 Fluxo de Funcionamento

O fluxo completo da aplicação ocorre da seguinte forma:

1. O desenvolvedor altera o código da aplicação
2. O código é versionado e enviado ao GitHub
3. O pipeline de CI é acionado automaticamente
4. O Docker constrói a imagem da aplicação
5. O Docker Compose sobe o container
6. Os testes automatizados são executados
7. A aplicação fica disponível localmente via porta exposta

---

## 🗂️ Estrutura de Diretórios

```
web-app-docker/
├── src/                     # Código-fonte da aplicação
│   └── app.py
│
├── tests/                   # Testes automatizados
│
├── .github/workflows/       # Pipelines de CI (GitHub Actions)
│   └── ci.yml
│
├── Dockerfile               # Build da imagem Docker
├── docker-compose.yml       # Orquestração local
├── requirements.txt         # Dependências Python
├── README.md                # Documentação principal
└── architecture.md          # Documento de arquitetura
```

---

## 🔐 Considerações de Segurança e Boas Práticas

* Containers isolam a aplicação do sistema host
* Dependências são controladas via `requirements.txt`
* Pipeline automatizado evita deploys com código quebrado
* Estrutura preparada para uso de variáveis de ambiente

---

## 🚀 Possíveis Evoluções da Arquitetura

* Adicionar banco de dados (PostgreSQL, MySQL)
* Criar `docker-compose.prod.yml`
* Implementar healthchecks
* Deploy em cloud (AWS, Azure, GCP)
* Adicionar observabilidade (logs, métricas)

---

## 📘 Conclusão

A arquitetura atual é propositalmente simples, mas **segue padrões reais do mercado**, permitindo que o projeto evolua de forma organizada à medida que novos componentes sejam adicionados.
