# econmodels.agent_functions.functional_forms
# Common funcitonal forms for functions used in economoics.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
Class that represent common functional forms for utility, production, and
resource constraint functions in economoics.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp

##########################################################################
## Functional Forms Class
##########################################################################

class BaseForms():
    """
    The BaseForms class returns common functional forms used in economics
    to represent utility and production functions. Each function form follows
    a similar pattern: define the symbols used, create the index range for
    the inputs, define how form the inputs will take, define the functional form
    with multiple inputs, substitute symbols for any values passed into the
    FunctionalForms class, return both the final functional form and the 
    symbol_dict.

    Attributes
    ----------
    num_inputs : int
        The number of input variables for the polynomial equation.

    input_name : str
        The base name for the input variables.

    coeff_name : str
        The base name for the coefficient variables.

    coeff_values : {None, 'symbol', tuple}
        The values to substitute for the coefficient variables. If 'symbol',
        use the variables as symbols. If None, substitute with a tuple of 1s.

    constant_name : str
        The base name for the constant variable.

    constant_value : {None, 'symbol', tuple}
        The values to substitute for the constant variable. If 'symbol',
        use the variable as a symbol. If None, substitute with 1.

    exponent_name : str
        The base name for the exponent variables.

    exponent_values : {None, 'symbol', tuple}
        The values to substitute for the exponent variables. If 'symbol',
        use the variables as symbols. If None, substitute with a tuple of 1s.

    dependent_name : str
        The base name for the dependent variable.

    dependent_value : {None, 'symbol', tuple}
        The values to substitute for the dependent variable. If 'symbol',
        use the variable as a symbol. If None, substitute with 1.

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

    constant_name : str, optional

    constant_value : {None, 'symbol', tuple}, optional

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

    Construct the functional form of a Cobb-Douglas function with two inputs.
    >>> func_forms = BaseForms()
    >>> cobb_douglas, symbol_dict = func_forms.cobb_douglas()
    >>> print(cobb_douglas)
    C - Y + beta[0]*beta[1]*x[0]**alpha[0]*x[1]**alpha[1]

    Construct the functional form of a function with perfect substitutes
    for two inputs 'k_1' and 'k_2' with coefficients 0.5 and 0.7,
    respectively, and a dependent variable 'Y' with a value of 100 and a
    constant 'C' of 10.
    >>> func_forms = BaseForms(
    ... num_inputs=2, input_name='k',
    ... coeff_name='beta', coeff_values=(0.5, 0.7),
    ... dependent_name='Y', dependent_value=100,
    ... constant_name='C')
    >>> substitutes, symbol_dict = func_forms.substitutes()
    >>> print(substitutes)
    0.5*k[0] + 0.7*k[1] + 10 - Y

    Construction the functional form of a CES function.
    >>> func_forms = BaseForms()
    >>> ces, symbol_dict = func_forms.ces()
    >>> print(ces)
    C - Y + (beta[0]*x[0]**alpha + beta[1]*x[1]**alpha)**(1/alpha)
    """

    def __init__(
        self,
        num_inputs=2, input_name='x',
        coeff_name='beta', coeff_values='symbols',
        exponent_name='alpha', exponent_values='symbols',
        dependent_name='Y', dependent_value='symbols',
        constant_name='C', constant_value='symbols'
    ):
        # Check that number of inputs passed is greater than 0.
        if num_inputs < 0:
            raise Exception(
                f"Negative inputs passed: {num_inputs}."
            )

        # Set attributes.
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

        # Create the symbol_dict used for most functional forms. If num_inputs
        # is equal to 1, then the variables are not indexed and are only a
        # symbol object. If num_inputs > 1, then variables are indexed and are
        # indexed base objects.
        self.symbol_dict = {
            'constant': sp.symbols(f"{self.constant_name}", real=True),
            'dependent': sp.symbols(f"{self.dependent_name}", real=True),
            'i': sp.symbols('i', cls=sp.Idx),
            'coefficient': sp.IndexedBase(f"{self.coeff_name}", real=True),
            'exponent': sp.IndexedBase(f"{self.exponent_name}", real=True),
            'inputs': sp.IndexedBase(f"{self.input_name}", real=True)
        }

        # Define a dictionary of symbols to strings.
        self.symbol_str_dict = {
            str(self.symbol_dict['constant']): self.symbol_dict['constant'],
            str(self.symbol_dict['dependent']): self.symbol_dict['dependent'],
            str(self.symbol_dict['i']): self.symbol_dict['i'],
            str(self.symbol_dict['coefficient']): self.symbol_dict['coefficient'],
            str(self.symbol_dict['exponent']): self.symbol_dict['exponent'],
            str(self.symbol_dict['inputs']): self.symbol_dict['inputs']
        }

        # Set the range for indexed inputs, with the exception of complements
        # function.
        self.irange = (self.symbol_dict['i'], 0, self.num_inputs - 1)

    ##########################################################################
    ## Substitute Values
    ##########################################################################

    def sub_symbols(self, func, symbol_values, symbol_dict=None):
        """
        Substitute symbol values into a function.

        Parameters
        ----------
        func : SymPy expression
            The function to substitute values into.

        values : dict
            A dict of symbol-value pairs to substitute into the function.

        symbol_dict : dict, optional
            A dict of symbols to substitute into the function. If None, then    
            the default symbol_dict is used. Default is None.

        Returns
        -------
        SymPy expression
            The function with symbol values substituted in.
        """

        # If no custom symbol_dict is given, then use the default symbol_dict.
        if symbol_dict == None:
            symbol_dict = self.symbol_dict

        # Confirm the symbol_dict contains the symbols passed in the values
        # dictionary. Otherwise, raise an exception.
        symbols = list(symbol_values.keys())

        if not all([sym in symbol_dict.values() for sym in symbols]):
            raise Exception(f"Some symbols missing from symbol_dict.")

        # Finalize the values dictionary:
        #   1. If the value is 'symbols', then we don't want to make any
        #   substitutions since the default functional form is already in terms
        #   of symbols.
        #   2. If the value is None, then we want to substitute the symbol
        #   object or IndexedBase object with 1.
        #   3. If the value is a tuple which includes None, then we want to
        #   substitute None in the tuple with 1. This will be used to subsitute
        #   the value of a symbol or IndexedBase object with 1.
        #   4. If the value is a tuple for an IndexedBase object and the tuple
        #   contains a mix of numbers, None types, and 'symbol', then the
        #   'symbol' should be substituted with the symbol object for the index
        #   in the tuple and the None types should be substituted with 1.
        #   5. Otherwise, substitute symbol with the passed values.

        for symbol, value in symbol_values.copy().items():
            if value == 'symbols':
                symbol_values.pop(symbol)
            elif value == None:
                if type(symbol) == sp.tensor.indexed.IndexedBase:
                    symbol_values.update({symbol : tuple([1]*self.num_inputs)})
                elif type(symbol) == sp.core.symbol.Symbol:
                    symbol_values.update({symbol : 1})
            elif type(value) == tuple:
                if None in value:
                    symbol_values.update({symbol : tuple([1 if val == None else val for val in value])})
                elif 'symbol' in value:
                    symbol_values.update({symbol : tuple([symbol[i] if val == 'symbol' else val for i, val in enumerate(value)])})

        func = func.subs(symbol_values)

        return func

    ##########################################################################
    ## Functional Forms
    ##########################################################################

    def additive(self):
        """
        Construct an additive function where inputs are multiplied by a
        coefficient and summed together with a constant. The functional form
        is: C + beta[0]*x[0] + beta[1]*x[1] + ... + beta[n]*x[n] - Y. Each input
        is included only once, multiplied by one coefficient and one power. The
        dependent variable is included in the functional form as the function
        is a homogenous function.

        Returns
        -------
        func_form : sympy expression
            The functional form of the Cobb-Douglas production function.
        
        symbol_dict : dict
            A dictionary of the symbols and indexes used in the function.
        """

        # Define the functional form of the inputs for an additive function.
        input_form = (
            self.symbol_dict['coefficient'][self.symbol_dict['i']] *
            self.symbol_dict['inputs'][self.symbol_dict['i']]**
            self.symbol_dict['exponent'][self.symbol_dict['i']]
        )
    
        # Define the final function form.
        func_form = (
            sp.Sum(input_form, self.irange) +
            self.symbol_dict['constant'] -
            self.symbol_dict['dependent']
        ).doit()

        # Substitute the symbols in the function with any passed values for
        # the symbols.
        func_form_sub = self.sub_symbols(
            func=func_form,
            symbol_values={
                self.symbol_dict['coefficient']: self.coeff_values,
                self.symbol_dict['exponent']: self.exponent_values,
                self.symbol_dict['constant']: self.constant_value,
                self.symbol_dict['dependent']: self.dependent_value
            }
        )

        return func_form_sub, self.symbol_dict

    def multiplicative(self):
        """
        Construct a multiplicative function: cX^a*dY^b. The functional form
        is: c[0]*x[0]^a[0]*d[0]*y[0]^b[0] + ... + c[n]*x[n]^a[n]*d[n]*y[n]^b[n]
        - Y. Each input is included only once, multiplied by one coefficient
        and one power. The dependent variable is included in the functional
        form as the function is a homogenous function.

        Returns
        -------
        func_form : sympy expression
            The functional form of the multiplicative function.
        
        symbol_dict : dict
            A dictionary of the symbols and indexes used in the function.
        """

        # Define the functional form of the inputs for a multiplicative
        # function.
        input_form = (
            self.symbol_dict['coefficient'][self.symbol_dict['i']] *
            self.symbol_dict['inputs'][self.symbol_dict['i']]**
            self.symbol_dict['exponent'][self.symbol_dict['i']]
        )

        # Define the function form: cX^a*dY^b.
        func_form = (
            sp.Product(input_form, self.irange)  +
            self.symbol_dict['constant'] -
            self.symbol_dict['dependent']
        ).doit()

        # # Substitute the symbols in the function with any passed values for
        # # the symbols.
        func_form_sub = self.sub_symbols(
            func=func_form,
            symbol_values={
                self.symbol_dict['coefficient']: self.coeff_values,
                self.symbol_dict['exponent']: self.exponent_values,
                self.symbol_dict['constant']: self.constant_value,
                self.symbol_dict['dependent']: self.dependent_value
            }
        )

        return func_form_sub, self.symbol_dict

    def minimum_function(self):
        """
        Construct a minimum function of inputs. The functional form is:
        \min{x_0, x_1, x_2,..., x_n} - Y. Each input is included only once.
        The dependent variable is included in the functional form as the
        function is a homogenous function.

        Returns
        -------
        func_form : sympy expression
            The functional form of the minimum function.
    
        symbol_dict : dict
            The dictionary of the symbols and indexes used in the function
        """
        
        # Define the form of the inputs to be the minimum.
        input_form = sp.Min(
            *[self.symbol_dict['coefficient'][i]*self.symbol_dict['inputs'][i] for i in range(self.num_inputs)]
        )

        # Define the functional form.
        func_form = input_form - self.symbol_dict['dependent']

        # Substitute the symbols in the function with the passed values or with
        # a value of 1 if None.
        func_form_sub = self.sub_symbols(
            func=func_form,
            symbol_values={
                self.symbol_dict['coefficient']: self.coeff_values,
                self.symbol_dict['exponent']: self.exponent_values,
                self.symbol_dict['constant']: self.constant_value,
                self.symbol_dict['dependent']: self.dependent_value
            }
        )

        return func_form_sub, self.symbol_dict

    def ces(self):
        """
        Construct a Constant Elasticity of Substitution (CES) function.

        Returns
        -------
        func_form : sympy expression
            The CES function expression.

        symbol_dict : dict
            A dictionary of the symbols and indexes used in the function
            expression.
        """

        # For this version of the CES function, exponents are not indexed.
        # A new exponent symbol is used instead of the symbol_dict.
        exponent = sp.symbols(f"{self.exponent_name}")

        # Define the form of the inputs into CES function.
        input_form = (
            self.symbol_dict['coefficient'][self.symbol_dict['i']] *
            self.symbol_dict['inputs'][self.symbol_dict['i']]**exponent
        )

        # Define the functional form.
        func_form = (
            sp.Sum(input_form, self.irange)**(1/exponent) +
            self.symbol_dict['constant'] -
            self.symbol_dict['dependent']
        ).doit()

        # Substitute values for the symbols. Pass a custom symbol_dict to
        # sub_symbols to update the exponent symbol.
        cust_dict = self.symbol_dict.copy()
        cust_dict['exponent'] = exponent

        func_form_sub = self.sub_symbols(
            func=func_form,
            symbol_dict=cust_dict,
            symbol_values={
                self.symbol_dict['coefficient']: self.coeff_values,
                exponent: self.exponent_values,
                self.symbol_dict['constant']: self.constant_value,
                self.symbol_dict['dependent']: self.dependent_value
            }
        )

        return func_form_sub, self.symbol_dict

    def quasi_linear():
        """
        Construct A quasi-linear utility function has a linear and non-linear
        component. The linear component is the numeraire. All of the other
        terms will be be combined by an arbitrary function:

        \left(x_{1},\dots ,x_{L}\right)=x_{1}+\theta \left(x_{2},...,x_{L}\right)
        """
        print("Quasi-linear functions are being developed.")