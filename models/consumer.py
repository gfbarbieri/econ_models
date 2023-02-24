import sympy as sp
from primitives.utility import Utility
from primitives.constraints import Budget_Constraint

class Consumer():
    """ A class representing a consumer. A consumer is a combination of a utility function and a
    budget constraint. Prices are exogenous, that is, the consumer is a price taker. In addition,
    the parameters of the utility function are exogenous and are created when the consumer is initiated.

    Attributes
    ----------

    Parameters
    ----------

    Examples
    --------
    """

    def __init__(self, num_goods=2):
        # Define the price and quantity variables for each good in the consumer's utility.
        # self.p = sp.symbols(f"p:{num_goods}", real=True)
        # self.q = sp.symbols(f"q:{num_goods}", real=True)

        # Define parameters of the consumer's utility funciton.
        # self.utility = Cobb_Douglas_Utility()

        # Define parameters of a consumers budget constraint.
        # self.m = m or sp.symbols('m', real=True)
        # self.px_1 = px_1 or sp.symbols('px_1', real=True)
        # self.px_2 = px_2 or sp.symbols('px_2', real=True)

        # Define a budget constraint which is each good multiplied by the price, substracted by
        # the income value. The result is a homogenous equation.
        # self.budget = p_x_1*x_1 + p_x_2*x_2 - m
        self.util = Utility()

    def get_demand(self):
        """ We have to calculate demand for each good.
        
        This should return demand functions given values of inputs. """
        pass

    def max_utility(self):
        """ We have to maximize utility given a budget constraint. """
        pass