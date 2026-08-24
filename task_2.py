stock_price = {
    "AAPL": 150.00,                                    
    "TSLA": 700.00,
    "GOOGL": 2800.00,
    "AMZN": 3400.00, 
}                                  # Dictionary to store stock prices
n = int(input("Enter the number of stocks you want to check: "))          # Get the number of stocks from the user
total_investment = 0                        # Variable to keep track of the total investment
for i in range(n):                           # Loop to iterate through the number of stocks
    stock_name = input("Enter the stock name (AAPL, TSLA, GOOGL, AMZN): ")           # Get the stock name from the user
    quantity = int(input("Enter the quantity of stocks you want to buy: "))          # Get the quantity of stocks from the user
    investment = stock_price[stock_name] * quantity                      # Calculate the investment for the current stock
    total_investment += investment                                   # Add the current investment to the total investment
print(f"The total investment: ${total_investment:.2f}")          # Display the total investment to the user




#THIS IS A chatbot SIMPLE CODE.
# THANK YOU FOR USING THIS CODE. I HOPE YOU ENJOYED IT.
   
