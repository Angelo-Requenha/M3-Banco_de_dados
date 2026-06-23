from config.database import connect_db

def create_db():
    conexion = connect_db()

    try:
        with open('create_db/schemas/streaming.sql', 'r') as f:
            sql_script = f.read()

        with conexion.cursor() as cursor:
            cursor.execute(sql_script)

    except Exception as e:
        print(f"Error to execute SQL script: {e}")

    finally:
        conexion.close()
    