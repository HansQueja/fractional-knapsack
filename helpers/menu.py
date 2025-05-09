
import json
from helpers.stock import Stock

def menu():
    option = 0

    while option not in [1, 2, 3]:
        print("==============================================================================")
        print("\n\tWelcome to your trusted Stock Portfolio Evaluator!")

        print("\tWhat's your total budget (in Peso) for this instance?")
        try:
            budget = float(input("\t=> "))
            if budget < 100:
                print("\tThe minimum budget is at least 100 pesos! Try again.")
                continue
        except Exception as e:
            print(f"\tWARNING: {e}")
            continue

        print("\tHow would you like your stock options read by the program?\n")
        print("\t[1] I will input it manually")
        print("\t[2] Read an existing JSON file")
        print("\t[3] Quit the program\n")

        try:
            option = int(input("\t=> "))
            if option not in [1, 2, 3]:
                print("\tSorry, you need to choose between the values 1 and 2 only! Try again.")
                continue
            
            if option == 1:
                return manual_input(), budget
            elif option == 2:
                return json_input(), budget
            else:
                print("\tThank you for using the program!")
                break
        except Exception as e:
            print(f"\tWARNING: {e}")


def manual_input():
    print("==============================================================================")
    
    while True:
        print("\tHow many stock items are you going to enter?\n")
        try:
            stock_count = int(input("\t=> "))

            if stock_count < 2:
                print("\tWarning: You need to enter at least two items. Please try again.")
                continue
            
            stock_list = []
            count = 0

            while count < stock_count:
                print(f"\n\tSTOCK #{count+1}\n")
                
                try:
                    stock_name = input("\tStock Name: ")
                    stock_price = float(input("\tStock Price: "))
                    stock_profit = float(input("\tStock Return Profit: "))
                    
                    stock_list.append(Stock(stock_name, stock_price, stock_profit))
                    count += 1
                except ValueError:
                    print("\tWarning: Enter a valid type.")
            
            print("\n\tValues are read.")
            return stock_list
        except ValueError:
            print("\tWarning: You need to enter a valid number of items. Please try again.")


def json_input():
    print("==============================================================================")
    
    while True:
        print("\n\tWhat's your JSON's file name?")
        file_name = 'data/' + input("\t=> ")
        
        if ".json" not in file_name:
            print("\tWARNING: File needs to be of JSON type. Please try again.")
            continue

        try:
            with open(file_name, 'r') as file:
                data = json.load(file)

            stock_list = []

            for stock in data['stocks']:
                new_stock = Stock(stock['name'], stock['price'], stock['profit'])
                stock_list.append(new_stock)
            
            print(f"\tStocks from {file_name} read.\n")
                
            return stock_list
        except json.decoder.JSONDecodeError:
            print("\tWARNING: The file is empty or contains invalid JSON.")
            continue
        except FileNotFoundError:
            print("\tWARNING: The file cannot be found. Please try again.")
            continue


if __name__ == "__main__":
    menu()