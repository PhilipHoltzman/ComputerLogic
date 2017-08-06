# Philip Holtzman
# Computer Logic
# July 18th 2017
# Week 5 Assignment 1



def calcGrossPay(hourlyPayRate,numberHoursWorked):
  grossPay =hourlyPayRate*numberHoursWorked
  
  return grossPay

payTrue = 1
hoursTrue = 1

while payTrue == 1:
  hourlyPayRate = float(input("Enter hourly rate.."))
  if(hourlyPayRate >= 7.5 and hourlyPayRate <= 18.25):
    payTrue = 0
  else:
    print("Invalid.. enter 7.5 to 18.25")

while hoursTrue == 1:
  numberHoursWorked = int(input("Enter number hours.."))
  if(numberHoursWorked >= 0 and numberHoursWorked <= 40):
    hoursTrue = 0
  else:
    print("Invalid.. enter 0 thru 40 please")

grossPay = calcGrossPay(hourlyPayRate,numberHoursWorked)

print("")
print("Employee gross pay: $%d" % grossPay)