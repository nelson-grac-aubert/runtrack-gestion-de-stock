import mysql.connector

def access_database(database_name, host_name="localhost", user_name="root", pass_word="Misstouille83!sql") : 
    
    database = mysql.connector.connect(
        host = host_name,
        user = user_name,
        password = pass_word,
        database = database_name
    )

    return database

def point_cursor(database) : 

    return database.cursor()

def close_everything_properly(cursor, database) : 

    cursor.close()
    database.close()