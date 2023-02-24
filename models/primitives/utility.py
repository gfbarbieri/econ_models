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
from .functional_forms import cobb_douglas
from .functional_forms import linear_combination

##########################################################################
## Supported utiliy functions.
##########################################################################

UTILITY_FUNCTIONAL_FORMS = {
    "cobb-douglas": cobb_douglas(),
    "perf_subs": linear_combination()
}

UTILITY_FUNCTION_NAMES = {
    "cobb-douglas": "Cobb-Douglas Utility",
    "perf_subs": "Perfect Substitute Utility"
}

##########################################################################
## Utility Functions
##########################################################################

class Utility():
    """ A class representing a utility function for two goods only. The utility function
    takes the form of a Cobb-Douglas utility function: `U(x,y)=\prod a_i*x_i^b_i`.

    Attributes
    ----------
    U   : float or sympy.core.symbol.Symbol
        The total utility.
    x_i : float or sympy.core.symbol.Symbol
        The quantity of good_i.
    a_i : float or sympy.core.symbol.Symbol, optional, default: 1
        The linear term augmenting good_i.
    b_i : float or sympy.core.symbol.Symbol, optional, default: 1
        The polynomial term of good_i.

    Parameters
    ----------
    num_goods : int, required, default: 2
        The number of goods/characteristics in the utility function.
    params : list, optional, default: [(1,1),(1,1)]
        A list of tuples representing the liner and polynomial terms of each good, respectively.
        That is, the first element in the params list is a tuple of the linear and polynomial term
        of the first good. If None is passed, then all parameters are symbols.

    Examples
    --------
    """

    def __init__(self, num_goods=2, params=[(1,1),(1,1)]):
        """ Initialize the Utility class with parameters.

        The utility parameters can be set as inputs, or they can be set to default
        values of SymPy symbols.
    
        Parameters
        ----------
        num_goods : int, required, default: 2
            The number of goods/characteristics in the utility function.
        params : list, optional, default: [(1,1),(1,1)]
            A list of tuples representing the liner and polynomial terms of each good, respectively.
            That is, the first element in the params list is a tuple of the linear and polynomial term
            of the first good. If None is passed, then all parameters are symbols.
        """

        # Define total utility.
        self.U = sp.symbols('U', real=True)

        # Define the goods in the utility.
        self.x = sp.symbols(f"x:{num_goods}", real=True, positive=True)

        # Define the utility function's parameters.
        if params == None:
            self.a = sp.symbols(f"a:{num_goods}", real=True, positive=True)
            self.b = sp.symbols(f"b:{num_goods}", real=True, positive=True)
        else:
            self.a = list(zip(*params))[0]
            self.b = list(zip(*params))[1]

        # Define the utility function as a homogenous equation, limited to two goods.
        self.utility = (self.a[0] * self.x[0]**self.b[0]) * (self.a[1] * self.x[1]**self.b[1]) - self.U

    def set_util_params(self, params=[(1,1),(1,1)]):
        """ Set the parameters of the utility functon.

        Parameters
        ----------
        params : list, optional, default: [(1,1),(1,1)]
            A list of tuples representing the liner and polynomial terms of each good, respectively.
            That is, the first element in the params list is a tuple of the linear and polynomial term
            of the first good. If None is passed, then all parameters are symbols.

        Returns
        -------
        None

        Examples
        --------
        """
    
        # Define the utility function's parameters.
        self.a = list(zip(*params))[0]
        self.b = list(zip(*params))[1]

    def get_total_util(self, x=[]):
        """ This function calculates the total utility given a quantities of
        goods x_i.

        Parameters
        ----------
        x : list, required, default: []
            The quantity values of each good x_i. To only set the quantity of
            a specific number of goods, include the values in the list and
            include None as the values for the remainder of the goods in the
            list. None values will be replaced with current values.
        
        Returns
        -------
        float or Sympy function.
            The total utility.

        Examples
        --------
        """

        # If no values for the goods are passed, then the utility will be calculated
        # with current values. If some goods are passed values, but others are not, then
        # the passed values will replace current values of the goods and the remaining goods
        # will keep their current values.
        if len(x) == 0:
            x = self.x
        else:
            x = [self.x[i] if g is None else g for i, g in enumerate(x)]

        # Create list of substitutions and subtitute variables in the utility function
        # with the list of substitutions.
        subs = [(g, x[i]) for i, g in enumerate(self.x)]
        utility = self.utility.subs(subs)

        # Solve for utility in terms of the goods x_i.
        utility = sp.solve(utility, self.U, simplify=True)

        return utility[0]

    def get_indiff(self, lhs=0, util=10):
        """ This function calculates the indifferene curve using a constant utility value.
        The indifference curve represents the combinations of both goods that result in the
        specified value of utility.

        Parameters
        ----------
        lhs : string, required
            Which good to isolate. The result will be an indifference function in terms
            the remaining goods. E.g., lhs = x_1 -> x_1(x_i) where i != 1.
        util : float, required
            The total level of utility, held constant to create an indifference curve.
    
        Returns
        -------
        Sympy symbol
            The utility function with a constant substituted for total utility.

        Examples
        --------
        """

        # Substitute the constant value for utility.
        utility = self.utility.subs(self.U, util)

        # Solve for the LHS variable.
        indiff = sp.solve(utility, self.x[lhs], simplify=True)

        return indiff[0]