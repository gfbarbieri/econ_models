# econmodels.agent_functions.utility
# A class representing a utility function used by economic agents.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
A class representing a utility function used by economic agents.
"""

# Available utility functional forms.
_utils_ = ['additive','multiplicative','minimum','ces']

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
    num_inputs : int
        The number of goods/characteristics that are inputs into the consumer's utility function and
        budget constraint.

    Examples
    --------
    >>> utility = Utility()
    >>> utility.maximize_utility()
    >>> utility.opt_values_dict
    """

    def __init__(
        self,
        num_inputs=2, input_name='x',
        coeff_name='beta', coeff_values='symbols',
        exponent_name='alpha', exponent_values='symbols',
        dependent_name='U', dependent_value='symbols',
        constant_name='C', constant_value='symbols',
        func_form='multiplicative'
    ):
        # Check that functional form is supported.
        if func_form not in _utils_:
            raise Exception(f"Functional form is not supported: \"{func_form}\"")
        
        # Call parent class.
        super().__init__(
            num_inputs=num_inputs, input_name=input_name,
            coeff_name=coeff_name, coeff_values=coeff_values,
            exponent_name=exponent_name, exponent_values=exponent_values,
            dependent_name=dependent_name, dependent_value=dependent_value,
            constant_name=constant_name, constant_value=constant_value
        )

        # Set utility function using a dictionary dispatcher.
        func_form_dict = {
            'additive': self.additive,
            'multiplicative': self.multiplicative,
            'minimum': self.minimum_function,
            'ces': self.ces,
        }
        
        self.function, self.symbol_dict = func_form_dict[func_form]()

    def get_utility(self, input_values, constant):
        """
        This function calculates the total utility given a quantities of the
        goods (inputs variable). The function also allows for the substitution
        of constant values into the utility function. This is useful for
        calculating the utility of a specific bundle of goods.
        
        Parameters
        ----------
        input_values : tuple
            The values of the indexed inputs.

        constant : float
            The value of the constant.
        
        Returns
        -------
        float
            The utility value.

        Examples
        --------
        >>> utility = Utility()
        >>> utility.get_utility(input_values=[1,2], constant=0)
        2.0
        """

        # Solve for utility.
        utility_expr = sp.solve(self.function, self.symbol_dict['dependent'])

        # Substitute values for symbols in the utility funciton.
        utility_expr_sub = self.sub_symbols(
            func=utility_expr[0],
            symbol_values={
                self.symbol_dict['inputs']: input_values,
                self.symbol_dict['constant']: constant
            }
        )

        return utility_expr_sub

    def get_indifference(self, constant=None, dependent=None):
        """
        This function creates the indifferene curve for the indexed inputs. The
        indifference curve is simply the relationship between the indexed input
        values where the level of utility is held constant. Users can define
        the both the level of utility and any constant values over which the
        indexed inputs will vary.

        Parameters
        ----------
        constant : None or int
            The value of the constant inputs.

        dependent : None or int
            The value of the dependent variable.
        
        Returns
        -------
        SymPy expression.
            The indifference curve.

        Examples
        --------
        >>> utility = Utility()
        >>> utility.get_indifference(constant=0, dependent=1)
        1.0
        """

        # Substitute values for symbols in the utility funciton.
        indiff_expr = self.sub_symbols(
            func=self.function,
            symbol_values={
                self.symbol_dict['constant']: constant,
                self.symbol_dict['dependent']: dependent
            }
        )

        return indiff_expr

    def marginal_utility(self, indx=0, subs={}):
        """
        This function calculates the marginal utility for an input. The function
        also allows for the substitution of constant values into the utility
        function. This is useful for calculating the marginal utility of a
        specific bundle of goods.

        Parameters
        ----------
        indx : int
            The index of the input for which the marginal utility is calculated.

        subs : tuple
            A tuple of values to substitute in the utility function.
        
        Returns
        -------
        SymPy expression.
            The marginal utility for the indexed input.

        Examples
        --------
        >>> utility = Utility()
        >>> utility.marginal_utility(indx=0, subs=[['coefficient',1]])
        2.0
        """
    
        # Substitute values for symbols in the utility funciton.
        utility_expr = self.sub_symbols(
            func=self.function,
            symbol_values=subs
        )

        # Solve the utility function such that the dependent variable is on the
        # LHS and interms of all other variables.
        utility_expr = sp.solve(utility_expr, self.symbol_dict['dependent'])[0]

        # Take the first derivative with respect to the indexed good.
        mu_expr = sp.diff(utility_expr, self.symbol_dict['inputs'][indx])

        return mu_expr