from db_connector import MySQLConnector

def get_student(student_id):
    db = MySQLConnector()
    result = db.fetch_one("SELECT * FROM students WHERE id=%s", (student_id,))
    db.close()
    return result

def get_all_students():
    db = MySQLConnector()
    result = db.fetch_all("SELECT * FROM students")
    db.close()
    return result
