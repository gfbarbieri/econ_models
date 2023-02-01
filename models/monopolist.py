import sympy as sp

class Monopolist():
    def __init__(self, a=None, b=None, c=None):
        # Define the price and quantity variables.
        self.p, self.q = sp.symbols('p q', real=True)

        # Define demand funciton parameters.
        if a == None:
            self.a = sp.symbols('a', real=True)
        else:
            self.a = a

        if b == None:
            self.b = sp.symbols('b', real=True)
        else:
            self.b = b

        # Define cost function parameters.
        if c == None:
            self.c = sp.symbols('c', real=True)
        else:
            self.c = c

        # Define price elasticity parameters.
        self.p_0, self.q_0 = sp.symbols('p_0 q_0', real=True)

    def set_demand_params(self, a, b):
        # Redefine demand function parameters using user defined values.
        self.a = a
        self.b = b

    def set_cost_params(self, c):
        # Redefine cost function parameters using user defined values.
        self.c = c

    def get_demand(self, p=None, q=None, inverse=False):
        
        # If no p or q parameters are passed, used the initiated values.
        if p == None:
            p = self.p
        
        if q == None:
            q = self.q

        # Define market demand curve faced by the firm. For the purposes of the SymPy library,
        # market demand is defined as a homogenous equation.
        demand = self.a - self.b * q - p
        
        # If inverse demand, then solve for p(q). Else, solve for q(p).
        if inverse == True:
            demand = sp.solve(demand, p, simplify=True)
        else:
            demand = sp.solve(demand, q, simplify=True)

        return demand[0]

    def get_total_cost(self, c=None, q=None):

        # If no q or c parameters are passed, used the initiated values.
        if q == None:
            q = self.q
    
        if c == None:
            c = self.c
    
        # Define firm's total cost function.
        total_cost = c * q

        return total_cost

    def get_total_revenue(self, p=None, q=None):

        # If no p or q parameters are passed, used the initiated values.
        if p == None:
            p = self.p
        
        if q == None:
            q = self.q

        # Define firm's total revenue function.
        total_revenue = p*q
    
        return total_revenue

    def get_marginal_revenue(self, p=None):
        # If no p or q parameters are passed, used the initiated values.
        if p == None:
            p = self.p
    
        # Get total revenue, passing in the value of p.
        total_revenue = self.get_total_revenue(p=p)

        # Define firm's marginal revenue function as the first derivative
        # of the firm's total revenue function. The q passed into the diff
        # function must be a symbol.
        marginal_revenue = sp.diff(total_revenue, self.q)

        return marginal_revenue

    def get_marginal_cost(self, q=None):
        # If no p or q parameters are passed, used the initiated values.
        if q == None:
            q = self.q
    
        # Get total revenue, passing in the value of p.
        total_cost = self.get_total_cost(q=q)

        # Define firm's marginal cost function as the first derivative
        # of the firm's total cost function. The p passed into the diff
        # function must be a symbol.
        marginal_cost = sp.diff(total_cost, self.q)

        return marginal_cost

    def get_profit(self, p=None, q=None):
        
        # If no p or q parameters are passed, used the initiated values.
        if p == None:
            p = self.p
        
        if q == None:
            q = self.q

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