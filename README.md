# M3 - Banco de Dados (Streaming)

Projeto da disciplina de Banco de Dados (M3). É uma aplicação de terminal em Python
que gerencia um banco de dados de uma plataforma de **streaming**, com cadastro de
usuários, vídeos e histórico de visualização. A navegação é feita por um menu com setas.

## Requisitos

- Python 3
- MySQL rodando localmente

## Instalação

```bash
# clone o repositório e entre na pasta
git clone <url-do-repositorio>
cd M3-Banco_de_dados

# crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/macOS
# venv\Scripts\activate       # Windows

# instale as dependências
pip install -r requirements.txt
```

Antes de iniciar, confira os dados de conexão com o MySQL em `config/database.py`
(host, usuário, senha e nome do banco).

## Como iniciar

```bash
python main.py
```

O banco de dados é criado automaticamente na primeira execução. Use as **setas**
para navegar no menu e **Enter** para selecionar.
