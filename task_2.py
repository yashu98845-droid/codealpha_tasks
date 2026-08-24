stock_price = {
    "AAPL": 150.00,
    "TSLA": 700.00,
    "GOOGL": 2800.00,
    "AMZN": 3400.00,
}
n = int(input("Enter the number of stocks you want to check: "))
total_investment = 0      
for i in range(n):
    stock_name = input("Enter the stock name (AAPL, TSLA, GOOGL, AMZN): ")
    quantity = int(input("Enter the quantity of stocks you want to buy: "))
    investment = stock_price[stock_name] * quantity
    total_investment += investment
print(f"The total investment: ${total_investment:.2f}")
   
