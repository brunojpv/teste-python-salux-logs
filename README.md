# 📄 Projeto de Simulação de Logs - COPY vs Executemany com PostgreSQL

Este projeto demonstra duas formas de inserir registros de logs em um banco PostgreSQL:

- Usando **`executemany`** (inserções em lote via `INSERT`)
- Usando **`COPY`** (inserção de alto desempenho com buffer)

Você pode executá-los **de fato com Docker e PostgreSQL**. Também foram adicionados **testes automatizados com `pytest`**.

---

## 📁 Estrutura do Projeto

```
project/
├── docker-compose.yml                # PostgreSQL container
├── init/init.sql                     # Criação da tabela logs
├── requirements.txt                  # Dependências
├── README.md                         # Instruções do projeto
├── src/
│   ├── process_log_copy_real.py             # COPY real
│   └── process_log_executemany_real.py      # executemany real
└── tests/
    └── test_logs.py                  # Testes automatizados
```

---

## 🐳 Rodando com Docker + PostgreSQL real

1. Suba o container PostgreSQL:
```bash
docker compose up -d
```

2. Dados de acesso:
```
Host: localhost
Porta: 5432
Banco: test
Usuário: postgres
Senha: salux
```

3. Tabela `logs` criada automaticamente via `init/init.sql`

---

## 🧪 Testando

1. Crie ambiente virtual e instale dependências:
```bash
python -m venv venv
venv\Scripts\activate  # ou source venv/bin/activate no Linux/mac
pip install -r requirements.txt
```

2. No `tests/test_logs.py`, altere o import para o modo real desejado:
```python
from process_log_copy import process_log
# ou
from process_log_executemany import process_log
```

3. Rode os testes:
```bash
pytest
```

---

## 🧪 Testes com `pytest`

Testes estão configurados para verificar os seguintes cenários:
- Inserção de 0, 1, 5 e 10 registros
- Rodam com qualquer modo (`simulado` ou real)

```bash
pytest
```

---

## 📦 Requisitos

- Python 3.10+
- Docker (para rodar o PostgreSQL)
- PostgreSQL 15 (via Docker)
- `psycopg2-binary`, `pandas`, `aiohttp`, `pytest`

Instale tudo com:
```bash
pip install -r requirements.txt
```

---

## ✍️ Autor

**Bruno Vieira**  
💻 Desenvolvedor .NET e Python  
🔗 [linkedin.com/in/brunojpv](https://www.linkedin.com/in/brunojpv)

> Projeto criado para teste técnico com simulação real e ambientes controlados.
