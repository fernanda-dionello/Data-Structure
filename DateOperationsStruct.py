from calendar import weekday
from DateStruct import DateStruct

class DateOperationsStruct:

    month31 = [1,3,5,7,8,10,12]
    month30 = [4,6,9,11]
    month2829 = [2]
    yearsRange = range(-5000, 5000)
    weekDays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    months = ["January", "February", "March", "April", "June", "July", "August", "September", "October", "November", "December"]

    def __init__(self, date):
        self.date = date
    
    def getYear(self):
        return self.year
    
    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day
    
    def setYear(self, year):
        if(self.yearIsValid(year)):
            self.year = year
        else:
            raise Exception("Invalid year")
    
    def setMonth(self, month):
        if(self.monthIsValid(month)):
            self.month = month
        else:
            raise Exception("Invalid month")

    def setDay(self, day):
        if(self.dayIsValid(day)):
            self.day = day
        else:
            raise Exception("Invalid day")

    def __str__(self):
        return f"{self.month}/{self.day}/{self.year}"
    
    def readDate(self):
        self.day = int(input("Day: "))
        self.month = int(input("Month: "))
        self.year = int(input("Year: "))
    
    def isValid(self) -> bool:
        return self.dayIsValid(self.day) and self.monthIsValid(self.month) and self.yearIsValid(self.year)

    def dayIsValid(self, day):
        valueMaxDay = self.getMaxDayValue(self.month)
        return day in range(1, valueMaxDay + 1)
    
    def monthIsValid(self, month):
        return month in range(1,13)
    
    def yearIsValid(self, year):
        return year in self.yearsRange
    
    def getMaxDayValue(self, month):
        if(month in self.month31):
            return 31
        elif(month in self.month30):
            return 30
        elif(month in self.month2829):
            return 28
    
    def isLeapYear(self) -> bool:
        if self.yearIsValid(self.year) and self.year % 4 == 0:
            if self.year % 100 == 0 and self.year % 400 != 0:
                return False
            else:
                return True
        else:
            return False
    
    def easterDay(self):
        #Using Gauss algorithm
        #Based fonts:
        # 1 - https://www.daniweb.com/programming/software-development/code/463551/another-look-at-easter-dates-python
        # 2 - https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch38.html
        if self.isValid():
            month = 3
            golden = (self.year % 19) + 1
            century = self.year // 100 + 1
            xx = (3 * century) // 4 - 12
            yy = (8 * century + 5) // 25 - 5
            zz = (5 * self.year) // 4 - xx - 10
            ee = (11 * golden + 20 + yy - xx) % 30
            if ee == 24:
                ee += 1
            if ee == 25 and golden > 11:
                ee += 1
            moon = 44 - ee
            if moon < 21:
                moon += 30
            day = (moon + 7) - ((zz + moon) % 7)
            if day > 31:
                day -= 31
                month = 4

            return DateStruct(day, month, self.year)
        else:
            return "Invalid data entry"

    def weekDay(self):
        # Code reference: https://java2blog.com/get-day-of-week-in-python/
        if self.isValid():
            month, day = self.month, self.day
            if month == 1:
                month = 13
                self.year -= 1
            elif month == 2:
                month = 14
                self.year -= 1
            remain = self.year % 100    
            intYearDivision = self.year // 100
            f = (day + int(13*(month + 1)/5.0) + remain + int(remain/4.0))
            fg = f + int(intYearDivision/4.0) - 2 * intYearDivision
            fdiv = f + 5 - intYearDivision
            if self.year > 1582:
                dayNumber = fg % 7
            else:
                dayNumber = fdiv % 7
            if dayNumber == 0:
                dayNumber = 7
            return self.weekDays[dayNumber - 1]
        else:
            return "Invalid data entry"
    
    def monthName(self):
        if self.monthIsValid(self.month):
            return self.months[self.month - 1]
        else:
            return "Invalid data entry"
    
    def dateInFull(self):
        if self.isValid():
            return f"{self.weekDay()}, {self.monthName()} {self.day}, {self.year}."
        else:
            return "Invalid data entry"   
