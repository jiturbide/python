import random

class PrisonersGame:

    def __init__(self):
        """Method Constructor

        Parameters:
            None

        Returns:
            None

        """
        self.previous_player_one_strategy = []
        self.previous_player_two_strategy = []


    def _define_tit_for_tat_strategy(self,
                                     player,
                                     other_player_strategy):
        """Method to define tit for tat strategy based in the next rule:
            - Cooperate initially and then mirroring the opponent's previous move

        Parameters:
            player (str): the player this strategy applies
            other_player_strategy (str): the strategy othe player will apply

        Returns:
            result (str): the next strategy to apply by the player

        """
        result = ""
        if player == "one":
            previous_player_strategies = self.previous_player_one_strategy
        else:
            previous_player_strategies = self.previous_player_two_strategy

        if previous_player_strategies.count("cooperate") >= 1:
            result = other_player_strategy
        else:
            if random.randrange(1) == 0:
                result = "cooperate"
            else:
                result = "defect"

        return result


    def _define_joss_strategy(self):
        """Method to define jos strategy based in the next rule:
            - Mostly cooperate, but occasionally defect randomly

        Parameters:
            None

        Returns:
            result (str): the next strategy to apply by the player

        """
        result = "cooperate"
        if random.randrange(7) == 7 or random.randrange(7) == 5:
            result = "defect"

        return result


    def _define_davis_strategy(self,
                                 player):
        """Method to define davis strategy based in the next rule:
            - Cooperate initially and then defecting if the opponent defects twice in a row

        Parameters:
            player (str): the player this strategy applies

        Returns:
            result (str): the next strategy to apply by the player

        """
        result = "cooperate"
        condition = 1
        strategies_tracking = []
        if player == "one":
            previous_player_strategies = self.previous_player_two_strategy
        else:
            previous_player_strategies = self.previous_player_one_strategy

        index = 0
        defect_count = 1
        for strategy in previous_player_strategies:
            if condition <= 2:
                if strategy == "defect" and not defect_count <= 2:
                    strategies_tracking.append(index)
                    defect_count += 1
                    index += 1
                    condition += 1

        if strategies_tracking:
            defect_index_one = strategies_tracking[0]
            defect_index_two = strategies_tracking[1]

            if (defect_index_one + 1) == defect_index_two:
                result = "defect"

        return result


    def _define_downing_strategy(self,
                                   player):
        """Method to define downing strategy based in the next rule:
            - Cooperate initially and then defecting if the opponent defects more times than they cooperate

        Parameters:
            player (str): the player this strategy applies

        Returns:
            result (str): the next strategy to apply by the player

        """
        result = "cooperate"
        if player == "one":
            previous_player_strategies = self.previous_player_two_strategy
        else:
            previous_player_strategies = self.previous_player_one_strategy

        cooperate_count = previous_player_strategies.count("cooperate")
        defect_count = previous_player_strategies.count("defect")

        if cooperate_count < defect_count:
            result = "defect"

        return result


    def prisoners_dilemma(self,
                          player_one_strategy,
                          player_two_strategy):
        """Method to play the prisioner's dilemma game based on the next rules:
            - If both players cooperate, both receive a moderate payoff of 3
            - If one player defects while the other cooperates, the defector receives a higher payoff of 5 and
              the cooperatos receives a lower payoff of 0
            - If both players defects, both receive a lower payoff of 1

        Parameters:
            player_one_strategy (str): it takes the action of the player one
            player_two_strategy (str): it takes the action of the player two

        Returns:
            result (tuple): it will content the payoffs received for player_one and player_two

        """
        result =()
        if player_one_strategy == "cooperate" and player_two_strategy == "cooperate":
            self.previous_player_one_strategy.append("cooperate")
            self.previous_player_two_strategy.append("cooperate")
            result = (3,3)
        elif player_one_strategy == "cooperate" and player_two_strategy == "defect":
            self.previous_player_one_strategy.append("cooperate")
            self.previous_player_two_strategy.append("defect")
            result = (0,5)
        elif player_one_strategy == "defect" and player_two_strategy == "cooperate":
            self.previous_player_one_strategy.append("defect")
            self.previous_player_two_strategy.append("cooperate")
            result = (5,0)
        elif player_one_strategy == "defect" and player_two_strategy == "defect":
            self.previous_player_one_strategy.append("defect")
            self.previous_player_two_strategy.append("defect")
            result = (1,1)

        elif player_one_strategy == "tit for tat":
            result = self.prisoners_dilemma(self._define_tit_for_tat_strategy("one",player_two_strategy),player_two_strategy)
        elif player_two_strategy == "tit for tat":
            result = self.prisoners_dilemma(player_one_strategy,self._define_tit_for_tat_strategy("two",player_one_strategy))

        elif player_one_strategy == "friedman":
            result = self.prisoners_dilemma("cooperate",player_two_strategy)
        elif player_two_strategy == "friedman":
            result = self.prisoners_dilemma(player_one_strategy,"cooperate")

        elif player_one_strategy == "joss":
            result = self.prisoners_dilemma(self._define_joss_strategy(),player_two_strategy)
        elif player_two_strategy == "joss":
            result = self.prisoners_dilemma(player_one_strategy,self._define_joss_strategy())

        elif player_one_strategy == "davis":
            result = self.prisoners_dilemma(self._define_davis_strategy("one"),player_two_strategy)
        elif player_two_strategy == "davis":
            result = self.prisoners_dilemma(player_one_strategy,self._define_davis_strategy("two"))

        elif player_one_strategy == "downing":
            result = self.prisoners_dilemma(self._define_davis_strategy("one"),player_two_strategy)
        elif player_two_strategy == "downing":
            result = self.prisoners_dilemma(player_one_strategy,self._define_davis_strategy("two"))

        return result