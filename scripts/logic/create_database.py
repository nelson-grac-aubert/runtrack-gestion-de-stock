import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Misstouille83!sql" 
        )
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE store")
        print("Base de données 'store' créée avec succès.")

        cursor.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("La base de données 'store' existe déjà.")
        else:
            print(f"Erreur lors de la création de la base : {err}")
    

def create_tables():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Misstouille83!sql",
            database="myzoo"
        )
        cursor = connection.cursor()

        cursor.execute("USE store;")

        TABLES = {}

        TABLES["product"] = (
            """
            CREATE TABLE product (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            price INT NOT NULL,
            quantity INT NOT NULL,
            id_category INT  NOT NULL
            );
            """
        )

        TABLES["category"] = (
            """
            CREATE TABLE category (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
            );
            """
        )

        for name, query in TABLES.items():
            cursor.execute(query)
            print(f"Table '{name}' vérifiée/créée.")

    except mysql.connector.Error as err:
        print(f"Erreur lors de la création des tables : {err}")

if __name__ == "__main__":

    create_database()
    create_tables()