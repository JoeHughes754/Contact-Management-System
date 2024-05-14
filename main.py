import sqlite3
from prettytable import PrettyTable

#connect to an existing database and if the database does not exist, then it will be automatically created.
conn = sqlite3.connect('demo.db')
cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT))")
    conn.commit()

def display_table():
    cur.execute('SELECT * FROM member')
    myTable = PrettyTable(["ID", "First Name", "Last Name", "Email"])
    for row in cur.fetchall():
        myTable.add_row([row[1], row[2], row[3]])
    print(myTable)

def insert_data(id, first_name, last_name, email):
    cur.execute("INSERT INTO member VALUES (?,?,?,?)", (id, first_name, last_name, email))
    conn.commit()
    print("-----------------------------------------")
    print("Data have successfully inserted.....")
    print("-----------------------------------------")

