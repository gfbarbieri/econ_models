# econmodels.agent_functions.utility_functions
# A class representing a utility function used by economic agents.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
A class representing a utility function used by economic agents.
"""

# Available utility functional forms.
_utils_ = ['cobb-douglas','substitutes','complements','ces','polynomial','quasi-linear']

##########################################################################
## Imports
##########################################################################

import sympy as sp
from .base import BaseForms

##########################################################################
## Utility Function
##########################################################################

class Utility(BaseForms):
    """ A class representing a utility function.

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
        String representing the functional form of the utility function.

    Attributes
    ----------

    Examples
    --------
    """

    def __init__(
        self,
        num_inputs=2, input_name='x',
        coeff_name='beta', coeff_values='symbol',
        exponent_name='alpha', exponent_values='symbol',
        dependent_name='U', dependent_value='symbol',
        constant_name='C',
        func_form='cobb-douglas'
    ):
        # Check that functional form is supported.
        if func_form not in _utils_:
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

    def get_utility(self):
        """
        This function calculates the total utility given a quantities of the goods (inputs
        variable).

        The expectation is that this function will take as arguments values for the goods
        included in the utilty funciton. The function will substitute the variable for the
        passed values for the goods, solve for utility (dependent variable), and return the
        resulting utility as total utility.
        
        The user should be able to pass values for any specific indexed goods in the utility
        function, no values, or values for all indexed goods. The indexed goods for which no
        value was passed, the value should remain it's current value which may be a symbol.
        """
        print("Get total utility function.")

    def get_indiff(self):
        """ This function calculates the indifferene curve for two indexed goods, holding
        utility and the quantity of any remaining index goods constant.

        The user is expected to tell the function which two indexed goods the indifference
        curve should compare, the remaining will be assumed constant, including the utility.
        The user may also pass a specific value of utility as the constant, as well as pass
        specific values of the remaining indexed goods.
        """
        print(
            "Return the indifference curve for an input in terms of the other \
            inputs: x_j = F(x_i where i =/= j)."
        )