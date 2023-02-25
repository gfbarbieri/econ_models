# econpy.primitives.production
# Primitive classes for market actors (firms, consumers).
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
Production function for economic agents.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp
from .generalized_function import generalized_function

##########################################################################
## Supported production functions.
##########################################################################

PRODUCTION_FUNCTIONAL_FORMS = {
    "cobb-douglas": cobb_douglas(),
    "perf_subs": linear_combination()
}

PRODUCTION_FUNCTION_NAMES = {
    "cobb-douglas": "Cobb-Douglas Production",
    "perf_subs": "Perfect Substitute Production"
}

##########################################################################
## Production Function
##########################################################################

class Production():
    """ A class representing a production function with variable inputs.

    Attributes
    ----------

    Parameters
    ----------

    Examples
    --------
    """

    def __init__(self):
        """
    
        Parameters
        ----------
        """
        pass

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