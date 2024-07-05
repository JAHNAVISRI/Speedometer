import mysql.connector
import os

def create_database_and_table():
    db = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="Jahnavi",
        password="Mobisjanu@99"
    )

    cursor = db.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS speedometer_db")
    cursor.execute("USE speedometer_db")

    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS speed_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        speed INT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.close()
    db.close()

if __name__ == "__main__":
    create_database_and_table()