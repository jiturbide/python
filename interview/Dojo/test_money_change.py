from money_change import MoneyChange
import unittest

class TestMoneyChange(unittest.TestCase):

    def test_when_pocket_change_is_not_enough(self):
        """Unit test when the pocket change is not enough to pay the item"""
        pocket_change = [2,100,0,0]
        item_price = 14.11
        expected_result = False

        a = MoneyChange(pocket_change,item_price)
        actual_result = a.change_enough()
        self.assertEqual(expected_result,actual_result)


    def test_when_pocket_change_is_enough(self):
        """Unit test when the pocket change is enough to pay the item"""
        # pocket_change = [0,0,20,5]
        # item_price = 0.75
        pocket_change = [0,0,20,5]
        item_price = 1.06
        expected_result = True

        b = MoneyChange(pocket_change,item_price)
        actual_result = b.change_enough()
        self.assertEqual(expected_result,actual_result)


    def test_when_pocket_change_is_enough_another_amounts(self):
        """Unit test when the pocket change is enough to pay the item with another amounts"""
        pocket_change = [30,40,20,5]
        item_price = 12.55
        expected_result = True

        c = MoneyChange(pocket_change,item_price)
        actual_result = c.change_enough()
        self.assertEqual(expected_result,actual_result)


    def test_when_pocket_change_cant_be_calculated(self):
        """Unit test when the pocket change can't be calculated with 5 types of coins"""
        pocket_change = [30,40,20,5,10]
        item_price = 100
        expected_result = "The pocket change can't be calculated"

        d = MoneyChange(pocket_change,item_price)
        actual_result = d.change_enough()
        self.assertEqual(expected_result,actual_result)


if __name__ == '__main__':
    unittest.main()