# econmodels.agent_functions.functional_forms
# Common funcitonal forms for functions used in economoics.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
Func that represent common funcitonal forms for utility, production, and
constraint functions in economoics.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp

##########################################################################
## Functional Forms Class
##########################################################################

class FunctionalForms():
    """
    The FunctionalForm class returns common functional forms used in economics
    to represent utility and production functions. Each function form follows
    a similar pattern: define the symbols used, create the index range for
    the inputs, define how form the inputs will take, define the functional form
    with multiple inputs, substitute symbols for any values passed into the
    FunctionalForms class, return both the final functional form and the 
    symboldict.

    Parameters
    ----------
    num_inputs : int, optional
        The number of input variables for the polynomial equation. Default is 2.

    input_name : str, optional
        The base name for the input variables. Default is 'k'.

    coeff_name : str, optional
        The base name for the coefficient variables. Default is 'beta'.

    coeff_values : {None, 'symbol', tuple}, optional
        The values to substitute for the coefficient variables. If 'symbol',
        the variables are left as symbols. If None, they are substituted
        with a tuple of 1s. If a tuple, they are substituted with the
        corresponding values. Default is 'symbol'.

    exponent_name : str, optional
        The base name for the exponent variables. Default is 'alpha'.

    exponent_values : {None, 'symbol', tuple}, optional
        The values to substitute for the exponent variables. If 'symbol',
        the variables are left as symbols. If None, they are substituted
        with a tuple of 1s. If a tuple, they are substituted with the
        corresponding values. Default is 'symbol'.

    dependent_name : str, optional
        The base name for the dependent variable. Default is 'Y'.

    dependent_value : {None, 'symbol', tuple}, optional
        The value to substitute for the dependent variable. If 'symbol',
        the variable is left as a symbol. If None, it is substituted
        with a value of 1. If a tuple, it is substituted with the
        corresponding value. Default is 'symbol'.

    Examples
    --------
    >>> from econmodels.agent_functions import FunctionalForms

    # Construct the functional form of a Cobb-Douglas function with two inputs.
    >>> func_forms = FunctionalForms()
    >>> cobb_douglas, symboldict = func_forms.cobb_douglas()
    >>> print(cobb_douglas)
    C - Y + beta[0]*beta[1]*x[0]**alpha[0]*x[1]**alpha[1]

    # Construct the functional form of a function with perfect substitutes
    # for two inputs 'k_1' and 'k_2' with coefficients 0.5 and 0.7,
    # respectively, and a dependent variable 'Y' with a value of 100 and a
    # constant 'C' of 10.
    >>> func_forms = FunctionalForms(
    ... num_inputs=2, input_name='k',
    ... coeff_name='beta', coeff_values=(0.5, 0.7),
    ... dependent_name='Y', dependent_value=100,
    ... constant_name='C')
    >>> substitutes, symboldict = func_forms.substitutes()
    >>> print(substitutes)
    0.5*k[0] + 0.7*k[1] + 10 - Y

    # Construction the functional form of a CES function.
    >>> func_forms = FunctionalForms()
    >>> ces, symboldict = func_forms.ces()
    >>> print(ces)
    C - Y + (beta[0]*x[0]**alpha + beta[1]*x[1]**alpha)**(1/alpha)
    """

    def __init__(
        self,
        num_inputs=2, input_name='x',
        coeff_name='beta', coeff_values='symbol',
        exponent_name='alpha', exponent_values='symbol',
        dependent_name='Y', dependent_value='symbol',
        constant_name='C', constant_value='symbol'
    ):
        # Check that number of inputs passed is greater than 0.
        if num_inputs < 0:
            raise Exception(
                f"{num_inputs} inputs passed. Number of inputs must be greater than zero."
            )

        self.num_inputs = num_inputs
        self.input_name = input_name
        self.coeff_name = coeff_name
        self.coeff_values = coeff_values
        self.exponent_name = exponent_name
        self.exponent_values = exponent_values
        self.dependent_name = dependent_name
        self.dependent_value = dependent_value
        self.constant_name = constant_name
        self.constant_value = constant_value

    ##########################################################################
    ## Substitute Values
    ##########################################################################

    def sub_values(self, num_inputs, func, symbol_values):
        """
        Substitute symbol values into a function.

        Parameters
        ----------
        num_inputs : int
            The number of input variables for the function.

        func : SymPy expression
            The function to substitute values into.

        symbol_values : list
            A list of symbol-value pairs to substitute into the function.
            If the value is None, the symbol is substituted with a tuple of 1s.
            If the value is a tuple, the indexed symbol is substituted with
            values in that tuple.
            If the value is a integer, the symbol is substituted with that
            integer value.

        Returns
        -------
        SymPy expression
            The function with symbol values substituted in.
        """

        for sym, values in symbol_values:
            if values == None and type(sym) == sp.tensor.indexed.IndexedBase:
                func = func.subs(sym, tuple([1]*num_inputs))
            elif values == None and type(sym) == sp.core.symbol.Symbol:
                func = func.subs(sym, 1)
            elif values != None and (isinstance(values, tuple) or isinstance(values, int)) == True:
                func = func.subs(sym, values)

        return func

    ##########################################################################
    ## Functional Forms
    ##########################################################################

    def polynomial_combination(self):
        """
        Construct a polynomial function.

        Returns
        -------
        func_form : sympy expression
            The functional form of the Cobb-Douglas production function.
        
        symboldict : dict
            A dictionary of the symbols and indexes used in the function.
        """

        # Create a dictionary of the symbols and indexes.
        symboldict = {
            'coefficient': sp.IndexedBase(f"{self.coeff_name}"),
            'constant': sp.symbols(f"{self.constant_name}"),
            'dependent': sp.symbols(f"{self.dependent_name}"),
            'exponent': sp.IndexedBase(f"{self.exponent_name}"),
            'i': sp.symbols('i', cls=sp.Idx),
            'input': sp.IndexedBase(f"{self.input_name}")
        }
    
        # Set the range for indexed inputs.
        irange = (symboldict['i'], 0, self.num_inputs - 1)

        # Define the functional form of the inputs for a polynomial equation:
        # cX^a + dX^b.
        input_form = (
            symboldict['coefficient'][symboldict['i']] *
            symboldict['input'][symboldict['i']]**
            symboldict['exponent'][symboldict['i']]
        )
    
        # Define the function form with the indexed rate of inputs, constant,
        # and dependent variable.
        func_form = (
            sp.Sum(input_form, irange) +
            symboldict['constant'] -
            symboldict['dependent']
        ).doit()

        # Substitute the symbols in the function with the passed
        # values or with a value of 1 if None.
        func_form = self.sub_values(
            num_inputs=self.num_inputs,
            func=func_form,
            symbol_values=[
                [symboldict['coefficient'], self.coeff_values],
                [symboldict['exponent'], self.exponent_values],
                [symboldict['dependent'], self.dependent_value],
                # [symboldict['constant'], self.constant_value]
            ]
        )

        # Return the functional form and the symboldict.
        return func_form, symboldict

    def cobb_douglas(self):
        """
        Construct a Cobb-Douglas function: cX^a*dY^b.

        Returns
        -------
        func_form : sympy expression
            The functional form of the Cobb-Douglas production function.
        
        symboldict : dict
            A dictionary of the symbols and indexes used in the function.
        """

        # Create a dictionary of the symbols and indexes.
        symboldict = {
            'coefficient': sp.IndexedBase(f"{self.coeff_name}"),
            'constant': sp.symbols(f"{self.constant_name}"),
            'dependent': sp.symbols(f"{self.dependent_name}"),
            'exponent': sp.IndexedBase(f"{self.exponent_name}"),
            'i': sp.symbols('i', cls=sp.Idx),
            'input': sp.IndexedBase(f"{self.input_name}")
        }

        # Set the range for indexed inputs.
        irange = (symboldict['i'], 0, self.num_inputs - 1)

        # Define the form of the inputs in a Cobb-Douglas function: cX^a*dY^b.
        input_form = (
            symboldict['coefficient'][symboldict['i']] *
            symboldict['input'][symboldict['i']]**
            symboldict['exponent'][symboldict['i']]
        )

        # Define the function form with the indexed rate of inputs, constant,
        # and dependent variable.
        func_form = (
            sp.Product(input_form, irange)  +
            symboldict['constant'] -
            symboldict['dependent']
        ).doit()

        # Substitute the symbols in the function with the passed values or with a
        # value of 1 if None.
        func_form = self.sub_values(
            num_inputs=self.num_inputs,
            func=func_form,
            symbol_values=[
                [symboldict['coefficient'], self.coeff_values],
                [symboldict['exponent'], self.exponent_values],
                [symboldict['dependent'], self.dependent_value]
            ]
        )

        # Return the functional form and the symboldict.
        return func_form, symboldict

    def substitutes(self):
        """
        Construct a function with perfect substitutes inputs.

        A function with perfect substitutes is a linear combination of inputs,
        such that each input can be completely substituted for the other without
        any change in output.

        Returns
        -------
        func_form : sympy expression
            The functional form of the production function with perfect
            substitutes.

        symboldict : dict
            A dictionary of the symbols and indexes used in the function.

        Notes
        -----
        This function makes use of the `polynomial_combination` function to
        create the functional form of a function with perfect substitutes. Once
        exponent_values are set, they will remain None.
        """

        # Use the polynomial_combination function without exponents to create a
        # form for perfect substitutes.
        self.exponent_values = None
        
        func_form, symboldict = self.polynomial_combination()

        # Return the functional form and the symboldict.
        return func_form, symboldict

    def complements(self):
        """
        Construct a function for perfect complement inputs.

        Returns
        -------
        func_form : sympy expression
            The functional form for the production function
    
        symboldict : dict
            The dictionary of the symbols and indexes used in the function

        """
        
        # Create a dictionary of the symbols and indexes.
        symboldict = {
            'coefficient': sp.IndexedBase(f"{self.coeff_name}"),
            'constant': sp.symbols(f"{self.constant_name}"),
            'dependent': sp.symbols(f"{self.dependent_name}"),
            'exponent': sp.IndexedBase(f"{self.exponent_name}"),
            'i': sp.symbols('i', cls=sp.Idx),
            'input': sp.IndexedBase(f"{self.input_name}")
        }
        
        # Define the form of the inputs to be the minimum of the different
        # linear terms: min{x_1, x_2, x_3,..., x_n}
        input_form = sp.Min(
            *[symboldict['input'][symboldict['i']] for symboldict['i'] in range(self.num_inputs)]
        )

        # Define the functional form as the input_form - constant - dependent.
        func_form = input_form - symboldict['dependent']

        # Substitute the symbols in the function with the passed values or with a
        # value of 1 if None.
        func_form = self.sub_values(
            num_inputs=self.num_inputs,
            func=func_form,
            symbol_values=[
                [symboldict['coefficient'], self.coeff_values],
                [symboldict['dependent'], self.dependent_value]
            ]
        )

        # Return the functional form and the symboldict.
        return func_form, symboldict

    def ces(self):
        """
        Construct a Constant Elasticity of Substitution (CES) function.

        Returns
        -------
        func_form : sympy expression
            The CES function expression.

        symboldict : dict
            A dictionary of the symbols and indexes used in the function expression.
        """

        # Create a dictionary of the symbols and indexes.
        symboldict = {
            'coefficient': sp.IndexedBase(f"{self.coeff_name}"),
            'constant': sp.symbols(f"{self.constant_name}"),
            'dependent': sp.symbols(f"{self.dependent_name}"),
            'input': sp.IndexedBase(f"{self.input_name}"),
            'coeff': sp.IndexedBase(f"{self.coeff_name}"),
            'exponent': sp.symbols(f"{self.exponent_name}"),
            'i': sp.symbols('i', cls=sp.Idx)
        }

        # Set the range for indexed inputs.
        irange = (symboldict['i'], 0, self.num_inputs - 1)

        # Define the form of the inputs into CES function.
        input_form = (
            symboldict['coefficient'][symboldict['i']] *
            symboldict['input'][symboldict['i']]**symboldict['exponent']
        )

        # Define the functional form with the indexed inputs, constant,
        # and dependent variable.
        func_form = (
            sp.Sum(input_form, irange)**(1/symboldict['exponent']) +
            symboldict['constant'] - symboldict['dependent']
        ).doit()

        # Substitute the symbols in the function with the passed values or with a
        # value of 1 if None.
        func_form = self.sub_values(
            num_inputs=self.num_inputs,
            func=func_form,
            symbol_values=[
                [symboldict['coefficient'], self.coeff_values],
                [symboldict['exponent'], self.exponent_values],
                [symboldict['dependent'], self.dependent_value]
            ]
        )

        # Return the functional form and the symboldict.
        return func_form, symboldict

    def quasi_linear():
        """
        Construct A quasi-linear utility function has a linear and non-linear
        component. The linear component is the numeraire. All of the other
        terms will be be combined by an arbitrary function:

        \left(x_{1},\dots ,x_{L}\right)=x_{1}+\theta \left(x_{2},...,x_{L}\right)
        """
        print("Quasi-linear functions are being developed.")