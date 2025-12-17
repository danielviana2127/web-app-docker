# Web App Docker 🚀

Este projeto é uma aplicação web simples em **Python** containerizada com **Docker** e gerenciada via **Docker Compose**.  
O objetivo é demonstrar como empacotar e executar uma aplicação em containers de forma prática e escalável.

---

## 📂 Estrutura do projeto
- `app.py` → Código principal da aplicação (Flask ou similar).
- `requirements.txt` → Lista de dependências Python.
- `Dockerfile` → Instruções para criar a imagem Docker.
- `docker-compose.yml` → Orquestração de serviços.
- `tests/` → Testes automatizados.
- `.github/workflows/` → Configuração de CI/CD (GitHub Actions).

---

## ⚙️ Pré-requisitos
- [Python 3.10+](https://www.python.org/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ▶️ Como executar

### 1. Clonar o repositório
bash
git clone https://github.com/danielviana2127/web-app-docker.git
cd web-app-docker

### 2. Construir a imagem
docker build -t web-app-docker .

### 3. Rodar com Docker Compose
docker-compose up
A aplicação estará disponível em:
👉 http://localhost:5000

🧪 Testes
Execute os testes com:
pytest tests/

📦 Deploy
Este projeto pode ser facilmente implantado em qualquer servidor que suporte Docker.
Exemplo de deploy:
docker-compose -f docker-compose.yml up -d

🤝 Contribuição
1. Faça um fork do projeto
2. Crie uma branch (git checkout -b feature/nova-feature)
3. Commit suas alterações (git commit -m 'Adiciona nova feature')
4. Push para a branch (git push origin feature/nova-feature)
5. Abra um Pull Request

📜 Licença
Este projeto está sob a licença MIT.
Sinta-se livre para usar.
