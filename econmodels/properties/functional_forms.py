# econmodels.primitives.functional_forms
# Common funcitonal forms for utility, production, and constraints in economoics.
#
# Author:   Greg Barbieri
#
# For license information, see LICENSE.txt

"""
Funcitons that represent common funcitonal forms for utility, production, and constraints in economoics.
"""

##########################################################################
## Imports
##########################################################################

import sympy as sp

##########################################################################
## Generalized Function
##########################################################################

def generalized(
    num_inputs=2, input_name='k',
    coeff_name='beta', coeff_values='symbol',
    exponent_name='alpha', exponent_values='symbol',
    dependent_name='Y', dependent_value='symbol', model='product'
):
    """ This function represents a generalized functional form of common
    functions used in economics.

    The function supports the following functional forms:
        1. Cobb-Douglas with IRS, DRS, or CRS.
        2. Linear, such as a budget constraint or perfect substitutes.
        3. Quasi-linear without logarithms or other functions.

    Parameters
    ----------
    num_inputs : int
        The number of goods/characteristics that are inputs into the consumer's utility function and
        budget constraint.
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
    model : string
        The model for combining inputs, either `product` for product or `sum` for summation.

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
        'exponent': sp.IndexedBase(f"{exponent_name}"),
        'i': sp.symbols('i', cls=sp.Idx)
    }

    form = symboldex['coeff'][symboldex['i']]*symboldex['input'][symboldex['i']]**symboldex['exponent'][symboldex['i']]
    range = (symboldex['i'], 0, num_inputs - 1)

    if model == 'product':
        func = (sp.Product(form, range) - symboldex['dependent']).doit()
    elif model == 'sum':
        func = (sp.Sum(form, range) - symboldex['dependent']).doit()

    # If specific values were passed to the coefficients, or None type was passed, then
    # substitute the symbols in the function with the passed values or with a value of 1,
    # respectively.
    
    # Coefficient variables:
    if coeff_values == None:
        func = func.subs(symboldex['coeff'], tuple([1]*num_inputs))
    elif coeff_values != None and isinstance(coeff_values, tuple) == True:
        func = func.subs(symboldex['coeff'], coeff_values)

    # Exponent variables:
    if exponent_values == None:
        func = func.subs(symboldex['exponent'], tuple([1]*num_inputs))
    elif exponent_values != None and isinstance(exponent_values, tuple) == True:
        func = func.subs(symboldex['exponent'], exponent_values)

    # Dependent variable:
    if dependent_value != None and isinstance(dependent_value, tuple) == True:
        func = func.subs(symboldex['dependent'], dependent_value)

    return func, symboldex

def cobb_douglas():
    pass

def perfect_substitutes():
    pass

def ces():
    pass

def perfect_complements():
    pass