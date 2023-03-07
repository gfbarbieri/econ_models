# econmodels.primitives.functional_forms
# Common funcitonal forms for functions used in economoics.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
Funcitons that represent common funcitonal forms for utility,
production, and constraint functions in economoics.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp

##########################################################################
## Substitute Values
##########################################################################

def sub_values(num_inputs, func, symbol_values):
    for var, values in symbol_values:
        if values == None:
            func = func.subs(var, tuple([1]*num_inputs))
        elif values != None and isinstance(values, tuple) == True:
            func = func.subs(var, values)

    return func

##########################################################################
## Polynomial Equation
##########################################################################

def polynomial_combination(
    num_inputs=2, input_name='k',
    coeff_name='beta', coeff_values='symbol',
    exponent_name='alpha', exponent_values='symbol',
    dependent_name='Y', dependent_value='symbol',
    constant_name='C'
):
    """
    This function returns a polynomial function.

    Parameters
    ----------
    num_inputs : int
        The number of goods/characteristics that are inputs into the
        consumer's utility function and budget constraint.
    input_name : string
        The character used as the input symbol.
    coeff_values : tuple
        The linear coefficient values.
    coeff_name : string
        The character symbol used to represent coefficients.
    exponent_values : tuple
        The exponent values.
    exponent_name : string
        The character symbol used to represent exponents.
    dependent_value : tuple
        The values of the dependent variable, if a constant is wanted.
    dependent_name : string
        The character symbol used to represent the dependent variable.
    constant_name : string
        The character symbol used to represent a constant.

    Returns
    -------
    None

    Examples
    --------
    """

    # Create a dictionary of the symbols and indexes.
    symboldex = {
        'i': sp.symbols('i', cls=sp.Idx),
        'dependent': sp.symbols(f"{dependent_name}"),
        'input': sp.IndexedBase(f"{input_name}"),
        'coefficient': sp.IndexedBase(f"{coeff_name}"),
        'exponent': sp.IndexedBase(f"{exponent_name}"),
        'constant': sp.symbols(f"{constant_name}")
    }

    # Define the functional form of the inputs for a polynomial equation:
    # cX^a + dX^b.
    input_form = (
        symboldex['coefficient'][symboldex['i']] *
        symboldex['input'][symboldex['i']]**symboldex['exponent'][symboldex['i']]
    )

    # Set the range for indexed inputs.
    range = (symboldex['i'], 0, num_inputs - 1)
    
    # Define the function form with the indexed rate of inputs, constant,
    # and dependent variable.
    func_form = (
        sp.Sum(input_form, range) +
        symboldex['constant'] -
        symboldex['dependent']
    ).doit()

    # Substitute the symbols in the function with the passed
    # values or with a value of 1 if None.
    func_form = sub_values(
        num_inputs=num_inputs,
        func=func_form,
        symbol_values=[
            [symboldex['coefficient'], coeff_values],
            [symboldex['exponent'], exponent_values],
            [symboldex['dependent'], dependent_value]
        ]
    )

    # Return the functional form and the symboldex.
    return func_form, symboldex

##########################################################################
## Cobb-Douglas Function
##########################################################################

def cobb_douglas(
    num_inputs=2, input_name='k',
    coeff_name='beta', coeff_values='symbol',
    exponent_name='alpha', exponent_values='symbol',
    dependent_name='Y', dependent_value='symbol',
    constant_name='C'
):
    """
    This function returns a Cobb-Douglas function.

    Parameters
    ----------
    num_inputs : int
        The number of goods/characteristics that are inputs into the
        consumer's utility function and budget constraint.
    input_name : string
        The character used as the input symbol.
    coeff_values : tuple
        The linear coefficient values.
    coeff_name : string
        The character symbol used to represent coefficients.
    exponent_values : tuple
        The exponent values.
    exponent_name : string
        The character symbol used to represent exponents.
    dependent_value : tuple
        The values of the dependent variable, if a constant is wanted.
    dependent_name : string
        The character symbol used to represent the dependent variable.
    constant_name : string
        The character symbol used to represent a constant.

    Returns
    -------
    None

    Examples
    --------
    """

    # Create a dictionary of the symbols and indexes.
    symboldex = {
        'i': sp.symbols('i', cls=sp.Idx),
        'dependent': sp.symbols(f"{dependent_name}"),
        'input': sp.IndexedBase(f"{input_name}"),
        'coefficient': sp.IndexedBase(f"{coeff_name}"),
        'exponent': sp.IndexedBase(f"{exponent_name}"),
        'constant': sp.symbols(f"{constant_name}")
    }

    # Define the function form of a Cobb-Douglas function: cX^a*dY^b.
    input_form = (
        symboldex['coefficient'][symboldex['i']] *
        symboldex['input'][symboldex['i']]**symboldex['exponent'][symboldex['i']]
    )

    # Set the range for indexed inputs.
    range = (symboldex['i'], 0, num_inputs - 1)

    # Define the function form with the indexed rate of inputs, constant,
    # and dependent variable.
    func_form = (
        sp.Product(input_form, range)  +
        symboldex['constant'] -
        symboldex['dependent']
    ).doit()

    # Substitute the symbols in the function with the passed values or with a
    # value of 1 if None.
    func_form = sub_values(
        num_inputs=num_inputs,
        func=func_form,
        symbol_values=[
            [symboldex['coefficient'], coeff_values],
            [symboldex['exponent'], exponent_values],
            [symboldex['dependent'], dependent_value]
        ]
    )

    # Return the functional form and the symboldex.
    return func_form, symboldex

