
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


def inputNumberofStudent():
    numOfStudent = int(input("Input the number of Student : "));
    return numOfStudent;
def inputNumberofCourse():
    numofCourse = int(input("Input the number of Course : "));
    return numofCourse;

def infoStudent():
    id = str(input("Input ID of Student : "));
    name = str(input("Input Name of Student : "));
    DoB = str(input("Input Date of Birth : "));
    student = Student(id,name,DoB);
    ListStudent.append(student);
    

def infoCourse():
    idCourse = str(input("Input ID of Course : "));
    nameCourse = str(input("Input name of Course : "));
    course = Course(idCourse,nameCourse);
    ListCourse.append(course);

def inputMark():
    mark = float(input("Input mark of course : "));
    Listmarks.append(mark);

def getInfoStudent():
    for i in range(0,len(ListStudent),1):
        print("===== Student " + str(i+1)+" =====");
        ListStudent[i].description();
        ListCourse[i].string();
        print("Diem mon hoc la : " + str(Listmarks[i]));

numberStudent = inputNumberofStudent();

for i in range(0,numberStudent,1):
    infoStudent();
    numberCourse = inputNumberofCourse();
    for i in range(0,numberCourse,1):
        infoCourse();
        inputMark();


getInfoStudent();