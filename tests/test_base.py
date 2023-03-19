import sympy as sp
import pytest
from econmodels.functional_forms.base import BaseForms

def test_init():
    # Test Case 1: Create a BaseForms object with no inputs. In test case 1,
    # we create a BaseForms object with no inputs. We then check that the
    # symbol_dict has the expected key values and that the key values are
    # equal to names passed into the BaseForms class.
    
    # Instantiate class to access init function.
    func_form = BaseForms(num_inputs=0)

    # Assert that the symbol_dict is an instance of a dictionary.
    assert isinstance(func_form.symbol_dict, dict)

    # Check that the symbol_dict has expected key values.
    assert all(key in func_form.symbol_dict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'exponent', 'input', 'i'
    ])

    # Check that the key values are equal to the names passed into the
    # BaseForms class.
    for key in func_form.symbol_dict.keys():
        if key == 'input':
            assert str(func_form.symbol_dict[key])  == func_form.input_name
        elif key == 'exponent':
            assert str(func_form.symbol_dict[key]) == func_form.exponent_name
        elif key == 'coefficient':
            assert str(func_form.symbol_dict[key]) == func_form.coeff_name
        elif key == 'dependent':
            assert str(func_form.symbol_dict[key]) == func_form.dependent_name
        elif key == 'constant':
            assert str(func_form.symbol_dict[key]) == func_form.constant_name

    # Test Case 2: Create a BaseForms object with two inputs. In test case 2,
    # we create a BaseForms object with two inputs. We then check that the
    # symbol_dict has the expected key values.

    # Instantiate class to access init function.
    func_form = BaseForms(num_inputs=2)

    # Assert that the symbol_dict is an instance of a dictionary.
    assert isinstance(func_form.symbol_dict, dict)

    # Check that the symbol_dict has expected key values.
    assert all(key in func_form.symbol_dict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'exponent', 'input', 'i'
    ])

    # Check that the key values are equal to the names passed into the
    # BaseForms class.
    for key in func_form.symbol_dict.keys():
        if key == 'input':
            assert str(func_form.symbol_dict[key])  == func_form.input_name
        elif key == 'exponent':
            assert str(func_form.symbol_dict[key]) == func_form.exponent_name
        elif key == 'coefficient':
            assert str(func_form.symbol_dict[key]) == func_form.coeff_name
        elif key == 'dependent':
            assert str(func_form.symbol_dict[key]) == func_form.dependent_name
        elif key == 'constant':
            assert str(func_form.symbol_dict[key]) == func_form.constant_name

    # Test Case 3: Create a BaseForms object with two inputs and custom names
    # for the symbols. In test case 3, we create a BaseForms object with two
    # inputs and custom names for the symbols. We then check that the
    # symbol_dict has the expected key values.
    
    # Instantiate class to access init function.
    func_form = BaseForms(
        num_inputs=2,
        input_name='x',
        exponent_name='e',
        coeff_name='c',
        dependent_name='y',
        constant_name='k'
    )

    # Assert that the symbol_dict is an instance of a dictionary.
    assert isinstance(func_form.symbol_dict, dict)

    # Check that the symbol_dict has expected key values.
    assert all(key in func_form.symbol_dict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'exponent', 'input', 'i'
    ])

    # Check that the key values are equal to the names passed into the
    # BaseForms class.
    for key in func_form.symbol_dict.keys():
        if key == 'input':
            assert str(func_form.symbol_dict[key])  == func_form.input_name
        elif key == 'exponent':
            assert str(func_form.symbol_dict[key]) == func_form.exponent_name
        elif key == 'coefficient':
            assert str(func_form.symbol_dict[key]) == func_form.coeff_name
        elif key == 'dependent':
            assert str(func_form.symbol_dict[key]) == func_form.dependent_name
        elif key == 'constant':
            assert str(func_form.symbol_dict[key]) == func_form.constant_name

    # Test Case 4: Create a BaseForms object with -1 inputs. In test case 3,
    # we create a BaseForms object with -1 inputs. We then check that an
    # exception is raised.

    # Instantiate class to access init function.
    with pytest.raises(Exception):
        func_form = BaseForms(num_inputs=-1)

