import sympy as sp

class Monopolist():
    """ A class representing a monopolist firm.

    Attributes
    ----------
    p : sympy.core.symbol.Symbol
        The price symbol.
    q : sympy.core.symbol.Symbol
        The quantity symbol.
    a : float or sympy.core.symbol.Symbol
        The demand function (linear) parameter symbol, represents the intercept.
    b : float or sympy.core.symbol.Symbol
        The demand function (linear) parameter symbol, represents the slope.
    c : float or sympy.core.symbol.Symbol
        The cost function parameter symbol, represents marginal cost.
    p_0 : sympy.core.symbol.Symbol
        The price elasticity parameter represents the input price..
    q_0 : sympy.core.symbol.Symbol
        The price elasticity parameter represents the input quantity.

    Parameters
    ----------
    a : float or sympy.core.symbol.Symbol, optional
        The demand function parameter symbol. Defaults to None.
    b : float or sympy.core.symbol.Symbol, optional
        The demand function parameter symbol. Defaults to None.
    c : float or sympy.core.symbol.Symbol, optional
        The cost function parameter symbol. Defaults to None.

    Examples
    --------
    """

    def __init__(self, a=None, b=None, c=None, d=1):
        """ Initialize the Monopolist class with cost and demand parameters.
        
        The cost and demand parameters can be set as inputs, or they can be set to default values using
        SymPy symbols.
    
        Parameters
        ----------
        a : float or Sympy symbol, optional
            The constant term in the demand function, by default None.
        b : float or Sympy symbol, optional
            The linear term in the demand function, by default None.
        c : float or Sympy symbol, optional
            The linear term in the cost function, by default None.
        d : float or sympy symbol, optional
            The polynomial term in the cost function, by default 1.
        """

        # Define the price and quantity variables.
        self.p, self.q = sp.symbols('p q', real=True)

        # Define demand funciton parameters.
        self.a = a or sp.symbols('a', real=True)
        self.b = b or sp.symbols('b', real=True)

        # Define cost function parameters.
        self.c = c or sp.symbols('c', real=True)
        self.d = d or sp.symbols('d', real=True)

        # Define price elasticity parameters.
        self.p_0, self.q_0 = sp.symbols('p_0 q_0', real=True)

    def set_demand_params(self, a, b):
        """ Set the parameters of the demand curve.

        Parameters
        ----------
        a : float
            The intercept of the demand curve.
        b : float
            The slope of the demand curve.

        Returns
        -------
        None

        Examples
        --------
        """
    
        # Redefine demand function parameters using user defined values.
        self.a = a
        self.b = b

    def set_cost_params(self, c, d=1):
        """ Set the cost parameters for the monopolist's cost function.
        
        Parameters
        ----------
        c : float or Sympy symbol, optional
            The coefficient for the linear term in the monopolist's cost function.
        d : float or Sympy symbol, optional
            The coefficient for the quadratic term in the monopolist's cost function.
    
        Returns
        -------
        None

        Examples
        --------
        """

        # Redefine cost function parameters using user defined values.
        self.c = c
        self.d = d

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
        float or Sympy symbol
            the demand for the product, calculated as either `b` - `a` * `p`
            or inverse demand `b / `a` - 1 / `a` * `q`.

        Examples
        --------
        """
    
        # If no p or q parameters are passed, used the initiated values.
        p = p or self.p
        q = q or self.q

        # Define market demand curve faced by the firm. For the purposes of the SymPy library,
        # market demand is defined as a homogenous equation.
        demand = self.a - self.b * q - p
        
        # If inverse demand, then solve for p(q). Else, solve for q(p).
        if inverse == True:
            demand = sp.solve(demand, p, simplify=True)
        else:
            demand = sp.solve(demand, q, simplify=True)

        return demand[0]

    def get_total_cost(self, c=None, d=None, q=None):
        """ Calculate the total cost of production for a given quantity `q`.
        
        Parameters
        ----------
        c : int or float or Sympy symbol, optional
            The coefficient for the linear term in the monopolist's cost function.
        d : int or float or Sympy symbol, optional
            The coefficient for the quadratic term in the monopolist's cost function.
        q : int or float or Sympy symbol, optional
            The quantity of goods to be produced.

        Returns
        -------
        total_cost : int or float or Sympy symbol
            The total cost of producing the given quantity `q`.

        Examples
        --------
        """
    
        # If no q, c, d parameters are passed, used the current values.
        q = q or self.q
        c = c or self.c
        d = d or self.d
    
        # Define firm's total cost function.
        total_cost = c * q**d

        return total_cost

    def get_total_revenue(self, p=None, q=None):
        """ Calculate the total revenue of a firm for a quantity `q` at price `p`.
        
        Parameters
        ----------
        p : int or float or Sympy symbol, optional
            The price of the product.
        q : int or float or Sympy symbol, optional
            The quantity of goods to be produced.

        Returns
        -------
        total_revenue : int or float or Sympy symbol
            The total revenue of producing the given quantity `q` at price `p`.
        
        Examples
        --------
        """
        # If no p or q parameters are passed, used the current values.
        p = p or self.p
        q = q or self.q

        # Define firm's total revenue function.
        total_revenue = p*q
    
        return total_revenue

    def get_marginal_revenue(self, p=None):
        # If no p or q parameters are passed, used the current values.
        p = p or self.p
    
        # Get total revenue, passing in the value of p.
        total_revenue = self.get_total_revenue(p=p)

        # Define firm's marginal revenue function as the first derivative
        # of the firm's total revenue function. The q passed into the diff
        # function must be a symbol.
        marginal_revenue = sp.diff(total_revenue, self.q)

        return marginal_revenue

    def get_marginal_cost(self, q=None):
        # If no p or q parameters are passed, used the initiated values.
        q = q or self.q
    
        # Get total revenue, passing in the value of p.
        total_cost = self.get_total_cost(q=q)

        # Define firm's marginal cost function as the first derivative
        # of the firm's total cost function. The p passed into the diff
        # function must be a symbol.
        marginal_cost = sp.diff(total_cost, self.q)

        return marginal_cost

    def get_profit(self, p=None, q=None):
        
        # If no p or q parameters are passed, used the initiated values.
        p = p or self.p
        q = q or self.q

        # Define firm's profit function. The cost parameters are not required
        # here, so the current values are used. Also, values of p and q are not
        # independently passed into the get_revenue or get_cost functions, instead
        # they passed into the profit fuction after the revenue and cost fuctions have
        # been combined.
        profit = self.get_total_revenue() - self.get_total_cost()

        return profit.subs([(self.p, p), (self.q, q)])

    def profit_maximization(self):
        # Alternative, set MR = MC directly instead of taking the FOC of the profit funciton.
        # mr = diff(tr, q)
        # mc = diff(tc, q)
        # q_eq = solve(mr - mc, q)

        # Rearrange the demand function interms of q: p(q).
        p = self.get_demand(inverse=True)

        # Substitute the inverse demand curve for P in the profit function.
        profit = self.get_profit(p=p)
    
        # Compute the first derivative of profit with respect to quantity.
        foc = sp.diff(profit, self.q)

        # Solve for profit maximizing quantity and price.
        q_star = sp.solve(foc, self.q)[0]
        p_star = p.subs(self.q, q_star)

        # Calculate profit at profit maximizing price and quantity.
        max_profit = self.get_profit(p=p_star, q=q_star)

        return p_star, q_star, max_profit

    def price_elasticity(self, p_0=None, q_0=None):
        if p_0 == None:
            p_0 = self.p_0
        
        if q_0 == None:
            q_0 = self.q_0
    
        # Rearrange demand function: q(p).
        q = self.get_demand(inverse=False)

        # Calculate price elasticity at given point.
        e_d = sp.diff(q, self.p)*(p_0 / q_0)

        return e_d

    ##########################################
    ## PLOTTING FUNCTIONS
    ##########################################

    def plot_total_cost(self):
        pass

    def plot_marginal_cost(self):
        pass
    
    def plot_total_revenue(self):
        pass
    
    def plot_marginal_revenue(self):
        pass

    def plot_demand(self):
        pass

    def plot_profit(self):
        pass