from db_connector import MySQLConnector

def update_student(student_id, name, email):
    db = MySQLConnector()
    rows = db.execute_query(
        "UPDATE students SET name=%s, email=%s WHERE id=%s",
        (name, email, student_id)
    )
    db.close()
    return rows
