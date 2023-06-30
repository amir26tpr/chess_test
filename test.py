import unittest
from Chess import Chessboard, GameController, King, Queen, Rook, Bishop, Knight, Pawn

class ChessGameTest(unittest.TestCase):
    def setUp(self):
        self.game = GameController()

    def test_initial_board_setup(self):
        board = self.game.board.board
        self.assertIsInstance(board[0][4], King)
        self.assertIsInstance(board[7][4], King)
        self.assertIsInstance(board[0][3], Queen)
        self.assertIsInstance(board[7][3], Queen)

        self.assertIsInstance(board[0][0], Rook)
        self.assertIsInstance(board[0][7], Rook)
        self.assertIsInstance(board[7][0], Rook)
        self.assertIsInstance(board[7][7], Rook)

        self.assertIsInstance(board[0][1], Knight)
        self.assertIsInstance(board[0][6], Knight)
        self.assertIsInstance(board[7][1], Knight)
        self.assertIsInstance(board[7][6], Knight)

        self.assertIsInstance(board[0][2], Bishop)
        self.assertIsInstance(board[0][5], Bishop)
        self.assertIsInstance(board[7][2], Bishop)
        self.assertIsInstance(board[7][5], Bishop)

        self.assertIsInstance(board[1][0], Pawn)
        self.assertIsInstance(board[1][1], Pawn)
        self.assertIsInstance(board[1][2], Pawn)
        self.assertIsInstance(board[1][3], Pawn)
        self.assertIsInstance(board[1][4], Pawn)
        self.assertIsInstance(board[1][5], Pawn)
        self.assertIsInstance(board[1][6], Pawn)
        self.assertIsInstance(board[1][7], Pawn)

        self.assertIsInstance(board[6][0], Pawn)
        self.assertIsInstance(board[6][1], Pawn)
        self.assertIsInstance(board[6][2], Pawn)
        self.assertIsInstance(board[6][3], Pawn)
        self.assertIsInstance(board[6][4], Pawn)
        self.assertIsInstance(board[6][5], Pawn)
        self.assertIsInstance(board[6][6], Pawn)
        self.assertIsInstance(board[6][7], Pawn)