import sympy as sp

class Demand():
    """ A class representing demand curves. This model can be used to define individual consumer demand curves
    market demand curves used by firms.

    Attributes
    ----------
    p : Symbol symbol
        The price symbol.
    q : Symbol symbol
        The quantity symbol.
    a : int or float or Symbol symbol
        The demand function (linear) parameter symbol, represents the intercept.
    b : int or float or Symbol symbol
        The demand function (linear) parameter symbol, represents the slope.
    p_0 : Symbol symbol
        The price elasticity parameter represents the input price.
    q_0 : Symbol symbol
        The price elasticity parameter represents the input quantity.

    Parameters
    ----------
    a : float or Symbol symbol, optional
        The demand function parameter symbol. Defaults to None.
    b : float or Symbol symbol, optional
        The demand function parameter symbol. Defaults to None.
    c : float or Symbol symbol, optional
        The cost function parameter symbol. Defaults to None.

    Examples
    --------
    """

    def __init__(self, a=None, b=None, alpha=1, c=None, d=0, beta=1):
        """ Initialize the Monopolist class with cost and demand parameters.
    
        The cost and demand parameters can be set as inputs, or they can be set to default values using
        SymPy symbols.
    
        Parameters
        ----------
        a : int or float or Sympy symbol, optional
            The constant term in the demand function. Default is Sympy symbol.
        b : int or float or Sympy symbol, optional
            The linear term in the demand function. Default is Sympy symbol.
        alpha : int or float or Sympy symbol, optional
            The degree term in the demand function. Default is 1.
        c : int or float or Sympy symbol, optional
            The linear term in the cost function. Default is Sympy symbol.
        d : int or float or Sympy symbol, optional
            The constant term in the cost function. Default is 0.
        beta : int or float or Sympy symbol, optional
            The degree term in the cost function. Default is 1
    
        Examples
        --------
        """

        # Define the price and quantity variables.
        self.p, self.q = sp.symbols('p q', real=True)

        # Define demand funciton parameters.
        self.a = a if a != None else sp.symbols('a', real=True)
        self.b = b if b != None else sp.symbols('b', real=True)
        self.alpha = alpha if alpha != None else sp.symbols('alpha', real=True)

        # Define cost function parameters.
        self.c = c if c != None else sp.symbols('c', real=True)
        self.d = d if d != None else sp.symbols('d', real=True)
        self.beta = beta if beta != None else sp.symbols('beta', real=True)

        # Define price elasticity parameters.
        self.p_0, self.q_0 = sp.symbols('p_0 q_0', real=True)

    def set_demand_params(self, a, b, alpha=1):
        """ Set the parameters of the demand curve.

        Parameters
        ----------
        a : int or float or Sympy symbol, optional
            The constant term in the demand function. Default is Sympy symbol.
        b : int or float or Sympy symbol, optional
            The linear term in the demand function. Default is Sympy symbol.
        alpha : int or float or Sympy symbol, optional
            The degree term in the demand function. Default is 1.

        Returns
        -------
        None

        Examples
        --------
        """
    
        # Redefine demand function parameters using user defined values.
        self.a = a
        self.b = b
        self.alpha = alpha

    def get_demand(self, p=None, q=None, inverse=False):
        """ This function calculates the demand for the monopolist's product given a price `p` or `q`.
        
        Parameters
        ----------
        p : float or Sympy symbol, optional
            The price of the product.
        q : float or Sympy symbol, optional
            The quantity of the product.
        inverse: bool, default=False
            A boolean whether to return the inverse demand function p(q) or q(p).
    
        Returns
        -------
        int or float or Sympy expression
            the demand for the product, calculated as either $q(p) = b - a * p$
            or inverse demand $p(q) = b /a - 1/a * q$.

        Examples
        --------
        """

        # Used passed values or current values.
        p = p if p != None else self.p
        q = q if q != None else self.q

        # Define market demand curve faced by the firm. For the purposes of the SymPy library,
        # market demand is defined as a homogenous equation.
        demand = self.a - (self.b**self.alpha) * q - p
        
        # If inverse demand, then solve for p(q). Else, solve for q(p).
        if inverse == True:
            demand = sp.solve(demand, p, simplify=True)
        else:
            demand = sp.solve(demand, q, simplify=True)

        return demand[0]

    def price_elasticity(self, p_0=None, q_0=None):
        """ Calculate the firm's price elasticity of quantity demanded (price elasticity of demand).
        
        Parameters
        ----------
        p_0 : int or float or Sympy symbol.
            The price point along the demand curve to assess elasticity.
        q_0 : int or float or Sympy symbol, optional
            The quantity point along the demand curve to assess elasticity.

        Returns
        -------
        int or float or Sympy expression.
            The price elasticity of demand as a symbolic expression or value.

        Notes
        -----
        Price elasticity of demand is defined as the ratio of the percent change in quantity and the percent
        change in price. Using calculus, this is defined as the first derivative of demand q(p) in terms of price
        multiplied by a price and quantity (p_0, q_0) along the demand curve. The result is the price elasticity
        of demand at the price, quantity point (p_0, q_0).

        Examples
        --------
        """

        # Use passed values or current values.
        p_0 = p_0 if p_0 != None else self.p_0
        q_0 = q_0 if q_0 != None else self.q_0
    
        # Rearrange demand function: q(p).
        q = self.get_demand(inverse=False)

        # Calculate price elasticity at given point.
        e_d = sp.diff(q, self.p)*(p_0 / q_0)

        return e_d