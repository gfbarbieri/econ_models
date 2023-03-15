# econmodels.agents.consumer
# A class representing a standard consumer with a utility funciton and budget
# constraint.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
A class representing a standard consumer with a utility funciton and budget
constraint.
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

    Parameters
    ----------

    Examples
    --------
    """

    def __init__(self, num_goods=2):
        """
        Initializes the Consumer object by defining the number of goods, the consumer's utility function, and the budget constraint.

        Parameters
        ----------
        num_goods : int, optional
            The number of goods. The default is 2.

        Example
        -------
        >>> consumer = Consumer(num_goods=3)
        """

        # Define number of goods.
        self.num_goods = num_goods

        # Define the consumer's utility function.
        self.utility = Utility(
            num_inputs=num_goods,
            constant_name='C'
        )

        # Define the consumer's budget constraint.
        self.constraint = Input_Constraint(
            num_inputs=num_goods,
            coeff_name='p_',
            exponent_values=None,
            constant_name='B'
        )

        # Define an empty optimal value dictionary.
        self.opt_values_dict = {}

    def maximize_utility(self):
        """
        Finds the optimal values of goods to purchase given the budget constraint,
        using the Lagrangian method.
                
        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        >>> consumer = Consumer()
        >>> consumer.maximize_utility()
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

    def get_demand(self, index):
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
            self.opt_values_dict[var[index]] -
            self.utility.symboldict['input'][index]
        )
        
        return demand