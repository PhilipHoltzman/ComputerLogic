# Philip Holtzman
# Jul 28th 2017
# Ch.9 Problem 2 

# initialize array 
names = [None]*20

# initialize variables for loop and control
addNames = True
i = 0

# user input loop
while addNames == True:
  names[i] = input("Enter name: ") # input to array
  if i == 19 or names[i] == '': # terminators
    addNames = False
  i += 1

# sloppy way of removing None type and blanks
names1 = [x for x in names if x is not None]
names2 = [x for x in names1 if x is not '']

names3 =sorted(names2) # re init list sorted A-Z

print("") # add a lil space for visibility 

#print em out!! 
for i in names3:
  print(i)