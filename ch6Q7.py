# Philip Holtzman
# Computer Logic
# Week 4 assignment, ch.6 problem 7

# calculate average
def calcAverage(num1,num2,num3,num4,num5):
  average = (num1+num2+num3+num4+num5) / 5
  return average

# determine grade
def determineGrade(average):
  if average <= 59:
    print("Your grade is a F...")
  elif average >= 60 and average <= 69:
    print("Your grade is a D...")
  elif average >= 70 and average <= 79:
    print("Your grade is a C...")
  elif average >= 80 and average <= 89:
    print("Your grade is a B...")
  elif average >= 90 and average <= 100:
    print("Your grade is a A...")  
  else:
    print("Error")
    
#input then convert to int    
num1,num2,num3,num4,num5 = input("Enter the 5 test scores: ").split()
num1,num2,num3,num4,num5 = [int(num1), int(num2), int(num3), int(num4), int(num5)]

# pass to average variable
average = calcAverage(num1,num2,num3,num4,num5)

print("Your grade average is: %d " % average)

# pass average to grade report function
determineGrade(average)



