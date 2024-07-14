"""
Tic Tac Toe
"""

class TicTacToe:
    def __init__(self, player_symbol, size=3):
        # initialize the size of the board
        self.size = size
        self.symbol_list = [" " for _ in range(size * size)]  # create a size x size grid

        # initialize the player symbol
        self.player_symbol = player_symbol

    def restart(self):
        # clears the grid 
        self.symbol_list = [" " for _ in range(self.size * self.size)]

    def draw_grid(self):
        # display the column headers
        header = " " * 5 + "   ".join([chr(65 + i) for i in range(self.size)])
        print(f"\n{header}")

        for row in range(self.size):
            row_str = f" {row + 1} "
            row_str += " ║ ".join(self.symbol_list[row * self.size:(row + 1) * self.size])
            print(row_str)
            if row < self.size - 1:
                print(" " * 5 + " ║ ".join(["═══"] * (self.size - 1)))
    
    def edit_square(self, grid_coord):
        # Validate the input format
        if len(grid_coord) < 2:
            print("Invalid coordinate. Please enter in the format 'A1', 'B2', etc.")
            return

        # Swap coordinates such as "1A" to "A1"
        if grid_coord[0].isdigit():
            grid_coord = grid_coord[1] + grid_coord[0]

        col = grid_coord[0].capitalize()
        row = grid_coord[1]

        # Validate the coordinate
        if col not in [chr(65 + i) for i in range(self.size)] or row not in [str(i + 1) for i in range(self.size)]:
            print("Invalid coordinate. Please enter a valid coordinate.")
            return

        # Convert "A1" to the correct index in the list
        col_idx = ord(col) - 65
        row_idx = int(row) - 1
        grid_index = row_idx * self.size + col_idx

        if self.symbol_list[grid_index] == " ":
            self.symbol_list[grid_index] = self.player_symbol
        else:
            print("That square is already taken!")

    def update_symbol_list(self, new_symbol_list):
        self.symbol_list = new_symbol_list

    def did_win(self, player_symbol):
        sym = player_symbol

        # Check rows, columns, and diagonals for a win
        for i in range(self.size):
            if all(self.symbol_list[i * self.size + j] == sym for j in range(self.size)):
                return True
            if all(self.symbol_list[j * self.size + i] == sym for j in range(self.size)):
                return True

        if all(self.symbol_list[i * self.size + i] == sym for i in range(self.size)):
            return True

        if all(self.symbol_list[(self.size - 1 - i) * self.size + i] == sym for i in range(self.size)):
            return True

        return False

    def is_draw(self):
        if self.did_win(self.player_symbol):
            return False
        return all(s != " " for s in self.symbol_list)
