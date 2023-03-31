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
from ..utils.solvers import lagrangian
from ..utils.solvers import is_linear

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

    def __init__(self, num_goods=2, util_form='multiplicative'):
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
            constant_value=0
        )

        # Define a dictionary of symbols to strings.
        self.sym_str_dict = {}

        for sym in (list(self.constraint.symbol_dict.values()) + list(self.utility.symbol_dict.values())):
            self.sym_str_dict[str(sym)] = sym
    
        # Define an empty optimal value dictionary.
        self.opt_values_dict = {}

    def maximize_utility(self):
        """
        Finds the optimal values of goods to purchase given the budget constraint,
        using the Lagrangian method.

        Returns
        -------
        None

        Examples
        --------
        >>> consumer = Consumer()
        >>> consumer.maximize_utility()
        >>> consumer.opt_values_dicts
        """
    
        # If it is jointly linear, a unique solution may not exist using the
        # langrangian method.
        if is_linear(self.utility):
            raise NotImplementedError("Linear functions are not yet supported.")

        # Use langrangian method to find optimal values.
        self.opt_values_dict = lagrangian(
            objective=self.utility,
            constraint=self.constraint
        )

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
        >> consumer.get_demand(indx=0)
        """

        # If the optimal values dictionary is empty, raise an error. Optimal
        # values must be determined first.
        if not self.opt_values_dict:
            raise AttributeError("Run max_utility() first.")
        
        # Get the symbol for the indexed input.
        var = self.utility.symbol_dict['input']

        # Set demand equal to the optimal value of the indexed input as a
        # homogenous equation.
        demand = sp.Eq(
            self.utility.symbol_dict['input'][indx],
            self.opt_values_dict[self.utility.symbol_dict['input'][indx]]
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
        d_x = sp.solve(d, self.utility.symbol_dict['input'][input_indx])[0]

        # Get the derivative of demand with respect to the variable.
        if type(sym) == sp.tensor.indexed.IndexedBase:
            f = sp.diff(d_x, sym[var_indx])
        elif type(sym) == sp.core.symbol.Symbol:
            f = sp.diff(d_x, sym)

        # If variable value or quantity value are None, set them equal to the
        # symbols.
        if point == 'symbol':
            point = (self.utility.symbol_dict['input'][input_indx], sym)

        # Calculate the elasticity.
        elas = f * point[1]/point[0]

        return elas