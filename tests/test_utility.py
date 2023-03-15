import sympy as sp
import pytest
from econmodels.functional_forms.utility import Utility

"""
Functions to test the Utility class.
"""

def test_init():
    # Test Case 1: Create Cobb-Douglas utility function with two inputs.
    # Check that the utility function is correct.
    # u(x1,x2) = beta1*x1**alpha1 + beta2*x2**alpha2

    # Define number of inputs.
    num_inputs = 2

    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        exponent_values=(2,2),
        func_form='cobb-douglas'
    )

    # Define the expected utility function.
    expected = 'C - U + beta[0]*beta[1]*x[0]**alpha[0]*x[1]**alpha[1]'

    # Check that the utility function is correct.
    assert str(util.function) == expected

    # Test Case 2: Create perfect complements utility function with two inputs.
    # Check that the utility function is correct.
    # u(x1,x2) = min(x1,x2)

    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        coeff_values=3,
        func_form='complements'
    )

    # Define expected utility function.
    expected = '-U + Min(x[0], x[1])'
    
    # Check that the utility function is correct.
    assert str(util.function) == expected

    # Test Case 3: Create Perfect Substitutes utility function with two inputs.
    # Check that the utility function is correct.
    # u(x1,x2) = x1 + x2

    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        coeff_values=(3,3),
        func_form='substitutes'
    )

    # Define expected utility function.
    expected = 'C - U + 3*x[0] + 3*x[1]'

    # Check that the utility function is correct.
    assert str(util.function) == expected

    # Test Case 4: Create CES utility function with two inputs.
    # Check that the utility function is correct.
    # u(x1,x2) = (beta1*x1**alpha + beta2*x2**alpha)**(1/(alpha))

    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        coeff_values=(3,3),
        exponent_values=2,
        func_form='ces'
    )

    # Define the expected utility function.
    expected = 'C - U + sqrt(2*x[0]**2 + 3*x[1]**2)'

    # Check that the utility function is correct.
    assert str(util.function) == expected

def test_get_utility():
    # Test Case 1: Create a Cobb-Douglas utility function with two inputs.
    # Substitute values into the function where the values are valid and
    # check that the utility function is correct.

    # Define number of inputs.
    num_inputs = 2

    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        coeff_values=(2,2),
        exponent_values=(2,2),
        func_form='cobb-douglas'
    )

    # Define the expected utility function.
    expected = 'C - U + 4*x[0]**2*x[1]**2'

    # Check that the utility function is correct.
    assert str(util.function) == expected

    # Define the values to substitute into the utility function.
    u = util.get_utility(input_values=[1,1], constant=1)

    # Define expected utility.
    expected = 5

    assert u == 5

    # where alpha1 = alpha2 = 1
    # and beta1 = beta2 = 1
    # and x1,x2 are positive.
    # The utility function should be:
    # u(x1,x2) = x1 + x2
    # The optimal bundle should be:
    # x1 = x2 = 1/2
    # The optimal utility should be:
    # u(x1,x2) = 1
    # The marginal utility of x1 should be:
    # mu1(x1,x2) = 1
    # The marginal utility of x2 should be:
    # mu2(x1,x2) = 1
    # The marginal rate of substitution should be:
    # mu1(x1,x2)/mu2(x1,x2) = 1
    # The marginal rate of transformation should be:
    # mu2(x1,x2)/mu1(x1,x2) = 1