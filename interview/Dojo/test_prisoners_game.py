from prisoners_game import PrisonersGame
import unittest

class TestPrisonersGame(unittest.TestCase):

    def test_prisoners_dilemma_game_one(self):
        """Unit test to play prisoners game with game 1"""

        a = PrisonersGame()

        player_one_strategy_one = "cooperate"
        player_two_strategy_one = "defect"
        expected_result = (0,5)

        actual_result = a.prisoners_dilemma(player_one_strategy_one,player_two_strategy_one)
        self.assertEqual(expected_result,actual_result)

        player_one_strategy_two = "tit for tat"
        player_two_strategy_two = "cooperate"
        expected_result = (3,3)

        actual_result = a.prisoners_dilemma(player_one_strategy_two,player_two_strategy_two)
        self.assertEqual(expected_result,actual_result)

        player_one_strategy_three = "friedman"
        player_two_strategy_three = "defect"
        expected_result = (0,5)

        actual_result = a.prisoners_dilemma(player_one_strategy_three,player_two_strategy_three)
        self.assertEqual(expected_result,actual_result)

        player_one_strategy_four = "joss"
        player_two_strategy_four = "cooperate"
        expected_result = [(3,3),(5,0)]

        actual_result = a.prisoners_dilemma(player_one_strategy_four,player_two_strategy_four)
        #The order of actual_result and expected_result variables are changed in order to follow the parameters expected in method assertIn
        self.assertIn(actual_result,expected_result)

        player_one_strategy_five = "davis"
        player_two_strategy_five = "defect"
        expected_result = (0,5)

        actual_result = a.prisoners_dilemma(player_one_strategy_five,player_two_strategy_five)
        self.assertEqual(expected_result,actual_result)

        player_one_strategy_six = "downing"
        player_two_strategy_six = "defect"
        expected_result = (0,5)

        actual_result = a.prisoners_dilemma(player_one_strategy_six,player_two_strategy_six)
        self.assertEqual(expected_result,actual_result)


if __name__ == '__main__':
    unittest.main()