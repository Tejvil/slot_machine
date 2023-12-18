import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbol definitions
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

def check_winnings(columns, lines, bet, values):
    """
    Check for winning combinations in the slot machine.

    Parameters:
        columns (list): 2D list representing the slot machine columns.
        lines (int): Number of lines to bet on.
        bet (int): Bet amount on each line.
        values (dict): Dictionary specifying the value of each symbol.

    Returns:
        tuple: Total winnings and a list of winning lines.
    """
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a random spin result for the slot machine.

    Parameters:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Dictionary specifying the count of each symbol.

    Returns:
        list: 2D list representing the slot machine columns.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []

    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    """
    Print the slot machine grid.

    Parameters:
        columns (list): 2D list representing the slot machine columns.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    """
    Get the initial deposit amount from the user.

    Returns:
        int: Deposited amount.
    """
    while True:
        try:
            amount = int(input("What would you like to deposit? $$$"))
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    return amount

def get_number_of_lines():
    """
    Get the number of lines to bet on from the user.

    Returns:
        int: Number of lines.
    """
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on (1-{MAX_LINES})? "))
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        except ValueError:
            print("Please enter a valid number.")

    return lines

def get_bet():
    """
    Get the bet amount from the user.

    Returns:
        int: Bet amount.
    """
    while True:
        try:
            amount = int(input(f"What would you like to bet on each line? ($1 - ${MAX_BET}) $$$"))
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        except ValueError:
            print("Please enter a valid number.")

    return amount

def spin(balance):
    """
    Execute a single spin of the slot machine.

    Parameters:
        balance (int): Current balance of the player.

    Returns:
        int: Net change in balance after the spin.
    """
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    if winning_lines:
        print(f"You won on lines: {', '.join(map(str, winning_lines))}")

    return winnings - total_bet

def main():
    """
    Main function to run the slot machine game.
    """
    print("Welcome to the Slot Machine Game!")
    balance = deposit()

    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to spin (Q to quit): ").lower()

        if answer == "q":
            break

        balance += spin(balance)

        if balance <= 0:
            print("Oops! You've run out of money.")
            break

    print(f"Thank you for playing! You left with ${balance}")

if __name__ == "__main__":
    main()
