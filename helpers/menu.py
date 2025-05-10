
import json
from helpers.stock import Stock

# Menu function to get the user's budget and stock items
def menu():
    option = 0

    while option not in [1, 2, 3]:
        print("==============================================================================")
        print("\n\tWelcome to your trusted Stock Portfolio Evaluator!")
        print("\tWhat's your total budget (in Peso) for this instance?")

        # Get a valid budget input from the user
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

        # Get a valid integer input from the user
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


# Function to get the stock items manually from the user iteratively
def manual_input():
    print("==============================================================================")
    
    # Loop until all said number of items are taken
    while True:
        print("\tHow many stock items are you going to enter?\n")

        # Get a valid integer input for the number of items
        try:
            stock_count = int(input("\t=> "))

            # Program requires at least two input values.
            if stock_count < 2:
                print("\tWarning: You need to enter at least two items. Please try again.")
                continue
            
            stock_list = []
            count = 0

            # Loop through number of stocks
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


# Function to get the user's stock list through a JSON file in the /data directory
def json_input():
    print("==============================================================================")
    
    # Loop until proper file is given
    while True:
        print("\n\tWhat's your JSON's file name?")
        file_name = 'data/' + input("\t=> ")
        
        # Require user to upload a JSON file
        if ".json" not in file_name:
            print("\tWARNING: File needs to be of JSON type. Please try again.")
            continue

        # Try to open and read the contents of JSON file.
        # If the file is invalid, missing, or empty, return an error
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