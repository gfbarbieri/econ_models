import sympy as sp

class Monopolist():
    """ A class representing a monopolist firm. Monopolists are faced with a downward sloping
    market demand curve. Currently, the model only allows a monopolist to produce one good in only
    one market.

    Attributes
    ----------
    p : Symbol symbol
        The price symbol.
    q : Symbol symbol
        The quantity symbol.
    a : int or float or Sympy symbol, optional
        The constant term in the demand function. Default is Sympy symbol.
    b : int or float or Sympy symbol, optional
        The linear term in the demand function. Default is Sympy symbol.
    alpha : int or float or Sympy symbol, optional
        The demand function (linear) parameter symbol, represents the slope.
    c : int or float or Sympy symbol, optional
        The linear term in the cost function. Default is Sympy symbol.
    d : int or float or Sympy symbol, optional
        The constant term in the cost function. Default is 0.
    beta : int or float or Sympy symbol, optional
        The degree term in the cost function. Default is 1
    p_0 : Symbol symbol
        The price elasticity parameter represents the input price.
    q_0 : Symbol symbol
        The price elasticity parameter represents the input quantity.

    Parameters
    ----------
    a : int or float or Sympy symbol, optional
        The constant term in the demand function. Default is Sympy symbol.
    b : int or float or Sympy symbol, optional
        The linear term in the demand function. Default is Sympy symbol.
    alpha : int or float or Sympy symbol, optional
        The demand function (linear) parameter symbol, represents the slope.
    c : int or float or Sympy symbol, optional
        The linear term in the cost function. Default is Sympy symbol.
    d : int or float or Sympy symbol, optional
        The constant term in the cost function. Default is 0.
    beta : int or float or Sympy symbol, optional
        The degree term in the cost function. Default is 1

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

    def set_cost_params(self, c, d=0, beta=1):
        """ Set the cost parameters for the monopolist's cost function.
        
        Parameters
        ----------
        c : int or float or Sympy symbol, optional
            The linear term in the cost function. Default is Sympy symbol.
        d : int or float or Sympy symbol, optional
            The constant term in the cost function. Default is 0.
        beta : int or float or Sympy symbol, optional
            The degree term in the cost function. Default is 1
    
        Returns
        -------
        None

        Examples
        --------
        """

        # Redefine cost function parameters using user defined values.
        self.c = c
        self.d = d
        self.beta = beta

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

    def get_total_cost(self, q=None):
        """ Calculate the total cost of production for a given quantity `q`.
    
        Parameters
        ----------
        q : int or float or Sympy symbol, optional
            The quantity of goods to be produced.

        Returns
        -------
        total_cost : int or float or Sympy symbol
            The total cost of producing the given quantity `q`.

        Examples
        --------
        """
    
        # Use passed values or current values.
        q = q if q != None else self.q
    
        # Define firm's total cost function.
        total_cost = self.d + self.c * (q**self.beta)

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
        total_revenue : int or float or Sympy symbol or Sympy expression.
            The total revenue of producing the given quantity `q` at price `p`.
    
        Notes
        -----
        Total revenue is always the firms price times the firms quantity sold. If the firm faces a demand
        curve, then either p or q can be subsituted with the demand curve p(q) or q(p), respectively.

        Examples
        --------
        """
        
        # Use passed values or current values.
        p = p if p != None else self.p
        q = q if q != None else self.q

        # Define firm's total revenue function.
        total_revenue = p*q
    
        return total_revenue

    def get_marginal_revenue(self, p=None):
        """ Calculate the marginal revenue of a firm given a price.
        
        Parameters
        ----------
        p : int or float or Sympy symbol.
            The price of each unit of the product.

        Returns
        -------
        int or float or Sympy symbol.
            The marginal revenue of the product with respect to q.
        
        Notes
        -----
        The marginal revenue is calculated as the first derivative of the firm's total revenue function with
        respect to the quantity of output produced. This will always equal the sum of the price of the products
        sold by the firm.

        Examples
        --------
        """

        # Use passed values or current values.
        p = p if p != None else self.p
    
        # Get total revenue, passing in the value of p.
        total_revenue = self.get_total_revenue(p=p)

        # Define firm's marginal revenue function as the first derivative
        # of the firm's total revenue function. The q passed into the diff
        # function must be a symbol.
        marginal_revenue = sp.diff(total_revenue, self.q)

        return marginal_revenue

    def get_marginal_cost(self, q=None):
        """ Calculate the marginal revenue of a firm given a price.
        
        Parameters
        ----------
        q : int or float or Sympy symbol, optional
            Quantity of output to be produced, by default None.

        Returns
        -------
        int or float or Sympy expression.
            The marginal cost of production as a symbolic expression or value.
        
        Notes
        -----
        The marginal cost is calculated as the first derivative of the firm's total cost function with
        respect to the quantity of output produced.

        Examples
        --------
        """

        # Used passed values or current values.
        q = q if q != None else self.q

        # Get total revenue, passing in the value of p.
        total_cost = self.get_total_cost(q=q)

        # Define firm's marginal cost function as the first derivative
        # of the firm's total cost function. The p passed into the diff
        # function must be a symbol.
        marginal_cost = sp.diff(total_cost, self.q)

        return marginal_cost

    def get_profit(self, p=None, q=None):
        """ Calculate firm's profit.
        
        Parameters
        ----------
        p : int or float or Sympy symbol.
            The price of each unit of the product.
        q : int or float or Sympy symbol, optional
            Quantity of output to be produced, by default None.

        Returns
        -------
        int or float or Sympy expression.
            The profit as a symbolic expression or value.
        
        Notes
        -----
        The profit is calculated as the total revenue minus total cost.

        Examples
        --------
        """

        # Use passed values or current values if not None.
        p = p if p != None else self.p
        q = q if q != None else self.q

        # Define firm's profit function. Values of p and q are not independently passed
        # into the get_revenue or get_cost functions, but the profit function.
        profit = self.get_total_revenue() - self.get_total_cost()
        profit = profit.subs([(self.p, p), (self.q, q)])

        return profit

    def profit_maximization(self):
        """ Maximize the firm's profit function by finding the profit maximizing price and quantity.
        
        Parameters
        ----------
        p : int or float or Sympy symbol.
            The price of each unit of the product.
        q : int or float or Sympy symbol, optional
            Quantity of output to be produced, by default None.

        Returns
        -------
        int or float or Sympy expression.
            The profit as a symbolic expression or value.

        Notes
        -----
        The profit function is defined as total revenus total cost where price is substituted with the
        inverse demand function, p(q). Profit is maximized by
        1. Taking the first derivative of the profit function with respect to quantity.
        2. Setting the result to zero, and solving for the quantity. The result is the firms profit maximzing
        quantity.
        3. The quantity in the inverse demand curve is substitued with the profit maximizing quantity. The
        result is the firm's profit maximizing price.
        4. Price and quantity in the profit function are substituted with the profit maximizing price and
        quantity to calculate maximum profit.

        Examples
        --------
        """

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