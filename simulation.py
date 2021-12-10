
from random import randrange
class queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return self.items==[]
    def size(self):
        return len(self.items)

class doctor:
    def __init__(self, ageperminute):
        self.ageperminute = ageperminute
        self.currentpatient = None
        self.timeremaining = 0

    def tick(self):
        if self.currentpatient != None:
            self.timeremaining = self.timeremaining - 1
            if self.timeremaining == 0:
                self.currentpatient = None

    def busy(self):
        if self.currentpatient != None:
            return True
        else:
            return False

    def startnext(self, nextpatient):
        self.currentpatient = nextpatient
        self.timeremaining = nextpatient.getage() * 60 / self.ageperminute


class Patient:
    def __init__(self, time):
        self.timestamp = time
        self.age = randrange(20, 61)

    def getstamp(self):
        return self.timestamp

    def getage(self):
        return self.age

    def waittime(self, currentsecond):
        return currentsecond - self.timestamp


def simulation(numsecond, ageperminute):
    doctorclinic = doctor(ageperminute)
    doctorqueue = queue()
    waittime = []
    for currentsecond in range(numsecond):
        if randrange(1, 361) == 360:
            patient = Patient(currentsecond)
            doctorqueue.enqueue(patient)
        if (not doctorclinic.busy()) and (not doctorqueue.is_empty()):
            nextpatient = doctorqueue.dequeue()
            waittime.append(nextpatient.waittime(currentsecond))
            doctorclinic.startnext(nextpatient)
        doctorclinic.tick()
    averagewaittime = sum(waittime) / len(waittime)
    print("Avrage wait", "{:.2f}".format(averagewaittime), "sec", doctorqueue.size(), "patient remaining")


for i in range(10):
    simulation(4 * 3600, 5)
