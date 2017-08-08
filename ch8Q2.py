# Philip Holtzman
# Jul 28th 2017
# Ch.8 Problem 2 

# import random, gotta do it weird like this cuz repl.it
from random import randrange

# initialize list
lotteryNum = [0,0,0,0,0,0,0]

# run through the list assigning elements to random()
for i in range(len(lotteryNum)):
  lotteryNum[i] = randrange(10)

#print it out.. 
print("Todays Winning number is: ", *lotteryNum, sep='')
  
  