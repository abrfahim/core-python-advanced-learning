# A static method is a type of method that belongs to a class but does not bind to a class or instance.

import  datetime

class TimeUtility:

    @staticmethod
    def getTime():
        return datetime.datetime.now()

    @staticmethod
    def getDifference(date_from):
        return datetime.datetime.now() - date_from
print(TimeUtility.getTime())

anotherTime = datetime.datetime(1995, 3, 7)

print(TimeUtility.getDifference(anotherTime))
