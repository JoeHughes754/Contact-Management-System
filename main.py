import sqlite3
from prettytable import PrettyTable

#connect to an existing database and if the database does not exist, then it will be automatically created.
conn = sqlite3.connect('demo.db')
cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT)")
    conn.commit()

def display_table():
    cur.execute('SELECT * FROM contact')
    myTable = PrettyTable(["ID", "First Name", "Last Name", "Email"])
    for row in cur.fetchall():
        myTable.add_row([row[0],row[1], row[2], row[3]])
    print(myTable)

def insert_data(first_name, last_name, email):
    cur.execute("INSERT INTO contact VALUES (NULL,?,?,?)", ( first_name, last_name, email))
    conn.commit()
    print("-----------------------------------------")
    print("Data have successfully inserted.....")
    print("-----------------------------------------")

def update_data(first_name, last_name, email):
    cur.execute("update member set first_name = '%s', \
                last_name='%s' where email='%s'"%(first_name,last_name,email))
    conn.commit()
    print("---------------------------------------")
    print("Data have successfully updates.....")
    print("---------------------------------------")

def delete_data(email):
    cur.execute("delete from contact where email='%s'"%(email))
    conn.commit()
    print("-------------------------------")
    print("Data have successfully deleted..............")
    print("-------------------------------")

def delete_data_with_id(id):
    cur.execute("delete from contact where id='%s'"%(id))
    conn.commit()
    print("-------------------------------")
    print("Data have successfully deleted..............")
    print("-------------------------------")
    
# create_table()
# insert_data("Joe", "Hughes", "jhughes@hotmail.com")

display_table()
