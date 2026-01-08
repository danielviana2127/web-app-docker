# Web App em Python com Docker 🐳

## 🚀 Visão Geral

Este projeto é uma **aplicação web simples em Python**, containerizada com **Docker** e orquestrada com **Docker Compose**. Ele foi criado com foco em **boas práticas de DevOps**, servindo como base de estudo e portfólio para conceitos como:

* Versionamento com Git
* Containerização com Docker
* Orquestração local com Docker Compose
* Testes automatizados
* Integração Contínua (CI)

---

## 📦 Arquitetura do Projeto

Estrutura recomendada do repositório:

```
web-app-docker/
├── src/
│   └── app.py              # Código principal da aplicação
│
├── tests/                  # Testes automatizados
│
├── .github/workflows/      # Pipelines de CI (GitHub Actions)
│
├── Dockerfile              # Build da imagem da aplicação
├── docker-compose.yml      # Orquestração local dos containers
├── requirements.txt        # Dependências Python
└── README.md               # Documentação do projeto
```

### 📌 Observações de Arquitetura

* O código da aplicação foi isolado na pasta `src/` para facilitar escalabilidade e manutenção.
* Os arquivos de infraestrutura permanecem na raiz por simplicidade.
* A separação entre código, testes e automação segue padrões usados em projetos profissionais.

---

## 🧑‍💻 Como Executar o Projeto

### Pré-requisitos

* Docker
* Docker Compose

### Passo a passo

```bash
git clone https://github.com/danielviana2127/web-app-docker.git
cd web-app-docker
docker compose up -d --build
```

A aplicação ficará disponível em:

```
http://localhost:5000
http://localhost:8000/health
```

---

## 🧪 Executando os Testes

Com o ambiente configurado:

```bash
pytest
```

Os testes garantem que a aplicação continue funcionando corretamente após alterações no código.

---

## 🔄 CI/CD (Integração Contínua)

O projeto utiliza **GitHub Actions** para executar testes automaticamente a cada:

* Push
* Pull Request

Isso ajuda a manter a qualidade do código e evitar que erros cheguem à branch principal.

---

## 🐳 Docker — Boas Práticas Aplicadas

* Imagem base enxuta (`python-slim`)
* Dependências instaladas via `requirements.txt`
* Build reprodutível
* Inicialização clara da aplicação via `CMD`

---

## 📌 Próximas Evoluções (Roadmap)

* Separar ambientes (dev / prod)
* Adicionar variáveis de ambiente com `.env`
* Criar `docker-compose.prod.yml`
* Adicionar linting (flake8 ou ruff)
* Deploy em cloud (AWS / Azure / GCP)

---

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Faça um fork do projeto
2. Crie uma branch (`feature/minha-feature`)
3. Commit suas alterações
4. Abra um Pull Request

---

## 🪪 Licença

Este projeto é livre para fins educacionais e de estudo.
