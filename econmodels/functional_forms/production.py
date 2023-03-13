# econmodels.functional_forms.production
# A class constructing the functional forms of a production function.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
A class constructing the functional forms of a production function.
"""

# Available production functional forms.
_prods_ = ['cobb-douglas','substitutes','complements','ces','polynomial','quasi-linear']

##########################################################################
## Imports
##########################################################################

import sympy as sp
from .base import BaseForms

##########################################################################
## Production Function
##########################################################################

class Production(BaseForms):
    """
    A class representing a production function with variable inputs.
    
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

    func_form : string
        String representing the functional form of the production function.

    Attributes
    ----------

    Examples
    --------
    """

    def __init__(self):
        """
        Initialize the class.

        Parameters
        ----------

        """
        def __init__(
            self,
            num_inputs=2, input_name='x',
            coeff_name='beta', coeff_values='symbol',
            exponent_name='alpha', exponent_values='symbol',
            dependent_name='Y', dependent_value='symbol',
            constant_name='C',
            func_form='cobb-douglas'
        ):
            # Check that functional form is supported.
            if func_form not in _prods_:
                raise Exception(f"Functional form is not supported: \"{func_form}\"")
            
            # Call parent class.
            super().__init__(
                num_inputs = num_inputs, input_name = input_name,
                coeff_name = coeff_name, coeff_values = coeff_values,
                exponent_name = exponent_name, exponent_values = exponent_values,
                dependent_name = dependent_name, dependent_value = dependent_value,
                constant_name = constant_name
            )

            # Set utility function using a dictionary dispatcher.
            func_dict = {
                'cobb-douglas': self.cobb_douglas,
                'substitutes': self.substitutes,
                'complements': self.complements,
                'ces': self.ces,
                'quasi-linear': self.quasi_linear,
                'polynomial': self.polynomial_combination
            }
            
            self.function, self.symboldict = func_dict[func_form]()

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