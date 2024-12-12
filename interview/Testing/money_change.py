class MoneyChange:

    def __init__(self,
                 pocket_change,
                 item_price):
        """Method Constructor
        Parameters:
            pocket_change (list): the list with the quantity of every type of coin in the pocket
            item_price (float): the price of the item to buy
        Returns:
            None

        """
        self.pocket_change = pocket_change
        self.item_price = item_price


    def _validate_pocket_change(self):
        """Method to validate if pocket change can be calculated with 4 type of coins

        Parameters:
            None

        Returns:
            result (bool): True if the pocket change can be define or False if not
        """
        result = True
        if len(self.pocket_change) != 4:
            result = False

        return result


    def change_enough(self):
        """Method to define if the item could be paid with the change in the pocket

        Parameters:
            None

        Returns:
            result (bool or str): True if the item can be paid or False if not or
                                  message if pocket change can't be calculated
        """
        result = False
        total_in_pocket = 0
        if self._validate_pocket_change():
            for i in range(4):
                if i == 0:
                    total_in_pocket += self.pocket_change[i] * 0.25
                if i == 1:
                    total_in_pocket += self.pocket_change[i] * 0.10
                if i == 2:
                    total_in_pocket += self.pocket_change[i] * 0.05
                if i == 3:
                    total_in_pocket += self.pocket_change[i] * 0.01
            if total_in_pocket >= self.item_price:
                result = True
        else:
            result = "The pocket change can't be calculated"

        return result