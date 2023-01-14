class WeekDayError(Exception):
    pass

class Weeker:
    __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    __dow = 0
    
    def __init__(self, day):
        if day in self.__days:
            self.__dow = self.__days.index(day)
        else:
            raise WeekDayError 
    
    def __str__(self):
        return self.__days[self.__dow]
    
    def add_days(self, n):
        self.__dow = self.__dow + (n % 7) 
    
    def sub_days(self, n):
        self.__dow = self.__dow - (n % 7)
    
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.sub_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")