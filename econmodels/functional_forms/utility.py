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
        constant_name='C', constant_value='symbol',
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
            constant_name = constant_name, constant_value=constant_value
        )

        # Set utility function using a dictionary dispatcher.
        func_form_dict = {
            'ces': self.ces,
            'cobb-douglas': self.cobb_douglas,
            'complements': self.complements,
            'polynomial': self.polynomial_combination,
            # 'quasi-linear': self.quasi_linear,
            'substitutes': self.substitutes
        }
        
        self.function, self.symboldict = func_form_dict[func_form]()

    def get_utility(self, input_values, constant):
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
        
        Get the utility value given input values.
        
        Parameters
        ----------
        input_values : list
            A list of input values to substitute in the utility function.
            If an element in the list is None, the corresponding input value in the utility function is retained.
        
        Returns
        -------
        float
            The utility value.
        """

        # Solve for utility.
        utility_expr = sp.solve(self.function, self.symboldict['dependent'])

        # Substitute values for symbols in the utility funciton.
        utility_expr_sub = self.sub_values(
            func=utility_expr[0],
            symboldict=self.symboldict,
            values=[
                ['input', input_values],
                ['constant', constant]
            ]
        )

        return utility_expr_sub

    def get_indifference(self, lhs=0, constant=None, dependent=None):
        """
        This function creates the indifferene curve for the indexed inputs. The
        indifference curve is simply the relationship between the indexed input
        values where the level of utility is held constant. Users can define
        the both the level of utility and any constant values over which the
        indexed inputs will vary.

        Parameters
        ----------
        constant : None or int

        dependent : None or int
        
        Returns
        -------
        SymPy expression.
            The indifference curve.
        """

        # Substitute values for symbols in the utility funciton.
        indiff_expr = self.sub_values(
            func=self.function,
            symboldict=self.symboldict,
            values=[
                ['constant', constant],
                ['dependent', dependent]
            ]
        )

        return indiff_expr

    def marginal_utility(self, indx=0, subs=[]):
        """
        This function calculates the marginal utility for an input.

        Parameters
        ----------
        indx : int
            The index of the input for which the marginal utility is calculated.

        subs : list
            A list of values to substitute in the utility function.
        
        Returns
        -------
        SymPy expression.
            The marginal utility for the indexed input.
        """
    
        # Substitute values for symbols in the utility funciton.
        utility_expr = self.sub_values(
            func=self.function,
            symboldict=self.symboldict,
            values=subs
        )

        # Solve the utility function such that the dependent variable is on the
        # LHS and interms of all other variables.
        utility_expr = sp.solve(utility_expr, self.symboldict['dependent'])[0]

        # Take the first derivative with respect to the indexed good.
        mu_expr = sp.diff(utility_expr, self.symboldict['input'][indx])

        return mu_expr