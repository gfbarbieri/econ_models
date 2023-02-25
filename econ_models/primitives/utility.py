# econpy.primitives.utility
# Primitive classes for market actors (firms, consumers).
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

##########################################################################
## Imports
##########################################################################

import sympy as sp
from .generalized_function import generalized_function

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
        self.function, self.symbol_dict = generalized_function(
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