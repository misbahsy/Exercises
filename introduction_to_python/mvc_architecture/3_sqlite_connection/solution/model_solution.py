import sqlite3

def create():
    conn = sqlite3.connect('student.db')
    print("Created db")
    conn.execute('''CREATE TABLE IF NOT EXISTS STUDENT
                            (ID INT  NOT NULL,
                            NAME    TEXT    NOT NULL); ''')
    print('Table created')
    conn.close()

def query():
    conn = sqlite3.connect('student.db')
    print("Opened database successfully")

    conn.execute("INSERT INTO STUDENT (ID, NAME) VALUES (20, 'abc')")
    conn.execute("INSERT INTO STUDENT (ID, NAME) VALUES (21, 'xyz')")
    conn.commit()

    # cursor = conn.execute("SELECT id, name from STUDENT")
    # for row in cursor:
    #     return
    cursor = conn.cursor()
    data = cursor.fetchall()

    print("Operation done successfully")
    conn.close()
    return data

