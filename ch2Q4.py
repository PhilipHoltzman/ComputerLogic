# Philip Holtzman
# Computer Logic Question 4
"""
4. Total Purchase
A customer in a store is purchasing five items. Design a program that asks for the price of each item, and then displays the subtotal of the sale, the amount of sales tax, and the total. Assume the sales tax is 6 percent.
"""

tax = .06

print(" ")
item1 = float(input("Please enter price for item 1: "))
item2 = float(input("Please enter price for item 2: "))
item3 = float(input("Please enter price for item 3: "))
item4 = float(input("Please enter price for item 4: "))
item5 = float(input("Please enter price for item 5: "))

subtotal = item1+item2+item3+item4+item5

print("Subtotal is: ", subtotal)

tax_of_sub = subtotal * tax

print("Tax is: ", tax_of_sub)

net_total = tax_of_sub + subtotal

print("Total price is: ", net_total)