def test_sub_values():
    # Test Case 1: Substituting with None values.
    # In test case 1, we substitute both symbols with None values, which should
    # replace them with tuples of ones. We then add these tuples and check that
    # the result matches what we expect.
    
    # Define number of inputs.
    num_inputs = 2

    # Define indexed symbol and index.
    x = sp.IndexedBase('x')
    i = sp.symbols('i', cls=sp.Idx)

    # Define function.
    f = (sp.Sum(x[i], (i, 0, num_inputs - 1))).doit()

    # Create substitutions list.
    sub_values = {x: None}

    # Create expected outcome.
    expected = sum([1]*num_inputs)

    # Instantiate class to access sub_values function.
    func_form = BaseForms()

    # Asset that the function returns expected results.
    assert func_form.sub_symbols(
        func=f,
        symbol_values=sub_values
    ) == expected

    # Test Case 2: Substituting with tuple values.
    # In test case 2, we substitute both symbols with tuples of values, which
    # should replace them with the corresponding values. We then square these
    # values and add them together, and check that the result matches what we
    # expect.

    # Define another indexed symbol.
    beta = sp.IndexedBase('beta')

    # Define function.
    f = (sp.Sum(beta[i]*x[i]**2, (i, 0, num_inputs - 1))).doit()

    # Create substitutions list.
    sub_x = tuple(range(1, 1 + num_inputs)) # Test case values.
    sub_beta = tuple(range(1 + num_inputs, 3 + num_inputs)) # Test case values.
    sub_values = {
        x: sub_x,
        beta: sub_beta
    }

    # Create expected outcome.
    expected = sum([sub_beta[i]*sub_x[i]**2 for i in range(num_inputs)])

    # Instantiate class to access sub_values function.
    func_form = BaseForms()

    # Asset that the function returns expected results.
    assert func_form.sub_symbols(
        func=f,
        symbol_values=sub_values
     ) == expected
    
    # Test Case 3: Substituting with a mixture of values and None.
    # In test case 3, we substitute one symbol with a None value and the other
    # with a tuple of values. We then add these values together and check that
    # the result matches what we expect.

    # Define function.
    f = (sp.Sum(beta[i]*x[i]**2, (i, 0, num_inputs - 1))).doit()
    
    # Create substitutions list.
    sub_x = None # Test case values.
    sub_beta = tuple(range(1 + num_inputs, 3 + num_inputs)) # Test case values.
    sub_values = {
        x: sub_x,
        beta: sub_beta
    }

    # Create expected outcome.
    expected = sum([sub_beta[i]*1 for i in range(num_inputs)])

    # Instantiate class to access sub_values function.
    func_form = BaseForms()

    # Asset that the function returns expected results.
    assert func_form.sub_symbols(
        func=f,
        symbol_values=sub_values
    ) == expected

    # Test Case 4: Substituting with an empty list.
    # In test case 4, we substitute symbols with an empty list. The result
    # is the function returned unchanged.

    # Define function.
    f = (sp.Sum(beta[i]*x[i]**2, (i, 0, num_inputs - 1))).doit()

    # Create substitutions list.
    sub_values = {}

    # Instantiate class to access sub_values function.
    func_form = BaseForms()

    # Define the function and check for an error.
    expected = f

    assert func_form.sub_symbols(
        func=f,
        symbol_values=sub_values
    ) == expected

    # Test Case 5: Substituting with no values.
    # In test case 5, we don't substitute any symbols with values, so an error
    # should occur. Not sure I want to intervene to fix this. I feel like this
    # should not be an error, but what's the use case of passing empty tuple?

    # Define function.
    f = (sp.Sum(beta[i]*x[i]**2, (i, 0, num_inputs - 1))).doit()

    # Create substitutions list.
    sub_x = () # Test case values.
    sub_beta = () # Test case values.
    sub_values = {
        x: sub_x,
        beta: sub_beta
    }

    # Create expected outcome.
    expected = f

    # Instantiate class to access sub_values function.
    func_form = BaseForms()

    # Define the function and check for an error.
    with pytest.raises(IndexError):
        func_form.sub_symbols(
            func=f,
            symbol_values=sub_values
        ) == expected

    # Test Case 6: Substituting with a function that doesn't contain the
    # symbols.
    # In test case 6, we substitute symbols that aren't present in the function,
    # so the function return an error since the symbols are not in the
    # symbol_dict.

    # Define function.
    f = (sp.Sum(beta[i]*x[i]**2, (i, 0, num_inputs - 1))).doit()

    # Create substitutions list.
    sub_values = {
        sp.symbols('a'): None,
        sp.symbols('b'): None
    }

    # Instantiate class to access sub_values function.
    func_form = BaseForms()

    # Define the function and check for an error.
    with pytest.raises(Exception):
        func_form.sub_values(
            func=f,
            symbol_values=sub_values
        )

    # Test Case 7: Substituting None type.
    # In test case 7, we substitute symbols with None type. The result
    # is the function returns an error.

    # Define function.
    f = (sp.Sum(beta[i]*x[i]**2, (i, 0, num_inputs - 1))).doit()

    # Create substitutions list.
    sub_values = None

    # Instantiate class to access sub_values function.
    func_form = BaseForms()

    # Define the function and check for an error.
    with pytest.raises(AttributeError):
        func_form.sub_symbols(
            func=f,
            symbol_values=sub_values
        )

