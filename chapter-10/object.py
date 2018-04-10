'''
Object.py
by Nate Weeks April 2018
'''

class Student(object):
    ''' object that returns attendance based on an input of name, days absent, days tardy,
    and days present.  Defaults are set to 0 '''
    def __init__(self, name, absent=0, tardy=0, present=0):
        self.name = name
        self.absent = absent
        self.tardy = tardy
        self.present = present

    def dailyAttendance(self, number):
        ''' given and input of 1, 2 or 3, adds 1 to present, tardy, or absent respectively'''
        if number == 2:
            self.tardy += 1
        elif number == 3:
            self.absent += 1
        elif number == 1:
            self.present += 1
        else:
            print "please enter 1 for present, 2 for tardy or 3 for absent"

    def getAbsent(self):
        '''returns days absent'''
        return self.absent

    def getTardy(self):
        '''returns days tardy'''
        return self.tardy

    def getPresent(self):
        '''returns days present'''
        return self.present

    def getName(self):
        '''returns name'''
        return self.name

    def __str__(self):
        '''prints name + total attendance'''
        return "name: %s, total days present: %d total days absent: %d, total days tardy: %d" % (self.name, self.present, self.absent, self.tardy)

def main():
    bob = Student("bob")
    bob.dailyAttendance(3)
    bob.dailyAttendance(2)
    bob.dailyAttendance(1)
    bob.dailyAttendance("bob ain't here bro")
    print bob.getName()
    print bob.getAbsent()
    print bob.getTardy()
    print bob.getPresent()
    print bob
    fred = Student("fred", 17, 5, 89)
    print fred

main()
