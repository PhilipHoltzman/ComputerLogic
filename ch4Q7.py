# Philip Holtzman
# July 2017
# Week 3, Assignment 7

price = 99

discount20 = .20
discount30 = .30
discount40 = .40
discount50 = .50

total = 0
discountRate = 0

netTotal = 0

custOrder = int(input("Enter number of orders.. "))

total = custOrder * price

if custOrder < 10:
  print("Sorry.. No discount..")
  print('Total: $%d' % total)

elif custOrder >= 10 and custOrder <= 19:
  discountRate = total * discount20
  netTotal = total - discountRate
  print("20 percent discount!")
  print('Discount amount: $%d' % discountRate)
  print('Total: $%d' % netTotal)
  
elif custOrder >= 20 and custOrder <= 49:
  discountRate = total * discount30
  netTotal = total - discountRate
  print("30 percent discount!!")
  print('Discount amount: $%d' % discountRate)
  print('Total: $%d' % netTotal)
  
elif custOrder >= 50 and custOrder <= 99:
  discountRate = total * discount40
  netTotal = total - discountRate
  print("40 percent discount!!!")
  print('Discount amount: $%d' % discountRate)
  print('Total: $%d' % netTotal)
  
else:
  discountRate = total * discount50
  netTotal = total - discountRate
  print("50 percent discount!!!!")
  print('Discount amount: $%d' % discountRate)
  print('Total: $%d' % netTotal)
  
  
  