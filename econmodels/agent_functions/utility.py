# econmodels.agent_functions.utility
# A class representing the utility function used by economic agents.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
A class representing the utility function used by economic agents.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp
from .functional_forms import cobb_douglas
from .functional_forms import polynomial_combination
from .functional_forms import perfect_substitutes
from .functional_forms import perfect_complements
from .functional_forms import ces

##########################################################################
## Utility Function
##########################################################################

class BaseUtility():
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

    Examples
    --------
    """

    def __init__(self):
        """ Initialize the Utility class with parameters.
    
        Parameters
        ----------
        """

    def set_parameters(self):
        """ This function resets parameters of the utility funciton after
        it's initialization.

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

class Cobb_Douglas(BaseUtility):
    def __init__(
        self, num_inputs=2, input_name='L',
        coeff_name='beta', coeff_values='symbol',
        exponent_name='alpha', exponent_values='symbol',
        dependent_name='H', dependent_value='symbol',
        constant_name='J'
    ):
        """ Initialize the Utility class with parameters.
    
        Parameters
        ----------
        """

        # Define the utility function.
        self.function, self.symbol_dict = cobb_douglas(
            num_inputs=num_inputs, input_name=input_name,
            coeff_name=coeff_name, coeff_values=coeff_values,
            exponent_name=exponent_name, exponent_values=exponent_values,
            dependent_name=dependent_name, dependent_value=dependent_value,
            constant_name=constant_name
        )

class Polynomial(BaseUtility):
    def __init__(
        self, num_inputs=2, input_name='x',
        coeff_name='beta', coeff_values='symbol',
        exponent_name='alpha', exponent_values='symbol',
        dependent_name='U', dependent_value='symbol',
        constant_name='C'
    ):
        """ Initialize the Utility class with parameters.
    
        Parameters
        ----------
        """

        # Define the utility function.
        self.function, self.symbol_dict = polynomial_combination(
            num_inputs=num_inputs, input_name=input_name,
            coeff_name=coeff_name, coeff_values=coeff_values,
            exponent_name=exponent_name, exponent_values=exponent_values,
            dependent_name=dependent_name, dependent_value=dependent_value,
            constant_name=constant_name
        )

class Substitutes(BaseUtility):
    def __init__(
        self, num_inputs=2, input_name='x',
        coeff_name='beta', coeff_values='symbol',
        dependent_name='U', dependent_value='symbol',
        constant_name='C'
    ):
        """ Initialize the Utility class with parameters.
    
        Parameters
        ----------
        """

        # Define the utility function.
        self.function, self.symbol_dict = perfect_substitutes(
            num_inputs=num_inputs, input_name=input_name,
            coeff_name=coeff_name, coeff_values=coeff_values,
            dependent_name=dependent_name, dependent_value=dependent_value,
            constant_name=constant_name
        )

class Complements(BaseUtility):
    def __init__(
        self, num_inputs=2, input_name='x',
        coeff_name='beta', coeff_values='symbol',
        dependent_name='U', dependent_value='symbol',
    ):
        """ Initialize the Utility class with parameters.
    
        Parameters
        ----------
        """

        # Define the utility function.
        self.function, self.symbol_dict = perfect_complements(
            num_inputs=num_inputs, input_name=input_name,
            coeff_name=coeff_name, coeff_values=coeff_values,
            dependent_name=dependent_name, dependent_value=dependent_value,
        )

class CES(BaseUtility):
    def __init__(
        self, num_inputs=2, input_name='L',
        coeff_name='beta', coeff_values='symbol',
        exponent_name='alpha', exponent_values='symbol',
        dependent_name='H', dependent_value='symbol'
    ):
        """ Initialize the Utility class with parameters.
    
        Parameters
        ----------
        """

        # Define the utility function.
        self.function, self.symbol_dict = ces(
            num_inputs=num_inputs, input_name=input_name,
            coeff_name=coeff_name, coeff_values=coeff_values,
            exponent_name=exponent_name, exponent_values=exponent_values,
            dependent_name=dependent_name, dependent_value=dependent_value,
        )