import pytest
from econmodels.functional_forms.utility import Utility

"""
Functions to test the Utility class.
"""

def test_init():
    # Test Case 1: Create Cobb-Douglas utility function with two inputs.
    # In test case 1, we create a Utility object with two inputs with the 
    # function form of a cob-douglas utility function. We check that the
    # utility function is correct and that the symboldict has the expected key
    # values and that the key values are equal to names passed into the
    # BaseForms class.

    # Define number of inputs.
    num_inputs = 2

    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        exponent_values=(2,2),
        func_form='cobb-douglas'
    )

    # Define the expected utility function.
    expected = 'C - U + beta[0]*beta[1]*x[0]**2*x[1]**2'

    # Check that the utility function is correct.
    assert str(util.function) == expected

    # Assert that the symboldict is an instance of a dictionary.
    assert isinstance(util.symboldict, dict)

    # Check that the symboldict has expected key values.
    assert all(key in util.symboldict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'exponent', 'input', 'i'
    ])

    # Check that the key values are equal to the names passed into the
    # Utility class.
    for key in util.symboldict.keys():
        if key == 'input':
            assert str(util.symboldict[key])  == util.input_name
        elif key == 'exponent':
            assert str(util.symboldict[key]) == util.exponent_name
        elif key == 'coefficient':
            assert str(util.symboldict[key]) == util.coeff_name
        elif key == 'dependent':
            assert str(util.symboldict[key]) == util.dependent_name
        elif key == 'constant':
            assert str(util.symboldict[key]) == util.constant_name

    # Test Case 2: Create perfect complements utility function with two inputs.
    # In test case 2, we create a Utility object with two inputs with the
    # function form of a perfect complements utility function. We check that
    # the utility function is correct and that the symboldict has the expected
    # key values and that the key values are equal to names passed into the
    # Utility class.

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

    # Assert that the symboldict is an instance of a dictionary.
    assert isinstance(util.symboldict, dict)

    # Check that the symboldict has expected key values.
    assert all(key in util.symboldict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'exponent', 'input', 'i'
    ])

    # Check that the key values are equal to the names passed into the
    # Utility class.
    for key in util.symboldict.keys():
        if key == 'input':
            assert str(util.symboldict[key])  == util.input_name
        elif key == 'exponent':
            assert str(util.symboldict[key]) == util.exponent_name
        elif key == 'coefficient':
            assert str(util.symboldict[key]) == util.coeff_name
        elif key == 'dependent':
            assert str(util.symboldict[key]) == util.dependent_name
        elif key == 'constant':
            assert str(util.symboldict[key]) == util.constant_name

    # Test Case 3: Create Perfect Substitutes utility function with two inputs.
    # In test case 3, we create a Utility object with two inputs with the
    # function form of a perfect substitutes utility function. We check that
    # the utility function is correct and that the symboldict has the expected
    # key values and that the key values are equal to names passed into the
    # Utility class.

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

    # Assert that the symboldict is an instance of a dictionary.
    assert isinstance(util.symboldict, dict)

    # Check that the symboldict has expected key values.
    assert all(key in util.symboldict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'exponent', 'input', 'i'
    ])

    # Check that the key values are equal to the names passed into the
    # Utility class.
    for key in util.symboldict.keys():
        if key == 'input':
            assert str(util.symboldict[key])  == util.input_name
        elif key == 'exponent':
            assert str(util.symboldict[key]) == util.exponent_name
        elif key == 'coefficient':
            assert str(util.symboldict[key]) == util.coeff_name
        elif key == 'dependent':
            assert str(util.symboldict[key]) == util.dependent_name
        elif key == 'constant':
            assert str(util.symboldict[key]) == util.constant_name

    # Test Case 4: Create CES utility function with two inputs.
    # In test case 4, we create a Utility object with two inputs with the
    # function form of a CES utility function. We check that the utility
    # function is correct and that the symboldict has the expected key values
    # and that the key values are equal to names passed into the Utility
    # class.

    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        coeff_values=(3,3),
        exponent_values=2,
        func_form='ces'
    )

    # Define the expected utility function.
    expected = 'C - U + sqrt(3*x[0]**2 + 3*x[1]**2)'

    # Check that the utility function is correct.
    assert str(util.function) == expected

    # Assert that the symboldict is an instance of a dictionary.
    assert isinstance(util.symboldict, dict)

    # Check that the symboldict has expected key values.
    assert all(key in util.symboldict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'exponent', 'input', 'i'
    ])

    # Check that the key values are equal to the names passed into the
    # Utility class.
    for key in util.symboldict.keys():
        if key == 'input':
            assert str(util.symboldict[key])  == util.input_name
        elif key == 'exponent':
            assert str(util.symboldict[key]) == util.exponent_name
        elif key == 'coefficient':
            assert str(util.symboldict[key]) == util.coeff_name
        elif key == 'dependent':
            assert str(util.symboldict[key]) == util.dependent_name
        elif key == 'constant':
            assert str(util.symboldict[key]) == util.constant_name

