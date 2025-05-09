
from helpers.stock import Stock

def fractional_knapsack(stock_list, remaining_budget):
    
    # Compute for the Profit per Cost Ratio (ROI) for each stock
    for stock in stock_list:
        stock.ROI = stock.price / stock.profit

    # Sort stocks in descending order based on their ROI
    sorted(stock_list, key=lambda stock: stock.ROI, reverse=True)

    count = 0
    total_profit = 0

    # Choose the stock with the largest ROI
    while True and count < len(stock_list):
        if stock_list[count].price <= remaining_budget:
            remaining_budget - stock_list[count].price
            total_profit += stock_list[count].profit
            print(f"\tName: {stock_list[count].name}\n\tPrice: {stock_list[count].price}\n\tProfit: {stock_list[count].profit}\n")
            count += 1
        else:
            fraction_cost = remaining_budget / stock_list[count].price
            total_profit += round(fraction_cost * stock_list[count].profit, 3)
            print(f"\tName: {stock_list[count].name}\n\tPrice: {fraction_cost}\n\tProfit: {total_profit}\n")
            break
    
    print(f"\n\tTotal profit: Php. {total_profit}")
