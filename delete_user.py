from db_connector import MySQLConnector

def delete_student(student_id):
    db = MySQLConnector()
    rows = db.execute_query(
        "DELETE FROM students WHERE id=%s",
        (student_id,)
    )
    db.close()
    return rows
