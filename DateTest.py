from DateStruct import DateStruct
from DateOperationsStruct import DateOperationsStruct

date = DateStruct(0,0,0)
d = DateOperationsStruct(date)

d.readDate()
# print(d.isValid())
# print(d)
print(d.isLeapYear())
print(d.easterDay())
print(d.dateInFull())