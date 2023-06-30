class ChessPiece:
    def __init__(self, color):
        self.color = color
    
    def can_move(self, start, end, board):
        raise NotImplementedError("Subclasses must implement the 'can_move' method.")

    def __str__(self):
        raise NotImplementedError("Subclasses must implement the '__str__' method.")
    

class King(ChessPiece):
    def can_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return row_diff <= 1 and col_diff <= 1 and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)
    
    def __str__(self):
         return "♔" if self.color == "white" else "♚"


class Queen(ChessPiece):
    def can_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return (start_row == end_row or start_col == end_col or row_diff == col_diff) and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)

    def __str__(self):
        return "♕" if self.color == "white" else "♛"


class Bishop(ChessPiece):
    def can_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return row_diff == col_diff and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)
   
    def __str__(self):
        return "♗" if self.color == "white" else "♝"


class Rook(ChessPiece):
    def can_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        return start_row == end_row or start_col == end_col and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)

    def __str__(self):
        return "♖" if self.color == "white" else "♜"


class Knight(ChessPiece):
    def can_move(self, start, end, board):
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
        self.has_moved = False

    def can_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        direction = 1 if self.color == "white" else -1

        if start_col == end_col and start_row + direction == end_row and board[end_row][end_col] is None:
            return True

        if abs(start_col - end_col) == 1 and start_row + direction == end_row:
            target_piece = board[end_row][end_col]
            return target_piece and target_piece.color != self.color

        if not self.has_moved and start_col == end_col and start_row + 2 * direction == end_row and board[end_row][end_col] is None:
            return True

        return False

    def __str__(self):
         return "♙" if self.color == "white" else "♟"
    
class Chessboard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_pieces()
    
    def initialize_pieces(self):

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

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    piece.position = (row, col)