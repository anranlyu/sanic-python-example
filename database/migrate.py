import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()


def create_tables():
    """
    Crea las tablas necesarias en la base de datos.
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            port=int(os.getenv("MYSQL_PORT", "3306")),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "root_password"),
            database=os.getenv("MYSQL_DATABASE", "test_db"),
        )

        if connection.is_connected():
            cursor = connection.cursor()
            create_items_table_query = """
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_items_table_query)
            connection.commit()
            print("Tabla 'items' creada exitosamente.")

            create_users_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_users_table_query)
            connection.commit()
            print("Tabla 'users' creada exitosamente.")

    except Error as e:
        print(f"Error al crear las tablas: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("Conexión a la base de datos cerrada.")


if __name__ == "__main__":
    create_tables()
