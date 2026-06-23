# mysql-connector-python - Resumo de Comandos

## Instalação

```bash
pip install mysql-connector-python
```

---

# Importação

```python
import mysql.connector
```

---

# Conectar ao banco

```python
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha",
    database="streaming"
)
```

---

# Verificar conexão

```python
if conexao.is_connected():
    print("Conectado")
```

---

# Criar cursor

```python
cursor = conexao.cursor()
```

---

# Executar SQL

```python
cursor.execute(
    "SELECT * FROM videos"
)
```

---

# SELECT

```python
cursor.execute(
    "SELECT * FROM videos"
)
```

---

# SELECT com parâmetros

```python
cursor.execute(
    "SELECT * FROM videos WHERE id_video = %s",
    (1,)
)
```

---

# Buscar um registro

```python
video = cursor.fetchone()
```

Retorna:

```python
(1, "Matrix", "videos/matrix.mp4")
```

---

# Buscar vários registros

```python
videos = cursor.fetchall()
```

Retorna:

```python
[
    (1, "Matrix"),
    (2, "Avatar")
]
```

---

# Inserir dados

```python
cursor.execute(
    """
    INSERT INTO videos
    (titulo, caminho_arquivo)
    VALUES (%s, %s)
    """,
    (
        "Matrix",
        "videos/matrix.mp4"
    )
)
```

---

# Confirmar alterações

```python
conexao.commit()
```

Necessário para:

* INSERT
* UPDATE
* DELETE

---

# Atualizar dados

```python
cursor.execute(
    """
    UPDATE videos
    SET titulo = %s
    WHERE id_video = %s
    """,
    (
        "Matrix Reloaded",
        1
    )
)

conexao.commit()
```

---

# Excluir dados

```python
cursor.execute(
    """
    DELETE FROM videos
    WHERE id_video = %s
    """,
    (1,)
)

conexao.commit()
```

---

# Obter ID inserido

```python
cursor.execute(
    """
    INSERT INTO videos
    (titulo)
    VALUES (%s)
    """,
    ("Matrix",)
)

conexao.commit()

print(cursor.lastrowid)
```

---

# Quantidade de linhas afetadas

```python
print(cursor.rowcount)
```

---

# Executar vários INSERTs

```python
dados = [
    ("Matrix",),
    ("Avatar",),
    ("Interestelar",)
]

cursor.executemany(
    """
    INSERT INTO videos
    (titulo)
    VALUES (%s)
    """,
    dados
)

conexao.commit()
```

---

# Rollback

```python
try:
    conexao.commit()
except:
    conexao.rollback()
```

---

# Fechar cursor

```python
cursor.close()
```

---

# Fechar conexão

```python
conexao.close()
```

---

# Estrutura básica recomendada

```python
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha",
    database="streaming"
)

cursor = conexao.cursor()

cursor.execute(
    "SELECT * FROM videos"
)

resultado = cursor.fetchall()

for video in resultado:
    print(video)

cursor.close()
conexao.close()
```

---

# Placeholders

## Correto

```python
cursor.execute(
    "SELECT * FROM videos WHERE id_video = %s",
    (1,)
)
```

```python
cursor.execute(
    """
    INSERT INTO videos
    (titulo)
    VALUES (%s)
    """,
    ("Matrix",)
)
```

## Errado

```python
cursor.execute(
    f"SELECT * FROM videos WHERE id_video = {id_video}"
)
```

Evite f-strings para SQL.
Use sempre `%s`.
