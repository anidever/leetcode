class Board:
    def __init__(self, board_size=3):
        self.size = board_size
        self.grid = self._generate_board()
        self.total = 0

    def _generate_board(self):
        return [[None for _ in range(self.size)] for _ in range(self.size)]

    def set_position(self, row, col, value):
        if not self.is_in_bounds(row, col):
            raise ValueError
        if self.grid[row][col] is not None:
            raise ValueError
        if self.is_filled():
            raise ValueError
        else:
            self.grid[row][col] = value
            self.total += 1

    def is_filled(self):
        return self.total == self.size * self.size

    def reset_board(self):
        self.grid = self._generate_board()

    def is_in_bounds(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def print_board(self):
        for row in self.grid:
            print(row)

class Player:
    def __init__(self, marker):
        self.marker = marker


class Game:
    def __init__(self, board_size, winning_count=3):
        self.board_size = board_size
        self.board = Board(self.board_size)
        self.player_X = Player('X')
        self.player_O = Player('O')
        self.current_player = self.player_X
        self.winning_count = winning_count

    def search_row(self, row, col, direction):
        count = 0
        placed_marker = self.board.grid[row][col]

        if direction == "+":
            for idx in range(1, self.winning_count):
                new_x, new_y = (row, col + idx)
                print(new_x, new_y, self.board.is_in_bounds(new_x, new_y))
                if not self.board.is_in_bounds(new_x, new_y):
                    break
                if self.board.grid[new_x][new_y] == placed_marker:
                    count += 1
                else:
                    break
        elif direction == "-":
            for idx in range(1, self.winning_count):
                new_x, new_y = (row, col - idx)
                print(new_x, new_y, self.board.is_in_bounds(new_x, new_y))
                if not self.board.is_in_bounds(new_x, new_y):
                    break
                if self.board.grid[new_x][new_y] == placed_marker:
                    count += 1
                else:
                    break
        else:
            raise ValueError("Invalid direction")

        return count

    def search_col(self, row, col, direction):
        count = 0
        placed_marker = self.board.grid[row][col]

        if direction == "+":
            for idx in range(1, self.winning_count):
                new_x, new_y = (row + idx, col)
                if not self.board.is_in_bounds(new_x, new_y):
                    break
                if self.board.grid[new_x][new_y] == placed_marker:
                    count += 1
                else:
                    break
        elif direction == "-":
            for idx in range(1, self.winning_count):
                new_x, new_y = (row - idx, col)
                if not self.board.is_in_bounds(new_x, new_y):
                    break
                if self.board.grid[new_x][new_y] == placed_marker:
                    count += 1
                else:
                    break
        else:
            raise ValueError("Invalid direction")

        return count

    def search_diagonal(self, row, col, direction):
        count = 0
        placed_marker = self.board.grid[row][col]

        if direction == "+":
            for idx in range(1, self.winning_count):
                new_x, new_y = (row + idx, col + idx)
                if not self.board.is_in_bounds(new_x, new_y):
                    break
                elif self.board.grid[new_x][new_y] == placed_marker:
                    count += 1
                else:
                    break
        elif direction == "-":
            for idx in range(1, self.winning_count):
                new_x, new_y = (row - idx, col - idx)
                if not self.board.is_in_bounds(new_x, new_y):
                    break
                elif self.board.grid[new_x][new_y] == placed_marker:
                    count += 1
                else:
                    break
        else:
            raise ValueError("Invalid direction")

        return count

    def check_rows(self, row, col):
        count = 1
        count += self.search_row(row, col, "+")
        count += self.search_row(row, col, "-")
        return count

    def check_cols(self, row, col):
        count = 1
        count += self.search_col(row, col, "+")
        count += self.search_col(row, col, "-")
        return count

    def check_diagonal(self, row, col):
        count = 1
        count += self.search_diagonal(row, col, "+")
        count += self.search_diagonal(row, col, "-")
        return count

    def check_winner(self, row, col):
        if self.check_rows(row, col) >= self.winning_count:
            return True
        if self.check_cols(row, col) >= self.winning_count:
            return True
        if self.check_diagonal(row, col) >= self.winning_count:
            return True

        return False

    def play(self):
        while not self.board.is_filled():
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            try:
                self.board.set_position(row, col, self.current_player.marker)
                marker = "X" if self.current_player == self.player_X else "O"
                print(f'Placed {marker} at {row}, {col}')
                self.board.print_board()
            except ValueError:
                print("Invalid move, out of bounds or already filled. Try again.")
                continue

            if self.check_winner(row, col):
                print(f"Player {self.current_player.marker} wins!")
                break

            self.current_player = self.player_X if self.current_player == self.player_O else self.player_O
            print("Next player's turn")

        print("Game Over")
        self.board.reset_board()


game = Game(10, 4)
game.play()