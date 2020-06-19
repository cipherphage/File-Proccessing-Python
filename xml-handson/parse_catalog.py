import sqlite3
import sys
import defusedxml.ElementTree as ET

DB_NAME = "author_contracts.db"

def update_db(isbn_data_list):
    """ 
    add code to execute each sql_stmt in the order given
    results from sql_query_3 should be assigned to results
    """
    
    sql_query_1 = ''' ALTER TABLE authors ADD COLUMN isbn CHAR(20); '''

    sql_query_2 = "UPDATE authors SET isbn = ? WHERE title = ?;"

    sql_query_3 = ''' SELECT isbn FROM authors;'''

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    con.execute(sql_query_1)
    con.commit()

    con.executemany(sql_query_2, isbn_data_list)
    con.commit()

    cur.execute(sql_query_3)
    results = cur.fetchall()

    cur.close()
    con.close()

    # test code
    expected_results = [('000-1-000000-00-1',), ('000-2-000000-00-2',), ('000-3-000000-00-3',), ('000-4-000000-00-4',), ('000-5-000000-00-5',)]

    assert results == expected_results

# using 'isbn.xml'
# loop through "book" in file and append isbn and title as a list object to isbn_data_list
# send isbn_data_list to function update_db

file_name = 'isbn.xml'

try:
    tree = ET.parse(file_name)
except:
    print("File not found")
    sys.exit(1)

isbn_data_list = []
for book in tree.findall('book'):
    title = book.findtext('title')
    isbn = book.findtext('isbn')
    isbn_data_list.append((isbn, title))

update_db(isbn_data_list)
