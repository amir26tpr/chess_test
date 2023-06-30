class ChessPiece:
    def __init__(self, color):
        self.color = color

    def can_move(self, start, end, board):
        # Logic to determine if the piece can move from 'start' to 'end'
        raise NotImplementedError("Subclasses must implement the 'can_move' method.")

    def __str__(self):
        # String representation of the chess piece
        raise NotImplementedError("Subclasses must implement the '__str__' method.")


class King(ChessPiece):
    def can_move(self, start, end, board):
        # Logic to determine if the king can move from 'start' to 'end'
        if start == end:
            return False
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return row_diff <= 1 and col_diff <= 1 and row_diff+col_diff >= 1 and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)

    def __str__(self):
        return "♔" if self.color == "white" else "♚"


class Queen(ChessPiece):
    def can_move(self, start, end, board):
        # Logic to determine if the queen can move from 'start' to 'end'
        if start == end:
            return False
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return (start_row == end_row or start_col == end_col or row_diff == col_diff) and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)

    def __str__(self):
        return "♕" if self.color == "white" else "♛"


class Bishop(ChessPiece):
    def can_move(self, start, end, board):
        # Logic to determine if the bishop can move from 'start' to 'end'
        if start == end:
            return False
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return row_diff == col_diff and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)

    def __str__(self):
        return "♗" if self.color == "white" else "♝"


class Rook(ChessPiece):
    def can_move(self, start, end, board):
        # Logic to determine if the rook can move from 'start' to 'end'
        if start == end:
            return False
        start_row, start_col = start
        end_row, end_col = end
        return start_row == end_row or start_col == end_col and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)

    def __str__(self):
        return "♖" if self.color == "white" else "♜"


class Knight(ChessPiece):
    def can_move(self, start, end, board):
        # Logic to determine if the knight can move from 'start' to 'end'
        if start == end:
            return False
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2) and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)

    def __str__(self):
        return "♘" if self.color == "white" else "♞"


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self._has_moved = False

    def can_move(self, start, end, board):
        # Logic to determine if the pawn can move from 'start' to 'end'
        if start == end:
            return False
        start_row, start_col = start
        end_row, end_col = end
        direction = 1 if self.color == "white" else -1

        if start_col == end_col and start_row + direction == end_row and board[end_row][end_col] is None:
            self._has_moved = True
            return True

        if abs(start_col - end_col) == 1 and start_row + direction == end_row:
            target_piece = board[end_row][end_col]
            if target_piece and target_piece.color != self.color:
                self._has_moved = True
                return True

        if not self._has_moved and start_col == end_col and start_row + 2 * direction == end_row and board[end_row][end_col] is None:
            self._has_moved = True
            return True

        return False

    def __str__(self):
        return "♙" if self.color == "white" else "♟"


class Chessboard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_pieces()

    def initialize_pieces(self):
        # Create and place the chess pieces on the board
        self.board[0][4] = King("white")
        self.board[7][4] = King("black")
        self.board[0][3] = Queen("white")
        self.board[7][3] = Queen("black")

        self.board[0][0] = Rook("white")
        self.board[0][7] = Rook("white")
        self.board[7][0] = Rook("black")
        self.board[7][7] = Rook("black")

        self.board[0][1] = Knight("white")
        self.board[0][6] = Knight("white")
        self.board[7][1] = Knight("black")
        self.board[7][6] = Knight("black")

        self.board[0][2] = Bishop("white")
        self.board[0][5] = Bishop("white")
        self.board[7][2] = Bishop("black")
        self.board[7][5] = Bishop("black")

        self.board[1] = [Pawn("white") for _ in range(8)]
        self.board[6] = [Pawn("black") for _ in range(8)]

        # Set the position of each piece
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    piece.position = (row, col)

    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece and piece.can_move(start, end, self.board):
            self.board[end[0]][end[1]] = piece
            self.board[start[0]][start[1]] = None
            piece.position = end
            return True
        else:
            return False

    def is_checkmate(self, color):
        # Check if the current player is in checkmate
        if not self.is_check(color):
            return False
        king_position = self.find_king(color)
        king_piece = self.find_king_piece(color)

        # Check if the king can move out of check
        for row in range(-1, 2):
            for col in range(-1, 2):
                new_row = king_position[0] + row
                new_col = king_position[1] + col
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if king_piece.can_move(king_position, (new_row, new_col), self.board):
                        new_check = False
                        for row_check in self.board:
                            for piece in row_check:
                                if piece and piece.color != color:
                                    if piece.can_move(piece.position, (new_row, new_col), self.board):
                                        new_check = True
                                        break
                            if new_check:
                                break
                        else:
                            return False
        return True

    def is_check(self, color):
        # Check if the current player is in check
        king_position = self.find_king(color)
        for row in self.board:
            for piece in row:
                if piece and piece.color != color:
                    if piece.can_move(piece.position, king_position, self.board):
                        return True
        return False

    def find_king(self, color):
        # Find the position of the king
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    return (row, col)

    def find_king_piece(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    return piece

    def __str__(self):
        # String representation of the chessboard
        board_str = ""
        for row in self.board:
            for piece in row:
                if piece:
                    board_str += str(piece) + " "
                else:
                    board_str += "- "
            board_str += "\n"
        return board_str


class GameController:
    def __init__(self):
        self.board = Chessboard()
        self.current_player = "white"

    def play(self):
        while True:
            print(self.board)
            print(f"It's {self.current_player}'s turn.")
            start = self.get_input("Enter the starting position (row, column): ")
            if self.board.board[start[0]][start[1]] and self.board.board[start[0]][start[1]].color != self.current_player:
                print("Invalid move. Try again.")
                continue
            end = self.get_input("Enter the ending position (row, column): ")

            if self.board.move_piece(start, end):
                if self.current_player == "white":
                    self.current_player = "black"
                else:
                    self.current_player = "white"

            else:
                print("Invalid move. Try again.")

            if self.board.is_checkmate(self.current_player):
                print(f"Checkmate! {self.current_player} wins.")
                break

    def get_input(self, message):
        while True:
            try:
                user_input = input(message)
                row, col = map(int, user_input.strip().split(","))
                if 0 <= row <= 7 and 0 <= col <= 7:
                    return row, col
                else:
                    print("Invalid input. Enter values between 0 and 7.")
            except ValueError:
                print("Invalid input. Enter values in the format 'row, col'.")


if __name__ == "__main__":
    game = GameController()
    game.play()