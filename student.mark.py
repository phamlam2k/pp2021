students = []
students_ID = []
courses = []
courses_id = []
marks = []


def input_information_of_students():
    def input_number_student():
        Num = int(input("Enter the numbers of student:"))
        if Num <= 0:
            print("There is no students")
            return 0
        else:
            return Num


def get_infomation_of_student():
    print("Get infomation of student to the course:")
    info = {
        'ID': '',
        'Name': '',
        'DOB': ''
    }
    print("Enter StudentID:")
    info['ID'] = id = input()
    print("Enter StudentName:")
    info['Name'] = input()
    print("Enter date of brith:")
    info['DOB'] = input()
    students.append(info)
    students_ID.append(id)


def get_infomation_of_courses():
    print("Number of courses")
    number_courses = int(input("Enter the number of courses:"))
    if (number_courses <= 0):
        print("There is no courses in here")
        return 0
    else:
        return number_courses


def get_id_of_courses():
    name = input("Enter the name of course")
    id = input("Enter the id of course")
    info = {
        'name': name,
        'id': id,
    }
    courses.append(info)
    courses_id.append(id)


def marks():
    print("Enter marks of students:")
    info = {
        'courseid': '',
        'idofstudents': '',
        'marks': '',
    }
    info['courseid'] = a = input()
    if a in courses_id:
        print("Enter student id:")
        info['idofstudents'] = a1 = input()
        if a1 in students_ID:
            print("Enter marks:")
            info['marks'] = float(input())
        else:
            return -1
    else:
        return -1
    marks.append(info)

def show_student():
    print("List Student")
    for i in range(0,len(students)):
        print(f"id:{students[i]['id']} name:{students[i]['name']} DoB:{students[i]['DoB']}")
def show_courses():
    print("Show lists of courses:")
    for i in range(0, len(courses)):
        print("[", courses[i]['cID'], "]", "[", courses[i]['Name'], "]", )
def show_marks():
    print("Show marks of students:")
    for i in range(len(students)):
        print("[", marks[i]['coID'], "]", "[", marks[i]['ID'], "]", "[", marks[i]['marks'], "]", )

def StudentManagement():
    print("_____")
    print("""please choose option you want:
    1.  Input  courses:
    2.  Stop """)
    option = int(input("Choose:"))
    if option == 1:
        Nco = get_infomation_of_courses()
        print("1.Add course:")
        print("2.Stop")
        option1 = int(input("Choose:"))
        if option1 == 1:
            for i in range(Nco):
                get_id_of_courses()
                Num = input_information_of_students()
                for i in range(Num):
                    print("1. Input student:")
                    print("2.Stop:")
                    option2 = int(input("Choose:"))
                    if option2 == 1:
                        for i in range(Num):
                            get_infomation_of_student()
                            show_courses()
                            show_student()
                            print("1.Add marks:")
                            print("2.Stop:")
                            option3 = int(input("Choose:"))
                            if option3 == 1:
                                marks()
                                show_courses()
                                show_student()
                                show_marks()
                                break
                            else:
                                exit()
                    else:
                        exit()
        else:
            exit()
    else:
        print("Out of service:")
        exit()


show_marks()
StudentManagement()

