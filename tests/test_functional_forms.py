import sympy as sp
import pytest
from econmodels.agent_functions.functional_forms import FunctionalForms

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
    sub_values = [[x, None]]

    # Create expected outcome.
    expected = sp.Add(*tuple([1]*num_inputs))

    # Instantiate class to access sub_values function.
    func_form = FunctionalForms()

    # Asset that the function returns expected results.
    assert func_form.sub_values(num_inputs, f, sub_values) == expected
    
    # Test Case 2: Substituting with tuple values.
    # In test case 2, we substitute both symbols with tuples of values, which
    # should replace them with the corresponding values. We then square these
    # values and add them together, and check that the result matches what we
    # expect.

    # Define another indexed symbol.
    y = sp.IndexedBase('y')

    # Define function.
    f = (sp.Sum(x[i]**2 + y[i]**2, (i, 0, num_inputs - 1))).doit()

    # Create substitutions list.
    sub_x = tuple(range(1, 1 + num_inputs))
    sub_y = tuple(range(1 + num_inputs, 3 + num_inputs))
    sub_values = [[x, sub_x], [y, sub_y]]

    # Create expected outcome.
    expected = sp.Add(
        sp.Add(*tuple([sp.Pow(x, 2) for x in sub_x])),
        sp.Add(*tuple([sp.Pow(y, 2) for y in sub_y]))
    )

    # Instantiate class to access sub_values function.
    func_form = FunctionalForms()

    # Asset that the function returns expected results.
    assert func_form.sub_values(num_inputs, f, sub_values) == expected
    
    # Test Case 3: Substituting with a mixture of values and None.
    # In test case 3, we substitute one symbol with a None value and the other
    # with a tuple of values. We then add these values together and check that
    # the result matches what we expect.

    # Define function.
    f = (sp.Sum(x[i] + y[i], (i, 0, num_inputs - 1))).doit()
    
    # Create substitutions list.
    sub_y = tuple(range(1, 1 + num_inputs))
    sub_values = [[x, None], [y, sub_y]]
    
    # Create expected outcome.
    expected = sp.Add(sp.Mul(1*num_inputs), sp.Add(*sub_y))

    # Instantiate class to access sub_values function.
    func_form = FunctionalForms()

    # Asset that the function returns expected results.
    assert func_form.sub_values(num_inputs, f, sub_values) == expected
    
    # Test Case 4: Substituting with no values.
    # In test case 4, we don't substitute any symbols with values, so the
    # function should be returned unchanged.
    
    # Define function.
    f = (sp.Sum(x[i] + y[i], (i, 0, num_inputs - 1))).doit()
    
    # Create substitutions list.
    sub_values = []

    # Create expected outcome.
    expected = (sp.Sum(x[i] + y[i], (i, 0, num_inputs - 1))).doit()
    
    # Instantiate class to access sub_values function.
    func_form = FunctionalForms()

    # Asset that the function returns expected results.
    assert func_form.sub_values(num_inputs, f, sub_values) == expected

    # Test Case 5: Substituting with a function that doesn't contain the
    # symbols.
    # In test case 5, we substitute symbols that aren't present in the function,
    # so the function should be returned unchanged.

    # Define function.
    f = (sp.Sum(x[i] + y[i], (i, 0, num_inputs - 1))).doit()
    
    # Create substitutions list.
    sub_values = [[sp.symbols('a'), None], [sp.symbols('b'), None]]
    
    # Create expected outcome.
    expected = (sp.Sum(x[i] + y[i], (i, 0, num_inputs - 1))).doit()
    
    # Instantiate class to access sub_values function.
    func_form = FunctionalForms()

    # Asset that the function returns expected results.
    assert func_form.sub_values(num_inputs, f, sub_values) == expected

