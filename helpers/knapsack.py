
def fractional_knapsack(stock_list, remaining_budget):
    
    # Compute for the Profit per Cost Ratio (ROI) for each stock
    for stock in stock_list:
        stock.ROI = stock.profit / stock.price

    # Sort stocks in descending order based on their ROI which takes O(nlogn)
    stock_list.sort(key=lambda stock: stock.ROI, reverse=True)

    count = 0
    total_profit = 0
    
    print("==============================================================================\n")

    # Choose the stock with the largest ROI
    while count < len(stock_list):

        print(f"\tInvested Stock #{count + 1}")

        # If stock price is within the remaining budget, invest in the stock
        if stock_list[count].price <= remaining_budget:
            remaining_budget -= stock_list[count].price
            total_profit += stock_list[count].profit

            print(f"\tName: {stock_list[count].name}\n\tPrice: {stock_list[count].price}\n\tProfit: {stock_list[count].profit}\n")
            count += 1

        # If its out of the budget, get the fractional value that we can fit in it
        else:
            fraction_cost = remaining_budget / stock_list[count].price
            total_profit += round(fraction_cost * stock_list[count].profit, 3)

            print("\t(Fractional Stock)")
            print(f"\tName: {stock_list[count].name}\n\tPrice: {fraction_cost * stock_list[count].price}\n\tProfit: {round(fraction_cost * stock_list[count].profit, 3)}\n")
            count += 1
            break
    
    # Show the total profit we've accumulated
    print(f"\tTotal profit: Php. {total_profit}")
    print(f"\tTotal number of stocks: {count}")
    print("\n==============================================================================\n")
