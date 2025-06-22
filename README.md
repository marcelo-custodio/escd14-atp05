# 📇 API de Contatos - FastAPI + GraphQL

Uma API simples para gerenciamento de contatos, desenvolvida com **FastAPI** e suporte a **GraphQL**, pronta para execução com **Docker Compose**.

---

## 🐳 Como Rodar com Docker Compose

### Pré-requisitos

- Docker instalado

### Passos

```bash
# Clone o repositório
git clone https://github.com/marcelo-custodio/escd14-atp05.git
cd escd14-atp05

# Suba os serviços
docker-compose up --build -d
# Execute o script de teste
python test_api.py
