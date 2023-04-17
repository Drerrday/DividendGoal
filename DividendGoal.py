"""
Created by Hunter Elam
Python 3.9
IDE: IntelliJ
Dec. 17, 2020
"""

def dividend_calculator(stock_price, div_yield, shares, goal_dividend):
    # Real Action
    investment = stock_price * shares
    annual_div = stock_price * div_yield
    qtr_div = annual_div / 4

    # Calculate the number of shares needed for the goal dividend
    shares_needed = goal_dividend / annual_div

    # Formatting
    print("*" * 100)
    print("At ${:.2f} per share".format(stock_price))
    print("You have ${:.2f} invested into this particular company.".format(investment))
    print()
    print("Quarterly Payouts (3-months)")
    print("Quarterly Dividend PER SHARE: {:.2f} cents".format(qtr_div))
    print("Quarterly Dividend ALL SHARES: ${:.2f}".format(qtr_div * shares))
    print()
    print("Yearly Payouts (12-months)")
    print("Annual Dividend PER SHARE: {:.2f} cents".format(annual_div))
    print("Annual Dividend ALL SHARES: ${:.2f}".format(annual_div * shares))
    print()
    print("Goal dividend: ${:.2f}".format(goal_dividend))
    print("To reach the goal dividend, you would need to own approximately {:.0f} shares.".format(shares_needed))
    print("{} more shares at the current stock price of ${:.2f} would mean you would have to invest an additional ${:.2f}".format(int(shares_needed) - shares, stock_price, (int(shares_needed) - shares) * stock_price))
    print("*" * 100)

while True:
    # Collect user input
    stock_price = float(input("Please enter the current stock price: "))
    div_yield = float(input("Please enter the current dividend yield (as a percentage): ")) / 100
    shares = int(input("Please enter the amount of shares owned: "))
    goal_dividend = float(input("Please enter your goal dividend: "))

    # Call the function with user input
    dividend_calculator(stock_price, div_yield, shares, goal_dividend)

    # Ask user if they want to run the program for another company
    response = input("Do you want to run the program for another company? (y/n): ")
    if response.lower() != "y":
        break

# Call the function with user input
dividend_calculator(stock_price, div_yield, shares, goal_dividend)
input()






