
import math
import numpy

students = []
courses = []
studentMarks = []

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



def inputStudentInfor(students):
    id = input("Input student's id: ")
    name = input("Input student's name: ")
    dOB = input("Input students's DOB: ")
    student = Student(id, name, dOB)
    students.append(student)

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


def listCourses():
    print("Course List:")
    for c in courses:
        c.describe()


def listStudents():
    print("Student List:")
    for s in students:
        s.describe()


def showMarks():
    courseName = input("Input course's name to show marks: ")
    print("Student Marks for " + courseName)
    for studentMark in studentMarks:
        if courseName == studentMark.getCourse().getName():
            studentMark.describe()

def calculateAvg(id):
    marks = []
    for studentMark in studentMarks:
        if (studentMark.getStudent().getId() == id):
            marks.append(studentMark.getMark())
    return numpy.average(marks)



def showAvarage():
    id = input("Input student id: ")
    for s in students:
        if id == s.getId():
            print("Name: " + s.getName() + " Avg: " + str(s.getAvg()))

def sort():
    sortedList = sorted(students, key=lambda x: x.gpa, reverse=True)
    for s in sortedList:
        s.describe()

def calculateSum(id):
    sum = 0
    for c in courses:
        smark = []
        warray = []
        for studentMark in studentMarks:
            if (studentMark.getStudent().getId == id):
                smark.append(studentMark.getMark())
                warray.append(c.etc)
        weights = numpy.array(warray)
        amark = numpy.array(smark)
        sum = sum + numpy.sum(numpy.dot(amark, weights))
    return sum

def showSum():
    id = input("Input student id: ")
    print("Weighted sum: " + str(calculateSum(id)))

def menu():
    choice = "-1";
    while (choice != "0"):
        print("""
                   MENU
            1. Add students
            2. Add courses
            3. Add marks
            4. Show student list
            5. Show course list
            6. Show mark list
            7. Calculate average score
            8. Calculate weighted sum
            9. Sort student list
            0. Exit
            """)
        choice = input("Input your choice: ")
        if (choice == "1"):
            inputStudentInfor()
        elif (choice == "2"):
            inputCoursesInfor()
        elif (choice == "3"):
            inputMark()
        elif (choice == "4"):
            listStudents()
        elif (choice == "5"):
            listCourses()
        elif (choice == "6"):
            showMarks()
        elif (choice == "7"):
            showAvarage()
        elif (choice == "8"):
            showSum();
        elif (choice == "9"):
            sort();

menu()
