from connect_db import get_database_connection

def delete_data_from_db():
    """
    Delete selected data from database.

    execute the given sql statement to remove
    the extra data
    """

    sql_query = ''' DELETE FROM authors WHERE (author="Smith, John" AND pages=100); '''

    con = get_database_connection()
    con.execute(sql_query)
    con.commit()
    con.close()    

def update_data():
    sql_query = ''' UPDATE authors SET due_date="2020-10-31" WHERE author="Smith, John"; '''

    con = get_database_connection()
    con.execute(sql_query)
    con.commit()
    con.close()

delete_data_from_db()
update_data()