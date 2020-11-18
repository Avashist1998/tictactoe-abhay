import unittest
from tic_tac_toe.TicTacToe import TicTacToe

def board_starter(spot:int):
    game = TicTacToe()
    status = game.play_turn(spot)
    return game, status

class test_play_turn(unittest.TestCase):
    def test_perfect_case(self):
        game, status = board_starter(1)
        board = '-------\n|x|2|3|\n|4|5|6|\n|7|8|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        game, status = board_starter(2)
        board = '-------\n|1|x|3|\n|4|5|6|\n|7|8|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        game, status = board_starter(3)
        board = '-------\n|1|2|x|\n|4|5|6|\n|7|8|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        game, status = board_starter(4)
        board = '-------\n|1|2|3|\n|x|5|6|\n|7|8|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        game, status = board_starter(5)
        board = '-------\n|1|2|3|\n|4|x|6|\n|7|8|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        game, status = board_starter(6)
        board = '-------\n|1|2|3|\n|4|5|x|\n|7|8|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        game, status = board_starter(7)
        board = '-------\n|1|2|3|\n|4|5|6|\n|x|8|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        game, status = board_starter(8)
        board = '-------\n|1|2|3|\n|4|5|6|\n|7|x|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        game, status = board_starter(9)
        board = '-------\n|1|2|3|\n|4|5|6|\n|7|8|x|\n-------\n'
        self.assertEqual(game.get_board(), board)
    
    def test_over_lap_case(self):
        game, status = board_starter(1)
        board = '-------\n|x|2|3|\n|4|5|6|\n|7|8|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        status = game.play_turn(1)
        self.assertEqual(-1, status)
        self.assertEqual(board, game.get_board())
        game, status = board_starter(2)
        board = '-------\n|1|x|3|\n|4|5|6|\n|7|8|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        status = game.play_turn(2)
        self.assertEqual(-1, status)
        self.assertEqual(board, game.get_board())
        game, status = board_starter(3)
        board = '-------\n|1|2|x|\n|4|5|6|\n|7|8|9|\n-------\n'
        self.assertEqual(game.get_board(), board)
        status = game.play_turn(3)
        self.assertEqual(-1, status)
        self.assertEqual(board, game.get_board())

    def test_invalid_case(self):
        game = TicTacToe()
        status = game.play_turn(-1)
        self.assertEqual(-1,status)
        game = TicTacToe()
        status = game.play_turn()
        self.assertEqual(0,status)
        status = game.play_turn(1)
        self.assertEqual(-1,status)

if __name__ == "__main__":
    unittest.main()