##########################################################################
## Pefect Substitutes
##########################################################################

def perfect_substitutes(
    num_inputs=2, input_name='k',
    coeff_name='beta', coeff_values='symbol',
    dependent_name='Y', dependent_value='symbol',
    constant_name='C'
):
    """
    This function returns a Cobb-Douglas function.

    Parameters
    ----------
    num_inputs : int
        The number of goods/characteristics that are inputs into the
        consumer's utility function and budget constraint.
    input_name : string
        The character used as the input symbol.
    coeff_values : tuple
        The linear coefficient values.
    coeff_name : string
        The character symbol used to represent coefficients.
    dependent_value : tuple
        The values of the dependent variable, if a constant is wanted.
    dependent_name : string
        The character symbol used to represent the dependent variable.
    constant_name : string
        The character symbol used to represent a constant.

    Returns
    -------
    None

    Examples
    --------
    """

    func_form, symboldex = polynomial_combination(
        num_inputs=num_inputs, input_name=input_name,
        coeff_name=coeff_name, coeff_values=coeff_values,
        exponent_values=None,
        dependent_name=dependent_name, dependent_value=dependent_value,
        constant_name=constant_name
    )

    # Return the functional form and the symboldex.
    return func_form, symboldex

##########################################################################
## Perfect Complements
##########################################################################

def perfect_complements(
    num_inputs=2, input_name='k',
    coeff_name='beta', coeff_values='symbol',
    dependent_name='Y', dependent_value='symbol',
):
    """
    This function returns a Cobb-Douglas function.

    Parameters
    ----------
    num_inputs : int
        The number of goods/characteristics that are inputs into the
        consumer's utility function and budget constraint.
    input_name : string
        The character used as the input symbol.
    coeff_values : tuple
        The linear coefficient values.
    coeff_name : string
        The character symbol used to represent coefficients.
    dependent_value : tuple
        The values of the dependent variable, if a constant is wanted.
    dependent_name : string
        The character symbol used to represent the dependent variable.
    constant_name : string
        The character symbol used to represent a constant.

    Returns
    -------
    None

    Examples
    --------
    """

    # Create a dictionary of the symbols and indexes.
    symboldex = {
        'dependent': sp.symbols(f"{dependent_name}"),
        'input': sp.IndexedBase(f"{input_name}"),
        'coefficient': sp.IndexedBase(f"{coeff_name}"),
        'i': sp.symbols('i', cls=sp.Idx)
    }

    # input_form is going to be the minimum of the different
    # linear terms: min{x_1, x_2, x_3,..., x_n}
    input_form = sp.Min(
        *[symboldex['input'][symboldex['i']] for symboldex['i'] in range(num_inputs)]
    )

    # func_form is the input_form - constant - dependent.
    func_form = input_form - symboldex['dependent']

    # Substitute the symbols in the function with the passed values or with a
    # value of 1 if None.
    func_form = sub_values(
        num_inputs=num_inputs,
        func=func_form,
        symbol_values=[
            [symboldex['coefficient'], coeff_values],
            [symboldex['dependent'], dependent_value]
        ]
    )

    # Return the functional form and the symboldex.
    return func_form, symboldex

##########################################################################
## Constant Elasticity of Substitution (CES) Function
##########################################################################

def ces(
    num_inputs=2, input_name='k',
    coeff_name='beta', coeff_values='symbol',
    exponent_name='alpha', exponent_values='symbol',
    dependent_name='Y', dependent_value='symbol'
):
    """
    This function returns a Cobb-Douglas function.

    Parameters
    ----------
    num_inputs : int
        The number of goods/characteristics that are inputs into the
        consumer's utility function and budget constraint.
    input_name : string
        The character used as the input symbol.
    coeff_values : tuple
        The linear coefficient values.
    coeff_name : string
        The character symbol used to represent coefficients.
    exponent_values : tuple
        The exponent values.
    exponent_name : string
        The character symbol used to represent exponents.
    dependent_value : tuple
        The values of the dependent variable, if a constant is wanted.
    dependent_name : string
        The character symbol used to represent the dependent variable.

    Returns
    -------
    None

    Examples
    --------
    """
    # Create a dictionary of the symbols and indexes.
    symboldex = {
        'dependent': sp.symbols(f"{dependent_name}"),
        'input': sp.IndexedBase(f"{input_name}"),
        'coeff': sp.IndexedBase(f"{coeff_name}"),
        'exponent': sp.symbols(f"{exponent_name}"),
        'i': sp.symbols('i', cls=sp.Idx)
    }

    # Define the function form of CES function.
    input_form = (
        symboldex['coeff'][symboldex['i']] *
        symboldex['input'][symboldex['i']]**symboldex['exponent']
    )

    # Set the range for indexed inputs.
    range = (symboldex['i'], 0, num_inputs - 1)

    # Define the function form with the indexed rate of inputs, constant,
    # and dependent variable.
    func_form = (
        sp.Sum(input_form, range)**(1/symboldex['exponent']) +
        symboldex['constant'] - symboldex['dependent']
    ).doit()

    # Substitute the symbols in the function with the passed values or with a
    # value of 1 if None.
    func_form = sub_values(
        num_inputs=num_inputs,
        func=func_form,
        symbol_values=[
            [symboldex['coefficient'], coeff_values],
            [symboldex['exponent'], exponent_values],
            [symboldex['dependent'], dependent_value]
        ]
    )

    # Return the functional form and the symboldex.
    return func_form, symboldex

##########################################################################
## Quasi-Linear Function
##########################################################################

def quasi_linear():
    pass