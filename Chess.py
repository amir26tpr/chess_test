class ChessPiece:
    def __init__(self, color):
        self.color = color
        
    
    def can_move(self, start, end, board):
        # Logic to determine if the piece can move from 'start' to 'end'
        raise NotImplementedError("Subclasses must implement the 'can_move' method.")


    def __str__(self):
        # String representation of the chess piece
        raise NotImplementedError("Subclasses must implement the '__str__' method.")