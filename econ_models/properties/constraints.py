# econ_models.primitives.constraints
# A class representing constraints on economic actors.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
A class representing constraints on economic actors.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp
from .functional_forms import generalized

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