def test_additive():
    # Teat Case 1:
    # Test case for basic functionality: Check whether the function returns a
    # valid mathematical function and a dictionary of symbols and indexes when
    # passed valid input values.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3),
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=1
    )

    # Define the mathematical function.
    func_form, symbol_dict = function.additive()

    # Define expected outcome.
    expected = 'c + 2*x[0] + 3*x[1]**2 - 1'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected

    # Test Case 2:
    # Test case for a different number of inputs: Check whether the function
    # returns a valid mathematical function and a dictionary of symbols and
    # indexes when passed a different number of inputs.
    function = BaseForms(
        num_inputs=3,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3, 4),
        exponent_name='b',
        exponent_values=(1, 2, 3),
        constant_name='c',
        dependent_name='y',
    )

    # Define the mathematical function.
    func_form, symbol_dict = function.additive()

    # Define expected outcome.
    expected = 'c - y + 2*x[0] + 3*x[1]**2 + 4*x[2]**3'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected

    # Test Case 3:
    # Test case for zero inputs. This should return a function where the inputs
    # are effectively 0, leaving only the constants and the dependent.
    function = BaseForms(
        num_inputs=0, # Test case values.
        input_name='x',
        coeff_name='a',
        coeff_values=(),
        exponent_name='b',
        exponent_values=(),
        constant_name='c',
        dependent_name='y'
    )

    # Define the mathematical function.
    func_form, symbol_dict = function.additive()

    # Define the expected outcome.
    expected = "c - y"

    # Assert that the string version fo the mathematical function equals
    # expected outcome.
    assert str(func_form) == expected

    # Test Case 4:
    # Test case for invalid input: Check whether the function raises an
    # AttributeError when a tuple is passed to substitute a Sympy symbol.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3),
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=(1,2) # Test case values.
    )

    # Define the function and check for an error.
    with pytest.raises(AttributeError):
        function.additive()

    # Test Case 5:
    # Test case for invalid input: Check whether the function raises an
    # TypeError when an integer is passed to substitute an IndexedBase
    # instance.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=1, # Test case value.
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=1
    )

    # Define the function and check for an error.
    with pytest.raises(TypeError):
        function.additive()

def test_multiplicative():
    # Teat Case 1:
    # Test case for basic functionality: Check whether the function returns a
    # valid mathematical function and a dictionary of symbols and indexes when
    # passed valid input values.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3),
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=1
    )

    # Define mathematical function.
    func_form, symbol_dict = function.multiplicative()

    # Define expected outcome.
    expected = 'c + 6*x[0]*x[1]**2 - 1'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected

    # Test Case 2:
    # Test case for a different number of inputs: Check whether the function
    # returns a valid mathematical equation and a dictionary of symbols and
    # indexes when passed a different number of inputs.
    function = BaseForms(
        num_inputs=3,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3, 4),
        exponent_name='b',
        exponent_values=(1, 2, 3),
        constant_name='c',
        dependent_name='y',
    )

    # Define the mathematical function.
    func_form, symbol_dict = function.multiplicative()

    # Define expected outcome.
    expected = 'c - y + 24*x[0]*x[1]**2*x[2]**3'

    # Assert that the string function is equal to the expected function.
    assert str(func_form) == expected

    # Test Case 3:
    # Test case for zero inputs: Check whether the function returns a valid
    # mathematical function and a dictionary of symbols and indexes when passed
    # zero inputs.
    function = BaseForms(
        num_inputs=0,
        input_name='x',
        coeff_name='a',
        coeff_values=(),
        exponent_name='b',
        exponent_values=(),
        constant_name='c',
        dependent_name='y'
    )

    # Define the mathematical function.
    func_form, symbol_dict = function.multiplicative()

    # Define expected outcome.
    expected = 'c - y + 1'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected
    
    # Test Case 4:
    # Test case for invalid input: Check whether the function raises an
    # AttributeError when a tuple is passed to substitute a Sympy symbol.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3),
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=(1,2) # Test case values.
    )

    # Define the function and check for an error.
    with pytest.raises(AttributeError):
        function.multiplicative()

    # Test Case 5:
    # Test case for invalid input: Check whether the function raises an
    # TypeError when an integer is passed to substitute an IndexedBase
    # instance.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=1, # Test case value.
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=1
    )

    # Define the function and check for an error.
    with pytest.raises(TypeError):
        function.multiplicative()

