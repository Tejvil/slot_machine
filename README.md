# Slot Machine Game Documentation

## Introduction
This Python script simulates a simple slot machine game. Players can deposit money, place bets on multiple lines, and spin the slot machine reels to win or lose money based on the symbols that appear on the lines.


# project link
[click here](https://github.com/Tejvil/slot_machine.git)


## Code Structure

### Constants
- `MAX_LINES`: Maximum number of lines to bet on.
- `MAX_BET`: Maximum bet amount.
- `MIN_BET`: Minimum bet amount.
- `ROWS`: Number of rows in the slot machine.
- `COLS`: Number of columns in the slot machine.
- `symbol_count`: Dictionary specifying the count of each symbol.
- `symbol_value`: Dictionary specifying the value of each symbol.

### Functions

#### `check_winnings(columns, lines, bet, values)`
- Checks for winning combinations in the slot machine.
- Returns total winnings and the lines where the player won.

#### `get_slot_machine_spin(rows, cols, symbols)`
- Generates a random spin result for the slot machine.
- Returns a 2D list representing the slot machine columns.

#### `print_slot_machine(columns)`
- Prints the slot machine grid.

#### `deposit()`
- Takes user input for the initial deposit amount.
- Returns the deposited amount.

#### `get_number_of_lines()`
- Takes user input for the number of lines to bet on.
- Ensures a valid input within the specified range.
- Returns the number of lines.

#### `get_bet()`
- Takes user input for the bet amount on each line.
- Ensures a valid input within the specified range.
- Returns the bet amount.

#### `spin(balance)`
- Executes a single spin of the slot machine.
- Handles user input for the number of lines and bet amount.
- Checks if the player has enough balance to place the bet.
- Prints the slot machine result, winnings, and winning lines.
- Returns the net change in balance.

#### `main()`
- Main function to run the slot machine game.
- Manages the overall flow of the game, including depositing money and spinning the slot machine.
- Prints the final balance when the player decides to quit.


## Usage
1. Run the script.
2. Enter the initial deposit amount.
3. Press enter to spin the slot machine or 'Q' to quit.
4. Observe the results of each spin and the final balance.
