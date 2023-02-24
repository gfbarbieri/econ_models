##########################################################################
## Imports
##########################################################################

import sympy as sp

##########################################################################
## Cobb-Douglas
##########################################################################

def cobb_douglas(
    num_inpts=2, input_name='k',
    coeff_name='beta', coeff_values=None,
    exponent_name='alpha', exponent_values=None
):

    # Define the inputs into the function.
    inputs = sp.IndexedBase(f"{input_name}")
    coeff = sp.IndexedBase(f"{coeff_name}")
    exponent = sp.IndexedBase(f"{exponent_name}")
    i = sp.symbols('i')

    # Create generalized production function as a product of the inputs.
    func = sp.Product(coeff[i]*inputs[i]**exponent[i], (i, 0, num_inpts-1))

    # If values for the coefficients were passed, substitute symbols with passed values.
    if coeff_values == None:
        func = func.doit().subs(coeff, tuple([1]*num_inpts))
    elif coeff_values != None and len(coeff_values) == num_inpts:
        func = func.doit().subs(coeff, coeff_values)

    # If values for the exponents were passed, substitute symbols with passed values.
    if exponent_values == None:
        func = func.doit().subs(exponent, tuple([1]*num_inpts))
    elif exponent_values != None and len(exponent_values) == num_inpts:
        func = func.doit().subs(exponent, exponent_values)

    return func

##########################################################################
## Linear Combination
##########################################################################

def linear_combination(num_inpts=2, input_name='x', coeff_name='beta', coeff_values=None):

    # Define the inputs into the function.
    inputs = sp.IndexedBase(f"{input_name}")
    coeff = sp.IndexedBase(f"{coeff_name}")
    i = sp.symbols('i')

    # Create generalized function as a linear combination of inputs.
    func = sp.Sum(coeff[i]*inputs[i], (i, 0, num_inpts-1))

    # If values for coefficients were passed, substitute symbols with passed values.
    if coeff_values == None:
        func = func.doit().subs(coeff, tuple([1]*num_inpts))
    elif coeff_values != None and len(coeff_values) == num_inpts:
        func = func.doit().subs(coeff, coeff_values)

    return func