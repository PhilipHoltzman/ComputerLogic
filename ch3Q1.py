# Philip Holtzman
# July 2017
# Week 3, Assignment 1


userNumber = int(input('Enter in number: '))

if userNumber >= 1 and userNumber <= 10:
  if userNumber == 1:
    print("Roman Numeral: I")
  if userNumber == 2:
    print("Roman Numeral: II")
  if userNumber == 3:
    print("Roman Numeral: III")
  if userNumber == 4:
    print("Roman Numeral: IV")
  if userNumber == 5:
    print("Roman Numeral: V")
  if userNumber == 6:
    print("Roman Numeral: VI")
  if userNumber == 7:
    print("Roman Numeral: VII")
  if userNumber == 8:
    print("Roman Numeral: VIII")
  if userNumber == 9:
    print("Roman Numeral: IX")
  if userNumber == 10:
    print("Roman Numeral: X")
else:
  print("Out of bounds..")

