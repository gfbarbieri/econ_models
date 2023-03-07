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
from ..agent_functions.functions import Production
from ..agent_functions.functions import Input_Constraint
from ..agent_functions.functions import Cost_Structure

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
        """ Initialize the Monopolist class with cost and demand
        parameters.
        
        The cost and demand parameters can be set as inputs, or they
        can be set to default values using SymPy symbols.
    
        Parameters
        ----------
        """

        # Define the firms production function.

        # Define the firm's cost structure.
    
        # Define the market demand function faced by the firm.

    def get_input_demand(self):
        """ This function calculates the firms demand for an input
        factor.
    
        Parameters
        ----------
    
        Returns
        -------

        Examples
        --------
        """
        pass

    def get_total_cost(self):
        """ Calculate the total cost of production for a given quantity
        `q`.
        
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
        """ Calculate the total revenue of a firm for a quantity `q` at
        price `p`.
        
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
        """ Maximize profit given a firm's production function, cost
        structure and market demand.
        
        Parameters
        ----------

        Returns
        -------
        
        Examples
        --------
        """