# econpy.primitives
# Class for creating market demand and supply functions.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
Class for creating market demand and supply functions.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp
from generalized_function import generalized_function

##########################################################################
## Market Demand Functions
##########################################################################

class Market():
    """
    A market is function defines a relationship between the unit price and quantity
    of a good. An increasing relationship can be used to represent supply function
    and a decreasing relationship can be used to represent a demand function.

    The market function can include the quantity of other goods, but only the price
    for one good should be defined in the market function.

    Attributes
    ----------

    Parameters
    ----------

    Examples
    --------
    """

    def __init__(self):
        """ Initialize the market class.
        
        Parameters
        ----------
        """

        pass

    def set_params(self):
        """ Set the parameters of the function.

        Parameters
        ----------

        Returns
        -------
        None

        Examples
        --------
        """
        pass

    def get_price(self):
        """ This function calculates the price given a quantity `q`.

        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        """
        pass

    def get_quantity(self):
        """ This function calculates the demand given a price `p` or `q`.

        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        """
        pass

    def get_price_elasticity(self):
        """ This function calculates the price elasticity of quantity.

        Parameters
        ----------
        p_0 : float or Sympy symbol, optional, default: None
            The unit price of quantity.
        q_0 : float or Sympy symbol, optional, default: None
            The rate of quantity.
    
        Returns
        -------
        float or Sympy symbol
            The price elasticity of quantity at a specified price and quantity.

        Examples
        --------
        """
        pass