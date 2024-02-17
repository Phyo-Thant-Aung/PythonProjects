def main():

    # Ask how many cents the customer is owed
    change = get_change()

    cents = int(change * 100)

    # Calculate the number of quarters to give the customer
    quarters = int(calculate_quarters(cents))
    cents = cents - quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = int(calculate_dimes(cents))
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = int(calculate_nickels(cents))
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = int(calculate_pennies(cents))
    cents = cents - pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(f"{coins}")

def get_change():
    while True:
        try:
            change = float(input("Change owed: "))
            if change > 0:
                break
        except ValueError:
            print("Please input the correct positive number of change")
    return change

def calculate_quarters(cents):
    quarters = cents / 25
    return quarters

def calculate_dimes(cents):
    dimes = cents / 10
    return dimes

def calculate_nickels(cents):
    nickels = cents / 5
    return nickels

def calculate_pennies(cents):
    pennies = cents / 1
    return pennies

main()