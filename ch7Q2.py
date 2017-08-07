# Philip Holtzman
# Computer Logic
# July 18th 2017
# Week 5 Assignment 2

# I guess python doesnt really have constants
PRICE_A = 20
PRICE_B = 15
PRICE_C = 10

SECTION_TOTAL_A = 300
SECTION_TOTAL_B = 500
SECTION_TOTAL_C = 200

# will read about bools in python soon i promise
aTrue = 0
bTrue = 0
cTrue = 0

# really necessary function
def calcIncomeGenerated(seatsSold,PRICE):
  total = seatsSold*PRICE
  return total
  
# while loops to check input
while aTrue == 0:
  seatsSoldA = int(input("Enter total seats sold for section A (0-300).."))
  if (seatsSoldA >= 0 and seatsSoldA <= SECTION_TOTAL_A):
    aTrue = 1
  else:
    print("invalid.. maximum for Section A is 300 ")

while bTrue == 0:
  seatsSoldB = int(input("Enter total seats sold for section B (0-500).."))
  if (seatsSoldB >= 0 and seatsSoldB <= SECTION_TOTAL_B):
    bTrue = 1
  else:
    print("invalid.. Maximum for Section B is 500 ")
    
while cTrue == 0:
  seatsSoldC = int(input("Enter total seats sold for section C (0-200).."))
  if (seatsSoldC >= 0 and seatsSoldC <= SECTION_TOTAL_C):
    cTrue = 1
  else:
    print("invalid..Maximum for Section C is 200 ")
    
    
totalA = calcIncomeGenerated(seatsSoldA,SECTION_TOTAL_A)
totalB = calcIncomeGenerated(seatsSoldB,SECTION_TOTAL_B)
totalC = calcIncomeGenerated(seatsSoldC,SECTION_TOTAL_C)

# I should have made this a function
totalIncome = totalA+totalB+totalC

print("Total income : $%d"% totalIncome)

# whoa.. venues can make alot of money.. 


