
from datetime import datetime

class DateTimeConverte(object):

    def __init__(self, datetime):
        self._datetime_input = datetime

        self.year = None
        self.month = None
        self.day = None

        self.__convertToJavaScriptDate()


    def __convertToJavaScriptDate(self):
        self.year = self._datetime_input.year
        self.month = int(self._datetime_input.month) - 1
        self.day = self._datetime_input.day



if __name__ == '__main__':
    print("Call as Main")
    a = datetime(2012, 7, 2)
    print(datetime)
    b = DateTimeConverte(a)
    print(b.day)
    print(b.month)
    print(b.year)
