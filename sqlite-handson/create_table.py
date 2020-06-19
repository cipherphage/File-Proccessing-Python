from connect_db import get_database_connection

def create_table():
    """
    Creates a table ready to accept our data.

    write code that will execute the given sql statement
    on the database
    """

    create_table = """ CREATE TABLE authors(
        ID          INTEGER PRIMARY KEY     AUTOINCREMENT,
        author      TEXT                NOT NULL,
        title       TEXT                NOT NULL,
        pages       INTEGER             NOT NULL,
        due_date    CHAR(15)            NOT NULL
    )   
    """

    con = get_database_connection()
    con.execute(create_table)
    con.close()

def populate_table():
    contract_list = [
        ["Amith, Aohn", "Life of John", 1200, "2029-11-15"],
        ["Zmith, Zohn", "Life of Smith", 1200, "2029-11-15"],
        ["Smith, John", "Of John Smith", 100, "2029-11-15"],
        ["Gmith, Gohn", "Of John", 1200, "2029-11-15"],
        ["Rmith, Rohn", "Of Smith", 1200, "2029-11-15"],
        ["Smith, John", "John Smith", 1200, "2029-11-15"],
    ]
    add_data_stmt = ''' INSERT INTO authors(author,title,pages,due_date) VALUES(?,?,?,?); '''

    con = get_database_connection()
    con.executemany(add_data_stmt, contract_list)
    con.commit()
    con.close()

create_table()
populate_table()