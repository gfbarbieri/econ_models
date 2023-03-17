# econmodels.agents.consumer
# A class representing a standard consumer with a utility funciton and budget
# constraint.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
A class representing a consumer with a utility funciton and budget constraint.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp
from ..functional_forms.utility import Utility
from ..functional_forms.constraint import Input_Constraint

##########################################################################
## Representation of a Consumer
##########################################################################

class Consumer():
    """
    A class representing a consumer with a utility function and budget constraint.
    The class can find the optimal values of goods to purchase, given the budget
    constraint, using the Lagrangian method. The class can also query the demand
    for a quantity of a specific good.

    Attributes
    ----------
    num_goods : int
        The number of goods.

    utility : Utility
        The consumer's utility function.

    constraint : Input_Constraint
        The consumer's budget constraint.

    sym_str_dict : dict
        A dictionary of symbols to strings.

    opt_values_dict : dict
        A dictionary of optimal values of goods and lambda.

    Parameters
    ----------
    num_goods : int, optional
        The number of goods. The default is 2.

    Examples
    --------
    >>> consumer = Consumer()
    >>> consumer.maximize_utility()
    >>> consumer.opt_values_dict
    """

    def __init__(self, num_goods=2, util_form='cobb-douglas'):
        """
        Initializes the Consumer object by defining the number of goods, the consumer's utility function, and the budget constraint.

        Parameters
        ----------
        num_goods : int, optional
            The number of goods. The default is 2.
        
        func_form : string, optional
            The functional form of the utility function. The default is 'cobb-douglas'.

        Examples
        --------
        >>> consumer = Consumer()
        >>> consumer.maximize_utility()
        >>> consumer.opt_values_dict
        """

        # Define number of goods.
        self.num_goods = num_goods

        # Define the consumer's utility function.
        self.utility = Utility(
            num_inputs=num_goods,
            constant_name='C',
            func_form=util_form
        )

        # Define the consumer's budget constraint.
        self.constraint = Input_Constraint(
            num_inputs=num_goods,
            coeff_name='p_',
            exponent_values=None,
            constant_name='B'
        )

        # Define a dictionary of symbols to strings.
        self.sym_str_dict = {}

        for sym in (list(self.constraint.symboldict.values()) + list(self.utility.symboldict.values())):
            self.sym_str_dict[str(sym)] = sym
    
        # Define an empty optimal value dictionary.
        self.opt_values_dict = {}

    def maximize_utility(self):
        """
        Finds the optimal values of goods to purchase given the budget constraint,
        using the Lagrangian method.
                
        Parameters
        ----------
        None

        Returns
        -------
        None

        Examples
        --------
        >>> consumer = Consumer()
        >>> consumer.maximize_utility()
        >>> consumer.opt_values_dicts
        """

        # Solve for utility in terms of the other variables and values.
        util = sp.solve(
            self.utility.function,
            self.utility.symboldict['dependent']
        )[0]

        # Create a symbol for the Lagrangian lambda.
        l = sp.symbols('lambda')

        # Define the Lagrangian: `U(x_i) + \lambda(M - B(x_i))`.
        L = util + l * self.constraint.function

        # Find the FOC for each good.
        Lx = [
            sp.diff(L,self.utility.symboldict['input'][i])
            for i in range(self.num_goods)
        ]

        # Find the FOC for lambda.
        Ll = [sp.diff(L, l)]

        # Define the system of FOCs.
        Li = Lx + Ll

        # Define the variables we want to find optimal values for as a list. The
        # variables are each good (input) and the lambda.
        i = [
            self.utility.symboldict['input'][i]
            for i in range(self.num_goods)
        ] + [l]
    
        # Solve for the optimal values of goods and lambda and assign them to
        # a dictionary.
        self.opt_values_dict = sp.solve(Li, i, dict=True)[0]

    def get_demand(self, indx):
        """
        Queries the demand for a quantity from the consumer's dictionary of
        optimal values.

        Parameters
        ----------
        index : int
            The index of the good for which to query the demand.

        Returns
        -------
        demand : SymPy expression
            The demand for the good.

        Examples
        --------
        >> consumer = Consumer()
        >> consumer.maximize_utility()
        >> consumer.get_demand(index=0)
        """

        if not self.opt_values_dict:
            raise AttributeError("Run max_utility() first.")
        
        # Get the symbol for the indexed input.
        var = self.utility.symboldict['input']

        # Set demand equal to the optimal value of the indexed input as a
        # homogenous equation.
        demand = (
            self.opt_values_dict[var[indx]] -
            self.utility.symboldict['input'][indx]
        )
        
        return demand
    
    def get_elasticity(self, input_indx=0, var='p_', var_indx=0, point='symbol'):
        """
        Return the elasticity of quantity demanded for a variable.

        Parameters
        ----------
        input_indx : int, optional
            The index of the input for which to query the elasticity.
            The default is 0.

        var : str, optional
            The variable for which to query the elasticity. The default is 'p_'.

        var_indx : int, optional
            The index of the variable for which to query the elasticity.
            The default is 0.

        point : tuple, optional
            The point at which to evaluate the elasticity: (quantity, variable).
            The default is None.

        Returns
        -------
        float or Sympy symbol
            The elasticity of quantity with respect to the passed variable.

        Examples
        --------
        Calculate price elasticity of quantity demanded for good 0.
        >>> consumer = Consumer()
        >>> consumer.maximize_utility()
        >>> consumer.get_elasticity(input_indx=0, var='p_', var_indx=0)

        Calculate income elasticity of quantity demanded for good 0.
        >>> consumer = Consumer()
        >>> consumer.maximize_utility()
        >>> consumer.get_elasticity(input_indx=0, var='M', var_indx=0)

        Calculate price elasticity of quantity demanded for good 0 at a point
        where the price of good 0 is equal to quantity demanded.
        >>> consumer = Consumer()
        >>> consumer.maximize_utility()
        >>> consumer.get_elasticity(input_indx=0, var='p_', var_indx=0, point=(1,1))

        Calculate cross-price elasticity of quantity demanded for good 0 with
        respect to the price of good 1.
        >>> consumer = Consumer()
        >>> consumer.maximize_utility()
        >>> consumer.get_elasticity(input_indx=0, var='p_', var_indx=1)
        """

        # Check that the optimal values dictionary has been populated.
        if not self.opt_values_dict:
            raise AttributeError("Run max_utility() first.")
        
        # Check that the symbol is in the symbol dictionary for either the
        # constraint or the utility.
        if not var in self.sym_str_dict:
            raise AttributeError("Symbol not in symbol dictionary.")
        
        # Get the symbol for passed variable.
        sym = self.sym_str_dict[var]

        # Get demand for the indexed input.
        d = self.get_demand(indx=input_indx)
        d_x = sp.solve(d, self.utility.symboldict['input'][input_indx])[0]

        # Get the derivative of demand with respect to the variable.
        if type(sym) == sp.tensor.indexed.IndexedBase:
            f = sp.diff(d_x, sym[var_indx])
        elif type(sym) == sp.core.symbol.Symbol:
            f = sp.diff(d_x, sym)

        # If variable value or quantity value are None, set them equal to the
        # symbols.
        if point == 'symbol':
            point = (self.utility.symboldict['input'][input_indx], sym)

        # Calculate the elasticity.
        elas = f * point[1]/point[0]

        return elas