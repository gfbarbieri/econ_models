##########################################################################
## Imports
##########################################################################

import sympy as sp

##########################################################################
## Generalized Function
##########################################################################

def generalized_function(
    num_inputs=2, input_name='k',
    coeff_name='beta', coeff_values='symbol',
    exponent_name='alpha', exponent_values='symbol',
    dependent_name='Y', dependent_value='symbol', model='product'
):

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