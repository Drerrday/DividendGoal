"""
Created by Hunter Elam
Python 3.9
IDE: IntelliJ
Dec. 17, 2020
"""

# Initializers
stock_price = float(input("Please enter the current stock price: "))
div_yield = float(input("Please enter the current dividend yield: "))
shares = int(input("Please enter the amount of shares owned: "))
# Real Action
annual_div = stock_price * div_yield
qtr_div = annual_div / 4
goal_dividend = stock_price * shares

# Formatting
print("*" * 50)
print("Quarterly Payouts(3-months)")
print("Quarterly Dividend PER SHARE: {:.2f} cents".format(qtr_div))
print("Quarterly Dividend ALL SHARES: ${:.2f}".format(qtr_div * shares))
print()
print("Yearly Payouts (12-months)")
print("Annual Dividend PER SHARE: {:.2f} cents".format(annual_div))
print("Annual Dividend ALL SHARES: ${:.2f}".format(annual_div * shares))
print()
print("Cost to get to goal dividend: ${:.2f}".format(goal_dividend))
input()
