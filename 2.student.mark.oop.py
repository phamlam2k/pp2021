
ListStudent = [];
ListCourse = [];
Listmarks = [];


class Student:
    def __init__(self,id,name,DoB):
        self.__id = id;
        self.__name = name;
        self.__DoB = DoB;

    def description(self):
        print("ID Student : " + self.__id +"\n"+ "Name : " +self.__name + "\n" + "Dob : "+ self.__DoB)

    def getID(self):
        return self.__id;
    def getName(self):
        return self.__name;
    def getDoB(self):
        return self.__DoB;

class Course:
    def __init__(self, idCourse,nameCourse):
        self.__idCourse = idCourse;
        self.__nameCourse = nameCourse;

    def string(self):
        print("ID course : " + self.__idCourse + "\n" + "Name of Course : " + self.__nameCourse);

    def getidCourse(self):
        return self.__idCourse;
    def getnameCourse(self):
        return self.__nameCourse;

class StudentMark:
    def __init__(self, student, course, mark):
        self.__student = student
        self.__course = course
        self.__mark = mark

    def getStudent(self):
            return self.__student

    def getCourse(self):
        return self.__course

    def describe(self):
        print(self.__student.getId() + " " + self.__student.getName() + " "
              + self.__course.getName() + " " + str(self.__mark))

def inputNumberOfStudents():
    n = int(input("Input number of student: "))
    return n


def inputStudentInfor(students):
    id = input("Input student's id: ")
    name = input("Input student's name: ")
    dOB = input("Input students's DOB: ")
    student = Student(id, name, dOB)
    students.append(student)


def inputNumberOfCourses():
    n = int(input("Input number of courses: "))
    return n


def inputCoursesInfor(courses):
    id = input("Input courses's id: ")
    name = input("Input courses's name: ")
    course = Course(id, name)
    courses.append(course)


def inputMark(students, courses, studentMarks):
    courseName = input("Input course's name to input marks: ")
    for c in courses:
        if c.getName() == courseName:
            for s in students:
                mark = float(input("Input " + s.getName() + "'s mark: "))
                studentMark = StudentMark(s, c, mark)
                studentMarks.append(studentMark)


def listCourses(courses):
    print("Course List:")
    for c in courses:
        c.string()


def listStudents(students):
    print("Student List:")
    for s in students:
        s.description()


def showMarks(studentMarks):
    courseName = input("Input course's name to show marks: ")
    print("Student Marks for " + courseName)
    for studentMark in studentMarks:
        if courseName == studentMark.getCourse().getName():
            studentMark.describe()


n = inputNumberOfStudents()
students = []
courses = []
studentMarks = []
while n > 0:
    inputStudentInfor(students)
    n -= 1
n = inputNumberOfCourses()
while n > 0:
    inputCoursesInfor(courses)
    n -= 1
inputMark(students, courses, studentMarks)
listStudents(students)
listCourses(courses)
showMarks(studentMarks)














