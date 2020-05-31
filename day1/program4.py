cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

profit = sp - cp
profitPer = 100 * (profit/cp)
print("Profit: ", profit, "\nProfit Percentage: ", profitPer, "%")

profit += (105/100)*profit
print("Selling price when profit is increased by 5%: ", (cp+profit))