def test_polynomial_combination():
    # Teat Case 1:
    # Test case for basic functionality: Check whether the function returns a
    # valid mathematical function and a dictionary of symbols and indexes when
    # passed valid input values.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
    func_form, symboldict = function.polynomial_combination()

    # Define expected outcome.
    expected = 'c + 2*x[0] + 3*x[1]**2 - 1'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected

    # Assert that the symboldict is an instance of a dictionary.
    assert isinstance(symboldict, dict)

    # Check that the symboldict has expected key values.
    assert all(key in symboldict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'exponent', 'input', 'i'
    ])

    # Test Case 2:
    # Test case for a different number of inputs: Check whether the function
    # returns a valid mathematical function and a dictionary of symbols and
    # indexes when passed a different number of inputs.
    function = FunctionalForms(
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
    func_form, symboldict = function.polynomial_combination()

    # Define expected outcome.
    expected = 'c - y + 2*x[0] + 3*x[1]**2 + 4*x[2]**3'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected

    # Test Case 3:
    # Test case for zero inputs: Check whether the function returns a valid
    # mathematical function and a dictionary of symbols and indexes when passed
    # zero inputs.
    function = FunctionalForms(
        num_inputs=0,
        input_name='x',
        coeff_name='a',
        coeff_values=(), # Test case values.
        exponent_name='b',
        exponent_values=(), # Test case values.
        constant_name='c',
        dependent_name='y'
    )

    # Define the mathematical function.
    func_form, symboldict = function.polynomial_combination()

    # Define the expected outcome.
    expected = "c - y"

    # Assert that the string version fo the mathematical function equals
    # expected outcome.
    assert str(func_form) == expected

    # Test Case 4:
    # Test case for invalid input: Check whether the function raises an
    # AttributeError when a tuple is passed to substitute a Sympy symbol.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
        function.polynomial_combination()

    # Test Case 5:
    # Test case for invalid input: Check whether the function raises an
    # TypeError when an integer is passed to substitute an IndexedBase
    # instance.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
        function.polynomial_combination()

def test_cobb_douglas():
    # Teat Case 1:
    # Test case for basic functionality: Check whether the function returns a
    # valid mathematical function and a dictionary of symbols and indexes when
    # passed valid input values.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
    func_form, symboldict = function.cobb_douglas()

    # Define expected outcome.
    expected = 'c + 6*x[0]*x[1]**2 - 1'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected

    # Assert that the symboldict is an instance of a dictionary.
    assert isinstance(symboldict, dict)

    # Check that the symboldict has expected key values.
    assert all(key in symboldict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'input', 'exponent', 'i'
    ])

    # Test Case 2:
    # Test case for a different number of inputs: Check whether the function
    # returns a valid mathematical equation and a dictionary of symbols and
    # indexes when passed a different number of inputs.
    function = FunctionalForms(
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
    func_form, symboldict = function.cobb_douglas()

    # Define expected outcome.
    expected = 'c - y + 24*x[0]*x[1]**2*x[2]**3'

    # Assert that the string function is equal to the expected function.
    assert str(func_form) == expected

    # Test Case 3:
    # Test case for zero inputs: Check whether the function returns a valid
    # mathematical function and a dictionary of symbols and indexes when passed
    # zero inputs.
    function = FunctionalForms(
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
    func_form, symboldict = function.cobb_douglas()

    # Define expected outcome.
    expected = 'c - y + 1'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected
    
    # Test Case 4:
    # Test case for invalid input: Check whether the function raises an
    # AttributeError when a tuple is passed to substitute a Sympy symbol.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
        function.cobb_douglas()

    # Test Case 5:
    # Test case for invalid input: Check whether the function raises an
    # TypeError when an integer is passed to substitute an IndexedBase
    # instance.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
        function.cobb_douglas()

def test_substitutes():
    # Teat Case 1:
    # Test case for basic functionality: Check whether the function returns a
    # valid mathematical function and a dictionary of symbols and indexes when
    # passed valid input values.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
    func_form, symboldict = function.substitutes()

    # Define expected outcome.
    expected = 'c + 2*x[0] + 3*x[1] - 1'

    # Assert that the string version of the mathematical is equal to the 
    # expected function.
    assert str(func_form) == expected

    # Assert that the symboldict is an instance of a dictionary.
    assert isinstance(symboldict, dict)

    # Check that the symboldict has expected key values.
    assert all(key in symboldict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'input', 'exponent', 'i'
    ])

    # Test Case 2:
    # Test case for a different number of inputs: Check whether the function
    # returns a valid mathematical function and a dictionary of symbols and
    # indexes when passed a different number of inputs.
    function = FunctionalForms(
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
    func_form, symboldict = function.substitutes()

    # Define expected outcome.
    expected = 'c - y + 2*x[0] + 3*x[1] + 4*x[2]'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected

    # Test Case 3:
    # Test case for zero inputs: Check whether the function returns a valid
    # mathematical function and a dictionary of symbols and indexes when passed
    # zero inputs.
    function = FunctionalForms(
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
    func_form, symboldict = function.substitutes()

    # Define expected outcome.
    expected = 'c - y'

    # Assert that the string version of the mathematical function is equal to 
    # the expected function.
    assert str(func_form) == expected

    # Test Case 4:
    # Test case for invalid input: Check whether the function raises an
    # AttributeError when a tuple is passed to substitute a Sympy symbol.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
        function.substitutes()

    # Test Case 5:
    # Test case for invalid input: Check whether the function raises an
    # TypeError when an integer is passed to substitute an IndexedBase
    # instance.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
        function.substitutes()

def test_complements():
    # Teat Case 1:
    # Test case for basic functionality: Check whether the function returns a
    # valid mathematical function and a dictionary of symbols and indexes when
    # passed valid input values.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
    func_form, symboldict = function.complements()

    # Define expected outcome.
    expected = 'Min(x[0], x[1]) - 1'

    # Assert that the string version of the mathematical function is equal to 
    # the expected function.
    assert str(func_form) == expected

    # Assert that the symboldict is an instance of a dictionary.
    assert isinstance(symboldict, dict)

    # Check that the symboldict has expected key values.
    assert all(key in symboldict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'input', 'exponent', 'i'
    ])

    # Test Case 2:
    # Test case for a different number of inputs: Check whether the function
    # returns a valid mathematical equation and a dictionary of symbols and
    # indexes when passed a different number of inputs.
    function = FunctionalForms(
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
    func_form, symboldict = function.complements()

    # Define expected outcome.
    expected = '-y + Min(x[0], x[1], x[2])'

    # Assert that the string version of the mathematical function is equal to
    # the expected function.
    assert str(func_form) == expected

    # Test Case 3:
    # Test case for zero inputs: Check whether the function returns a valid
    # mathematical equation and a dictionary of symbols and indexes when passed
    # zero inputs.
    function = FunctionalForms(
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
    func_form, symboldict = function.complements()

    # Define expected outcome.
    expected = '-y + oo'

    # Assert that the string function is equal to the expected function.
    assert str(func_form) == expected

    # Test Case 4:
    # Test case for invalid input: Check whether the function raises an
    # AttributeError when a tuple is passed to substitute a Sympy symbol.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
        function.substitutes()

    # Test Case 5:
    # Test case for invalid input: Check whether the function raises an
    # TypeError when an integer is passed to substitute an IndexedBase
    # instance.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
        function.substitutes()

def test_ces():
    # Teat Case 1:
    # Test case for basic functionality: Check whether the function returns a
    # valid mathematical equation and a dictionary of symbols and indexes when
    # passed valid input values.

    # Instantiate class with arguments.
    function = FunctionalForms(
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
    func_form, symboldict = function.ces()

    # Define expected outcome.
    expected = 'c + 2*x[0] + 3*x[1] - 1'

    # Assert that the string function is equal to the expected function.
    assert str(func_form) == expected

    # Assert that the symboldict is an instance of a dictionary.
    assert isinstance(symboldict, dict)

    # Check that the symboldict has expected key values.
    assert all(key in symboldict.keys() for key in [
        'coefficient', 'constant', 'dependent',
        'input', 'exponent', 'i'
    ])

    # Test Case 2:
    # Test case for a different number of inputs: Check whether the function
    # returns a valid mathematical equation and a dictionary of symbols and
    # indexes when passed a different number of inputs.
    function = FunctionalForms(
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
    func_form, symboldict = function.ces()

    # Define expected outcome.
    expected = 'c - y + sqrt(2*x[0]**2 + 3*x[1]**2 + 4*x[2]**2)'

    # Assert that the string function is equal to the expected function.
    assert str(func_form) == expected

    # Test Case 3:
    # Test case for zero inputs: Check whether the function raises an error
    # for the CES function if exponent values are empty.
    function = FunctionalForms(
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
    with pytest.raises(TypeError):
        function.ces()

    # Test Case 4:
    # Test case for invalid input: Check whether the function raises an
    # AttributeError when a tuple is passed to substitute a Sympy symbol.

    # Instantiate class with arguments.
    function = FunctionalForms(
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

    # Test Case 5:
    # Test case for invalid input: Check whether the function raises an
    # TypeError when an integer is passed to substitute an IndexedBase
    # instance.

    # Instantiate class with arguments.
    function = FunctionalForms(
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