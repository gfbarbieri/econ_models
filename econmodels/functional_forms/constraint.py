# econmodels.functional_forms.constraint
# A class representing the functional form of a resource constraint.
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
from .base import BaseForms

##########################################################################
## Input Constraint
##########################################################################

class Input_Constraint(BaseForms):
    """
    A class representing the functional form of a resource constraint.

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

    Examples
    --------
    """

    def __init__(
        self,
        num_inputs=2, input_name='x',
        coeff_name='gamma', coeff_values='symbol',
        exponent_name='rho', exponent_values='symbol',
        dependent_name='M', dependent_value='symbol',
        constant_name='C', constant_value='symbol'
    ):
        """ Initialize the class.
    
        Parameters
        ----------
        """
        
        # Call parent class.
        super().__init__(
            num_inputs=num_inputs, input_name=input_name,
            coeff_name=coeff_name, coeff_values=coeff_values,
            exponent_name=exponent_name, exponent_values=exponent_values,
            dependent_name=dependent_name, dependent_value=dependent_value,
            constant_name=constant_name, constant_value=constant_value
        )

        self.function, self.symboldict = self.polynomial_combination()