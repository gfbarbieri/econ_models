import sympy as sp
from .primitives.utility import Utility
from .primitives.constraints import Budget_Constraint

class Consumer():
    """ A consumer is a combination of a utility function and a budget constraint. Prices are exogenous,
    that is, the consumer is a price taker. In addition, the parameters of the utility function are
    exogenous and are created when the consumer is initiated.

    A utility represents the satisfaction of a consumer's wants, goals, or preferences. Inputs into the utility
    function are goods or characteristics of goods. The goods or characteristics are combined together in order
    to accomplish the consumer's goals. Taking prices as given, consumers use either budget and exogenous prices
    to purchase goods/characteristics in order to satisfify their goals/preferences as completely as possible
    (maximization).

    From utility maximization, demand for each good can calculated. Demand functions are the relationship between
    the unit price and rate of quantity demanded that maximizes utility, holding all else constant.

    Attributes
    ----------

    Parameters
    ----------

    Examples
    --------
    """

    def __init__(self, num_goods=2):
        """
        Define the consumers utility function and budget constraint.
        """     

        # Define the consumer's utility function.
        self.utility = Utility(num_inputs=num_goods)

        # Define the consumer's budget constraint.
        self.budget_constraint = Budget_Constraint(num_inputs=num_goods)

    def max_utility(self):
        """ We have to maximize utility given a budget constraint.
        """
        pass

    def get_demand(self):
        """ We have to calculate demand for each good.
        
        This should return demand functions given values of inputs.
        """
        pass