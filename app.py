import pyodbc
import os
from dotenv import dotenv_values

config = dotenv_values()
# Connect to the SQL server
SERVER = config.get("SERVER")
DATABASE = config.get("DATABASE")
USERNAME = config.get("USERNAME")  
PASSWORD = config.get("PASSWORD")

connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString) 

# Create a cursor object
cursor = conn.cursor()

def get_word_list():
    
    # Execute a query to retrieve the list
    cursor.execute("SELECT Word FROM tWords")

    # Fetch all the results into a list
    word_list = [row[0] for row in cursor.fetchall()]


    return word_list


def update_word_list(newItem):

    # Add a new word to the database
    cursor.execute(f"""
                   INSERT INTO tWords (Word) 
                   VALUES('{newItem}')
                   """)
    cursor.commit()


def delete_word_list(deletion):

    # Execute a query to retrieve the list
    cursor.execute(f"DELETE FROM tWords WHERE Word='{deletion}'")
    cursor.commit()



def closeConnection():
    # Close the cursor and connection
    cursor.close()
    conn.close()






