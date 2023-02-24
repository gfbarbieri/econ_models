# econpy.primitives
# Classes for creating market demand and supply functions.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
Classes for creating market demand and supply functions.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp

##########################################################################
## Market Demand Functions
##########################################################################

class Demand():
    """
    The demand function represents a relationship between the unit price and a rate of
    quantity demanded. This function is limited to a demand function for a single good,
    assuming that any cross-elasticities are zero. Market demand functions for a single
    good are useful for quickly analyzing perfectly competitive or monopoly markets. The
    demand functions can be created without deriving it from consumer utility and budget
    constraints.

    Attributes
    ----------
    p : sympy.core.symbol.Symbol
        The price symbol.
    q : sympy.core.symbol.Symbol
        The quantity symbol.
    a : float or sympy.core.symbol.Symbol, optional, default: None
        The constant term in the demand function.
    b : float or sympy.core.symbol.Symbol, optional, default: None
        The linear term in the demand function.
    c : float or sympy.core.symbol.Symbol, optional, default: 1
        The polynomial term in the demand function.
    p_0 : sympy.core.symbol.Symbol
        The price elasticity parameter represents the input price.
    q_0 : sympy.core.symbol.Symbol
        The price elasticity parameter represents the input quantity.

    Parameters
    ----------
    a : float or sympy.core.symbol.Symbol, optional, default: None
        The constant term in the demand function.
    b : float or sympy.core.symbol.Symbol, optional, default: None
        The linear term in the demand function.
    c : float or sympy.core.symbol.Symbol, optional, default: 1
        The polynomial term in the demand function.

    Examples
    --------
    """

    def __init__(self, a=None, b=None, c=1):
        """ Initialize the Demand class.
        
        Parameters
        ----------
        a : float or sympy.core.symbol.Symbol, optional, default: None
            The constant term in the demand function.
        b : float or sympy.core.symbol.Symbol, optional, default: None
            The linear term in the demand function.
        c : float or sympy.core.symbol.Symbol, optional, default: 1
            The polynomial term in the demand function.
        """

        # Define the price and quantity variables.
        self.p, self.q = sp.symbols('p q', real=True)

        # Define demand funciton parameters.
        self.a = a or sp.symbols('a', real=True)
        self.b = b or sp.symbols('b', real=True)
        self.c = c or sp.symbols('c', real=True)

        # Define price elasticity parameters.
        self.p_0, self.q_0 = sp.symbols('p_0 q_0', real=True)

        # Define the demand function. For the purposes of the SymPy library,
        # market demand is defined as a homogenous equation.
        self.demand = self.a + self.b * self.q - self.p

    def set_demand_params(self, a=None, b=None, c=None):
        """ Set the parameters of the demand curve.

        Parameters
        ----------
        a : float or sympy.core.symbol.Symbol, optional, default: None
            The constant term in the demand function.
        b : float or sympy.core.symbol.Symbol, optional, default: None
            The linear term in the demand function.
        c : float or sympy.core.symbol.Symbol, optional, default: 1
            The polynomial term in the demand function.

        Returns
        -------
        None

        Examples
        --------
        """
    
        # Redefine demand function parameters using user defined values.
        self.a = a or self.a
        self.b = b or self.b
        self.c = c or self.c

    def get_price(self, q=None):
        """ This function calculates the price given a quantity demanded `q`.

        Parameters
        ----------
        q : float or Sympy symbol, optional, default: None
            The rate of quantity demanded.
    
        Returns
        -------
        float or Sympy symbol
            The unit price. If `q` is a symbol, it returns the inverse demand funciton
            p(q).

        Examples
        --------
        """

        q = q or self.q

        demand = self.demand.subs(self.q, q)
        price = sp.solve(demand, self.p, simplify=True)

        return price[0]

    def get_quantity(self, p=None):
        """ This function calculates the demand given a price `p` or `q`.

        Parameters
        ----------
        p : float or Sympy symbol, optional, default: None
            The unit price of quantity.
    
        Returns
        -------
        float or Sympy symbol
            The rate of quantity demanded for the product.

        Examples
        --------
        """
    
        # If no p or q parameters are passed, used the initiated values.
        p = p or self.p

        demand = self.demand.subs(self.p, p)
        quantity = sp.solve(demand, self.q, simplify=True)

        return quantity[0]

    def get_price_elasticity(self, p_0=None, q_0=None):
        """ This function calculates the price elasticity of quantity demand.

        Parameters
        ----------
        p_0 : float or Sympy symbol, optional, default: None
            The unit price of quantity.
        q_0 : float or Sympy symbol, optional, default: None
            The rate of quantity demanded.
    
        Returns
        -------
        float or Sympy symbol
            The price elasticity of quantity demanded at a specified price and quantity.

        Examples
        --------
        """

        if p_0 == None:
            p_0 = self.p_0
        
        if q_0 == None:
            q_0 = self.q_0
    
        # Rearrange demand function: q(p).
        q = self.get_quantity()

        # Calculate price elasticity at given point.
        e_d = sp.diff(q, self.p)*(p_0 / q_0)

        return e_d

class Supply():
    """
    The market supply function represents a relationship between the unit price and a rate
    of quantity supplied. This function is limited to a single good, assuming that any
    cross-elasticities are zero. Market supply functions are useful for quickly analyzing
    markets without deriving it from firm production functions and cost structures.

    Attributes
    ----------

    Parameters
    ----------

    Examples
    --------
    """

    def __init__(self, a=None, b=None, c=1):
        """ Initialize the Supply class.
        
        Parameters
        ----------
        """

        pass

    def set_demand_params(self, a=None, b=None, c=None):
        """ Set the parameters of the supply function.

        Parameters
        ----------

        Returns
        -------
        None

        Examples
        --------
        """

    def get_price(self, q=None):
        """ This function calculates the price given a quantity demanded `q`.

        Parameters
        ----------
        q : float or Sympy symbol, optional, default: None
            The rate of quantity demanded.
    
        Returns
        -------
        float or Sympy symbol
            The unit price. If `q` is a symbol, it returns the inverse demand funciton
            p(q).

        Examples
        --------
        """
        pass

    def get_quantity(self, p=None):
        """ This function calculates the demand given a price `p` or `q`.

        Parameters
        ----------
        p : float or Sympy symbol, optional, default: None
            The unit price of quantity.
    
        Returns
        -------
        float or Sympy symbol
            The rate of quantity demanded for the product.

        Examples
        --------
        """
        pass

    def get_price_elasticity(self, p_0=None, q_0=None):
        """ This function calculates the price elasticity of the rate
        of quantity supplied.

        Parameters
        ----------
        p_0 : float or Sympy symbol, optional, default: None
            The unit price of quantity.
        q_0 : float or Sympy symbol, optional, default: None
            The rate of quantity supplied.
    
        Returns
        -------
        float or Sympy symbol
            The price elasticity of the rate of quantity supplied at a specified
            price and quantity.

        Examples
        --------
        """
        pass