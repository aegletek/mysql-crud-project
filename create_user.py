from db_connector import MySQLConnector

def create_student(name, email):
    db = MySQLConnector()
    query = "INSERT INTO students(name, email) VALUES(%s, %s)"
    rows = db.execute_query(query, (name, email))
    db.close()
    return rows
