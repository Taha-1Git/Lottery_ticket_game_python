import random

# Constants
MAX_LINES = 3
MIN_LINES = 1
MAX_BET = 1000
MIN_BET = 100
ROWS = 3
COL = 3



# Symbol frequency and their values

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function to check winning lines
def check_win(columns, lines, bet, values):

    winning = 0

    winning_lines = []

    for line in range(lines):

        symbol = columns[0][line]

        for column in columns:

            if column[line] != symbol:

                break
        else:  
            winning += values[symbol] * bet

            winning_lines.append(line + 1)

    return winning, winning_lines

# Slot machine spin logic
def get_slot_machine_spin():

    all_symbols = []

    for symbol, count in symbol_count.items():

        all_symbols.extend([symbol] * count)

    columns = []

    for _ in range(COL):

        column = []

        current_symbols = all_symbols[:]

        for _ in range(ROWS):

            value = random.choice(current_symbols)

            current_symbols.remove(value)

            column.append(value)
            
        columns.append(column)

    return columns

# Print slot machine result
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Get deposit amount
def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Enter an amount greater than zero.")
        else:
            print("Enter a valid number.")

# Get number of lines
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to play on (1-3): ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter lines within the valid range (1-3).")
        else:
            print("Enter a valid number.")

# Get bet amount
def get_bet():
    while True:
        bet = input("Enter the amount you want to bet on each line: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Enter a bet between {MIN_BET} and {MAX_BET}.")
        else:
            print("Enter a valid number.")

# Core game logic for a single round
def game(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient balance. Your current balance is: {balance}")
        else:
            break

    print(f"\nYou are betting Rs.{bet} on {lines} lines. Total bet: Rs.{total_bet}")
    print(f"Remaining balance: Rs.{balance - total_bet}\n")

    slots = get_slot_machine_spin()
    print("Slot Machine Result:")
    print_slot_machine(slots)

    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print(f"\nYou won Rs.{winnings}")
    if winning_lines:
        print("You won on line(s):", ", ".join(str(line) for line in winning_lines))
    else:
        print("No winning lines this time.")

    return winnings - total_bet  # Net change in balance

# Main function
def main():
    balance = deposit()

    while True:
        print(f"\nYour current balance is: Rs.{balance}")
        answer = input("Press Enter to play (or type 'q' to quit): ")
        if answer.lower() == "q":
            break
        balance += game(balance)

    print(f"\nYou left with Rs.{balance}. Thanks for playing!")

main()
