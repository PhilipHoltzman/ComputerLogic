# Philip Holtzman
# Question 2

"""
2. Sales Prediction: A company has determined that its annual profit is typically 23 percent of total sales. Design a program that asks the user to enter the projected amount of total sales, and then displays the profit that will be made from that amount.
Hint: Use the value 0.23 to represent 23 percent.
"""

annual_profit = 0.23
print(" ")
projected_sales = float(input("Enter projected sales? "))
print(" ")
print("Profit from projected sale: " , annual_profit * projected_sales)