# econmodels.agents.consumer
# Classes for economic agents.
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
    A consumer is a combination of a utility function and a budget
    constraint. Prices are exogenous, that is, the consumer is a price
    taker. In addition, the parameters of the utility function are
    exogenous and are created when the consumer is initiated.

    A utility represents the satisfaction of a consumer's wants, goals,
    or preferences. Inputs into the utility function are goods or
    characteristics of goods. The goods or characteristics are combined
    together in order to accomplish the consumer's goals. Taking prices
    as given, consumers use either budget and exogenous prices to
    purchase goods/characteristics in order to satisfify their
    goals/preferences as completely as possible (maximization).

    From utility maximization, demand for each good can calculated.
    Demand functions are the relationship between the unit price and
    rate of quantity demanded that maximizes utility, holding all else
    constant.

    Attributes
    ----------

    Parameters
    ----------

    Examples
    --------
    """

    def __init__(self, num_goods=2):
        """
        Define the consumers utility function and budget constraint.
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
        This function maximizes utility subject to a budget constraint. The
        Lagrangian method is used.
                
        Parameters
        ----------

        Returns
        -------

        Examples
        --------
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
        Query the demand for a quantity from the consumer's dictionary
        of optimal values.
 
        Parameters
        ----------

        Returns
        -------

        Examples
        --------
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