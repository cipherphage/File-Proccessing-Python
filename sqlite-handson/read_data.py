from connect_db import get_database_connection

def read_data_from_db():
    """
    Return data from database.
    """

    sql_query = ''' SELECT author,title,due_date FROM authors; '''

    con = get_database_connection()
    cur = con.cursor()

    cur.execute(sql_query)
    results = cur.fetchall()
    print(results)

    cur.close()
    con.close()  

    return results

read_data_from_db()