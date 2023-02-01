import sympy as sp

class Consumer():
    def __init__(self, num_goods=2):
        # Define the price and quantity variables for each good in the consumer's utility.
        self.p = sp.symbols(f"p:{num_goods}", real=True)
        self.q = sp.symbols(f"q:{num_goods}", real=True)

        # Define parameters of the consumer's utility funciton.
        self.a, self.b = sp.symbols('a b', real=True)

        # Define parameters of the consumers budget constraint.
        self.m = sp.symbols('m', real=True)