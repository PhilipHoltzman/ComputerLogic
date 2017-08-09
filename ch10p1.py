# Philip Holtzman
# Aug 4th, 2017
# Ch. 10 Problem 1


numbers = input("Enter a series of numbers.. ")

# quickly append to front of file.. 
with open('numbers.dat', 'r+') as f:
  f.write(numbers)
f.closed

# open the file using 'with' is better
with open('numbers.dat', 'r+') as f:
    read_data = f.read() 
    print(read_data) # print the data
f.closed # close it up


