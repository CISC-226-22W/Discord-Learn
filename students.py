import random


class Classroom:
    def __init__(self, studentList, subject, ):
        self.studentList = studentList

class Event:
    def __init__(self, dueDate, startDate, typeEvent):
        self.dueDate = dueDate
        self.startDate = startDate
        self.typEvent = typeEvent

class Test(Event):
    def __init__(self, dueDate, startDate, typeEvent, duration):
        Event.__init__(self, dueDate, startDate, typeEvent)
        self.duration = duration


class StudentList:
    def __init__(self):
        self.holder = ()

    def addStudent(self, name):
        self.holder += (name,)

    def checkAttendence(self, names):  # names is a list of the users in the channel
        absents = []
        for student in students:
            found = False
            for name in names:
                if name == student:
                    found = True
                    break
            if not found:
                absents.append(student)
        return absents

    def makeGroup(self, numOfGroups):
        if numOfGroups > len(self.holder):
            return ('cannot make groups of', numOfGroups)
        remainder = len(self.holder) % numOfGroups
        numOfPeoplePerGrp = len(self.holder)//numOfGroups
        groups = []
        l = list(self.holder)
        random.shuffle(l)
        rearranged = tuple(l)
        j = 0
        c = 0
        groups.append(())
        for name in rearranged:
            groups[c] += (name,)
            j+=1
            if (j == numOfPeoplePerGrp):
                groups.append(())
                j = 0
                c +=1
        return groups


# # attendence tester
# student = StudentList()
# students = ['john', 'barbara', 'jeffrey', 'jpnanda', 'panda']
# # names = ['john', 'barbara', 'jeffrey', 'jpnanda']
# for s in students:
#     student.addStudent(s)

# # print(student.checkAttendence(names))
# print(student.makeGroup(2))