from create_user import create_student
from retrieve_user import get_student, get_all_students
from update_user import update_student
from delete_user import delete_student

if __name__ == "__main__":
    create_student("John Doe", "john@example.com")
    print(get_all_students())
    print(get_student(3))
    update_student(3, "John Updated", "updated@example.com")
    print(get_student(1))
    #delete_student(1)
    print(get_all_students())
