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
         

class Queen(ChessPiece):
    def can_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return (start_row == end_row or start_col == end_col or row_diff == col_diff) and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)

    def __str__(self):


class Bishop(ChessPiece):
    def can_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return row_diff == col_diff and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)
    
    def __str__(self):


class Rook(ChessPiece):
    def can_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        return start_row == end_row or start_col == end_col and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)

    def __str__(self):


class Knight(ChessPiece):
    def can_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2) and (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)
     
    def __str__(self):


class Pawn(ChessPiece):
    def can_move(self, start, end, board):
        


    def __str__(self):