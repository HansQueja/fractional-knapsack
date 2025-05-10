
# Acts as the stock data structure containing the stock's name, price, profit, and ROI
class Stock:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
        self.ROI = 0

    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nReturn Profit: {self.profit}"
    
