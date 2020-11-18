import unittest
from tic_tac_toe import TicTacToe

def board_maker(arr:list=[1,2,3,4,5,6,7,8,9]):
    output = "-------\n|{0}|{1}|{2}|"\
        "\n|{3}|{4}|{5}|"\
        "\n|{6}|{7}|{8}|"\
        "\n-------\n".format(*arr)
    return output
class test_board_print(unittest.TestCase):
    def test_inital(self):
        game = TicTacToe()
        numbers = [*range(1,11)]
        init_board = "-------\n|{0}|{1}|{2}|"\
            "\n|{3}|{4}|{5}|"\
            "\n|{6}|{7}|{8}|"\
            "\n-------\n".format(*numbers)
        self.assertEqual(game.get_board(),init_board)

    def test_normal(self):
        game = TicTacToe()
        game.play_turn(1)
        values = ['x',2,3,4,5,6,7,8,9]
        turn_one = board_maker(values)
        self.assertEqual(turn_one, game.get_board())
        
        game.play_turn(2)
        values = ['x','o',3,4,5,6,7,8,9]
        turn_two = board_maker(values)
        self.assertEqual(turn_two, game.get_board())
        
        game.play_turn(3)
        values = ['x','o','x',4,5,6,7,8,9]
        turn_three = board_maker(values)
        self.assertEqual(turn_three, game.get_board())

        game.play_turn(4)
        values = ['x','o','x','o',5,6,7,8,9]
        turn_four = board_maker(values)
        self.assertEqual(turn_four, game.get_board())

        game.play_turn(5)
        values = ['x','o','x','o','x',6,7,8,9]
        turn_five = board_maker(values)
        self.assertEqual(turn_five, game.get_board())

        game.play_turn(9)
        values = ['x','o','x','o','x',6,7,8,'o']
        turn_six = board_maker(values)
        self.assertEqual(turn_six, game.get_board())
        
        game.play_turn(6)
        values = ['x','o','x','o','x','x',7,8,'o']
        turn_seven = board_maker(values)
        self.assertEqual(turn_seven, game.get_board())

        game.play_turn(7)
        values = ['x','o','x','o','x','x','o',8,'o']
        turn_eight = board_maker(values)
        self.assertEqual(turn_eight, game.get_board())

        final_move = game.play_turn(8)
        values = ['x','o','x','o','x','x','o','x','o']
        turn_nine = board_maker(values)
        self.assertEqual(turn_nine, game.get_board())
        self.assertEqual(0,final_move)

if __name__ == "__main__":
    unittest.main(verbosity=True)