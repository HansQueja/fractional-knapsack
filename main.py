
from helpers.menu import menu
from helpers.knapsack import fractional_knapsack

def stock_application():
    
    # Ask user if they want to type the values or read an existing JSON file
    # Store data that the algorithm will process
    stock_list, budget = menu()

    # Call the algorithm with the data provided 
    # Get a return value of the choices made, and the total profit
    fractional_knapsack(stock_list, budget)

    # Ask the user if they want to run the application again


if __name__ == "__main__":
    stock_application()