def test_get_utility():
    # Test Case 1: Create a Cobb-Douglas utility function with two inputs.
    # Substitute valid values into the utility function and check that the
    # resulting utility function is correct.

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

    # Substitute vaid values into the utility function.
    u = util.get_utility(input_values=[1,1], constant=1)

    # Define expected utility.
    expected = 5

    # Check that the utility is correct.
    assert u == 5

def test_get_indifference():
    # Test Case 1: Create a Cobb-Douglas utility function with two inputs.
    # Do not explicitly pass values for the constant and the coefficients in
    # the get_indifference method. Check that the indifference curve is
    # correct.

    # Define number of inputs.
    num_inputs = 2

    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        exponent_values=(2,2),
        func_form='cobb-douglas'
    )

    # Define the expected indifference curve.
    expected = 'beta[0]*beta[1]*x[0]**2*x[1]**2'

    # Check that the indifference curve is correct.
    assert str(util.get_indifference()) == expected

    # Test Case 2: Create a Cobb-Douglas utility function with two inputs.
    # Explicitly pass values for the constant and the coefficients in the 
    # get_indifference method. Check that the indifference curve is correct.

    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        exponent_values=(2,2),
        func_form='cobb-douglas'
    )

    # Define the expected indifference curve.
    expected = 'beta[0]*beta[1]*x[0]**2*x[1]**2 + 2'

    # Check that the indifference curve is correct.
    assert str(util.get_indifference(constant=5, dependent=3)) == expected

    # Test Case 3: Create a Cobb-Douglas utility function with two inputs.
    # Explicitly pass negative values for the constant and the coefficients
    # in the get_indifference method. Check that the indifference curve is
    # correct.

    # Define the utility function.

    util = Utility(
        num_inputs=num_inputs,
        exponent_values=(2,2),
        func_form='cobb-douglas'
    )

    # Define the expected indifference curve.
    expected = 'beta[0]*beta[1]*x[0]**2*x[1]**2 - 2'

    # Check that the indifference curve is correct.
    assert str(util.get_indifference(constant=-5, dependent=-3)) == expected

def test_marginal_utility():
    # Test Case 1: Create a Cobb-Douglas utility function with two inputs.
    # Calculate the marginal utility for each input and check that the
    # marginal utility is correct.
    
    # Define number of inputs.
    num_inputs = 2
    
    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        exponent_values=(2,2),
        func_form='cobb-douglas'
    )

    # Define the expected marginal utility for indexed input 0.
    expected = '2*beta[0]*beta[1]*x[0]*x[1]**2'

    # Check that the marginal utility for indexed input 0 is correct.
    assert str(util.marginal_utility(indx=0)) == expected

    # Define the expected marginal utility for indexed input 1.
    expected = '2*beta[0]*beta[1]*x[0]**2*x[1]'

    # Check that the marginal utility for indexed input 1 is correct.
    assert str(util.marginal_utility(indx=1)) == expected

    # Test Case 2: Create a Cobb-Douglas utility function with two inputs.
    # Calculate the marginal rate of substitution as the ratio of the
    # marginal utility of indexed input 0 to the marginal utility of 
    # indexed input 1. Check that the marginal rate of substitution is
    # correct.

    # Define the utility function.
    util = Utility(
        num_inputs=num_inputs,
        exponent_values=(2,2),
        func_form='cobb-douglas'
    )

    # Define the marginal utility for indexed input 0.
    mu0 = util.marginal_utility(indx=0)

    # Define the marginal utility for indexed input 1.
    mu1 = util.marginal_utility(indx=1)

    # Define the expected marginal rate of substitution as mu0/mu1.
    expected = 'x[1]/x[0]'

    # Check that the marginal rate of substitution is correct.
    assert str(mu0/mu1) == expected