# econ_models.agents
# Classes for economic actors.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
Classes for economic actors, such as consumers and firms.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp
from .properties import Utility
from .properties import Production
from .properties import Budget_Constraint
from .properties import Cost_Structure

##########################################################################
## Representation of a Consumer
##########################################################################

class Consumer():
    """
    A consumer is a combination of a utility function and a budget constraint. Prices are exogenous,
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

        # Define number of goods.
        self.num_goods = num_goods

        # Define the consumer's utility function.
        self.utility = Utility(num_inputs=self.num_goods)

        # Define the consumer's budget constraint.
        self.budget_constraint = Budget_Constraint(num_inputs=self.num_goods)

        # Define an empty optimal value dictionary.
        self.opt_values_dict = {}

    def marginal_utility(self, index=1):
        util = sp.solve(self.utility.function, self.utility.symbol_dict['dependent'])[0]

        mu = sp.diff(util, self.utility.symbol_dict['input'][index])

        return mu

    def max_utility(self):
        """
        Max {X_i} Objective Function given Constraint where Objective
        Function is the utility function and Constraint is the budget.
        
        The Lagrangian method is used.
                
        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        """

        # Solve for utility in terms of the goods.
        util = sp.solve(self.utility.function, self.utility.symbol_dict['dependent'])[0]

        # Create a symbol for the Lagrangian lambda.
        l = sp.symbols('lambda')

        # Define the Lagrangian: `U(x_i) + \lambda(M - B(x_i))`.
        L = util + l * self.budget_constraint.function

        # Find the first order conditions for each good x_i and lambda.
        Lx = [sp.diff(L, self.utility.symbol_dict['input'][i]) for i in range(self.num_goods)]
        Ll = [sp.diff(L, l)]
        Li = Lx + Ll

        # Define the independent variables as a list.
        i = [self.utility.symbol_dict['input'][i] for i in range(self.num_goods)] + [l]
    
        # Solve for the optimal values of goods and lambda.
        self.opt_values_dict = sp.solve(Li, i, dict=True)[0]

    def get_demand(self, index):
        """
        Query the demand for a quantity from the consumer's dictionary of optimal values.
 
        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        """
        if not self.opt_values_dict:
            raise AttributeError("Run max_utility() first.")
        
        # Get the symbol for the indexed input.
        var = self.utility.symbol_dict['input']

        # Set demand equal to the optimal value of the indexed input as a homogenous
        # equation.
        demand = self.opt_values_dict[var[index]] - self.utility.symbol_dict['input'][index]
        
        return demand

##########################################################################
## Representation of a Firm
##########################################################################

class Firm():
    """ A class representing a firm.

    Attributes
    ----------

    Parameters
    ----------

    Examples
    --------
    """

    def __init__(self):
        """ Initialize the Monopolist class with cost and demand parameters.
        
        The cost and demand parameters can be set as inputs, or they can be set to default values using
        SymPy symbols.
    
        Parameters
        ----------
        """

        # Define the firms production function.

        # Define the firm's cost structure.
    
        # Define the market demand function faced by the firm.

    def get_input_demand(self):
        """ This function calculates the firms demand for an input factor.
    
        Parameters
        ----------
    
        Returns
        -------

        Examples
        --------
        """
        pass

    def get_total_cost(self):
        """ Calculate the total cost of production for a given quantity `q`.
        
        Parameters
        ----------

        Returns
        -------
        total_cost : int or float or Sympy symbol
            The total cost of producing the given quantity `q`.

        Examples
        --------
        """
        pass

    def get_total_revenue(self, p=None, q=None):
        """ Calculate the total revenue of a firm for a quantity `q` at price `p`.
        
        Parameters
        ----------

        Returns
        -------
        
        Examples
        --------
        """
        pass

    def get_marginal_revenue(self):
        """ Calculate the firm's marginal revenue.
        
        Parameters
        ----------

        Returns
        -------
        
        Examples
        --------
        """
        pass

    def get_marginal_cost(self, q=None):
        """ Calculate the firm's marginal cost.
        
        Parameters
        ----------

        Returns
        -------
        
        Examples
        --------
        """
        pass

    def get_profit(self, p=None, q=None):
        """ Calculate the firm's total profit.
        
        Parameters
        ----------

        Returns
        -------
        
        Examples
        --------
        """
        pass

    def profit_maximization(self):
        """ Maximize profit given a firm's production function, cost structure
        and market demand.
        
        Parameters
        ----------

        Returns
        -------
        
        Examples
        --------
        """