def test_minimum_function():
    # Teat Case 1:
    # Test case for basic functionality: Check whether the function returns a
    # valid mathematical function and a dictionary of symbols and indexes when
    # passed valid input values.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3),
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=1
    )

    # Define the mathematical function.
    func_form, symbol_dict = function.minimum_function()

    # Define expected outcome.
    expected = 'Min(2*x[0], 3*x[1]) - 1'

    # Assert that the string version of the mathematical function is equal to 
    # the expected function.
    assert str(func_form) == expected

    # Test Case 2:
    # Test case for a different number of inputs: Check whether the function
    # returns a valid mathematical equation and a dictionary of symbols and
    # indexes when passed a different number of inputs.
    function = BaseForms(
        num_inputs=3,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3, 4),
        exponent_name='b',
        exponent_values=(1, 2, 3),
        constant_name='c',
        dependent_name='y',
    )

    # Define mathematical function.
    func_form, symbol_dict = function.minimum_function()

    # Define expected outcome.
    expected = '-y + Min(2*x[0], 3*x[1], 4*x[2])'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected

    # Test Case 3:
    # Test case for zero inputs: Check whether the function returns a valid
    # mathematical equation and a dictionary of symbols and indexes when passed
    # zero inputs.
    function = BaseForms(
        num_inputs=0,
        input_name='x',
        coeff_name='a',
        coeff_values=(),
        exponent_name='b',
        exponent_values=(),
        constant_name='c',
        dependent_name='y'
    )

    # Define mathematical function.
    func_form, symbol_dict = function.minimum_function()

    # Define expected outcome.
    expected = '-y + oo'

    # Assert that the string function is equal to the expected function.
    assert str(func_form) == expected

    # Test Case 4:
    # Test case for invalid input: Check whether the function raises an
    # AttributeError when a tuple is passed to substitute a Sympy symbol.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3),
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=(1,2) # Test case values.
    )

    # Define the function and check for an error.
    with pytest.raises(AttributeError):
        function.minimum_function()

    # Test Case 5:
    # Test case for invalid input: Check whether the function raises an
    # TypeError when an integer is passed to substitute an IndexedBase
    # instance.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=1, # Test case value.
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=1
    )

    # Define the function and check for an error.
    with pytest.raises(TypeError):
        function.minimum_function()

def test_ces():
    # Teat Case 1:
    # Test case for basic functionality: Check whether the function returns a
    # valid mathematical equation and a dictionary of symbols and indexes when
    # passed valid input values.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3),
        exponent_name='b',
        exponent_values=1,
        constant_name='c',
        dependent_name='y',
        dependent_value=1
    )

    # Define the mathematical function.
    func_form, symbol_dict = function.ces()

    # Define expected outcome.
    expected = 'c + 2*x[0] + 3*x[1] - 1'

    # Assert that the string function is equal to the expected function.
    assert str(func_form) == expected

    # Test Case 2:
    # Test case for a different number of inputs: Check whether the function
    # returns a valid mathematical equation and a dictionary of symbols and
    # indexes when passed a different number of inputs.
    function = BaseForms(
        num_inputs=3,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3, 4),
        exponent_name='b',
        exponent_values=2,
        constant_name='c',
        dependent_name='y',
    )

    # Define the mathematical function.
    func_form, symbol_dict = function.ces()

    # Define expected outcome.
    expected = 'c - y + sqrt(2*x[0]**2 + 3*x[1]**2 + 4*x[2]**2)'

    # Assert that the string function is equal to the expected function.
    assert str(func_form) == expected

    # Test Case 3:
    # Test case for invalid input: Check whether the function raises an
    # AttributeError when a tuple is passed to substitute a Sympy symbol.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=(2, 3),
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=(1,2) # Test case values.
    )

    # Define the function and check for an error.
    with pytest.raises(AttributeError):
        function.ces()

    # Test Case 4:
    # Test case for invalid input: Check whether the function raises an
    # TypeError when an integer is passed to substitute an IndexedBase
    # instance.

    # Instantiate class with arguments.
    function = BaseForms(
        num_inputs=2,
        input_name='x',
        coeff_name='a',
        coeff_values=1, # Test case value.
        exponent_name='b',
        exponent_values=(1, 2),
        constant_name='c',
        dependent_name='y',
        dependent_value=1
    )

    # Define the function and check for an error.
    with pytest.raises(TypeError):
        function.ces()