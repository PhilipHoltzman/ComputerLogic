# Philip Holtzman
# Aug 4th, 2017
# Ch. 10 Problem 2


counter = 0

# enter the names
names = input("Enter some names.. ")

# write the names to the file and close the file
with open('names.dat', 'r+') as f:
  f.write(names)
f.closed

# open file and split names to seperate words and add counter
with open('names.dat', 'r+') as f:
  for line in f:
      words = line.split()
      counter += len(words)
f.closed

print("Total names in list... ")
print(counter)