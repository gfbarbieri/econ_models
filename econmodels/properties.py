# econmodels.properties
# A class representing the primary properties of economic agents.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
A class representing the primary properties of economic agents.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp
from .functional_forms import generalized

##########################################################################
## Utility Function
##########################################################################

class Utility():
    """ A class representing a utility function.

    Attributes
    ----------

    Parameters
    ----------
    num_inputs : int
        The number of goods/characteristics that are inputs into the consumer's utility function and
        budget constraint.
    input_name : string
        The character used as the input symbol.
    coeff_values : tuple
        The linear coefficient values.
    coeff_name : string
        The character symbol used to represent coefficients.
    exponent_values : tuple
        The exponent values.
    exponent_name : string
        The character symbol used to represent exponents.
    dependent_value : tuple
        The values of the dependent variable, if a constant is wanted.
    dependent_name : string
        The character symbol used to represent the dependent variable.
    model : string
        The model for combining inputs, either `product` for product or `sum` for summation.

    Examples
    --------
    """

    def __init__(
        self, num_inputs=2, input_name='x',
        coeff_name='beta', coeff_values='symbol',
        exponent_name='alpha', exponent_values='symbol',
        dependent_name='U', dependent_value='symbol',
        model='product'
    ):
        """ Initialize the Utility class with parameters.
    
        Parameters
        ----------
        """

        # Define the utility function.
        self.function, self.symbol_dict = generalized(
            num_inputs=num_inputs, input_name=input_name,
            coeff_name=coeff_name, coeff_values=coeff_values,
            exponent_name=exponent_name, exponent_values=exponent_values,
            dependent_name=dependent_name, dependent_value=dependent_value,
            model=model
        )

    def set_params(self, **kwargs):
        """ This function sets parameters of the utility funciton.

        The user is expected to pass values for any free symbols, including values for
        goods, exponents, coefficients, or the dependent variable. The function should
        not return any values, but instead update the class's utility funtion. The idea
        is that this would be used to update parameters after the utility funciton has
        been created initially.

        Parameters
        ----------

        Returns
        -------
        None

        Examples
        --------
        """
        pass

    def total_utility(self):
        """ This function calculates the total utility given a quantities of the goods (inputs
        variable).

        The expectation is that this function will take as arguments values for the goods
        included in the utilty funciton. The function will substitute the variable for the
        passed values for the goods, solve for utility (dependent variable), and return the
        resulting utility as total utility.
        
        The user should be able to pass values for any specific indexed goods in the utility
        function, no values, or values for all indexed goods. The indexed goods for which no
        value was passed, the value should remain it's current value which may be a symbol.
    
        Parameters
        ----------

        Returns
        -------
        float or Sympy function
            The total utility.

        Examples
        --------
        """
        pass

    def get_indiff(self):
        """ This function calculates the indifferene curve for two indexed goods, holding
        utility and the quantity of any remaining index goods constant.

        The user is expected to tell the function which two indexed goods the indifference
        curve should compare, the remaining will be assumed constant, including the utility.
        The user may also pass a specific value of utility as the constant, as well as pass
        specific values of the remaining indexed goods.

        Parameters
        ----------

        Returns
        -------
        Sympy function
            The indifference curve for two indexed goods.

        Examples
        --------
        """
        pass

##########################################################################
## Production Function
##########################################################################

class Production():
    """ A class representing a production function with variable inputs.

    Attributes
    ----------

    Parameters
    ----------

    Examples
    --------
    """

    def __init__(self):
        """
    
        Parameters
        ----------
        """
        pass

    def get_production(self):
        """

        Parameters
        ----------
        
        Returns
        -------

        Examples
        --------
        """
        pass

    def get_isoquant(self):
        """

        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        """
        pass

##########################################################################
## Budget Constraint
##########################################################################

class Budget_Constraint():
    """ A class representing an actors budget constraint.

    Attributes
    ----------

    Parameters
    ----------
    num_inputs : int
        The number of goods/characteristics that are inputs into the consumer's utility function and
        budget constraint.
    input_name : string
        The character used as the input symbol.
    coeff_values : tuple
        The linear coefficient values.
    coeff_name : string
        The character symbol used to represent coefficients.
    exponent_values : string or tuple, default None
        The exponent values.
    exponent_name : string
        The character symbol used to represent exponents.
    dependent_value : tuple
        The values of the dependent variable, if a constant is wanted.
    dependent_name : string
        The character symbol used to represent the dependent variable.
    model : string
        The model for combining inputs, either `product` for product or `sum` for summation.

    Examples
    --------
    """

    def __init__(
        self, num_inputs=2, input_name='x',
        coeff_name='p', coeff_values='symbol',
        exponent_name='alpha', exponent_values=None,
        dependent_name='M', dependent_value='symbol',
        model='sum'
    ):
        """ Initialize the Utility class with parameters.
    
        Parameters
        ----------
        """

        # Define the utility function.
        self.function, self.symbol_dict = generalized(
            num_inputs=num_inputs, input_name=input_name,
            coeff_name=coeff_name, coeff_values=coeff_values,
            exponent_name=exponent_name, exponent_values=exponent_values,
            dependent_name=dependent_name, dependent_value=dependent_value,
            model=model
        )

##########################################################################
## Cost Structure
##########################################################################

class Cost_Structure():
    """ A class representing the cost structure of a firm.

    Attributes
    ----------

    Parameters
    ----------

    Examples
    --------
    """

    def __init__(self):
        """
    
        Parameters
        ----------
        """
        pass

##########################################################################
## Market Functions
##########################################################################

class Market():
    """
    A market is function defines a relationship between the unit price and quantity
    of a good. An increasing relationship can be used to represent supply function
    and a decreasing relationship can be used to represent a demand function.

    The market function can include the quantity of other goods, but only the price
    for one good should be defined in the market function.

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