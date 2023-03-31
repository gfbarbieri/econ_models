import sympy as sp

def is_linear(func):
    """
    Check if the functional form is linear.

    Returns
    -------
    bool
        True if the functional form is linear, False otherwise.

    """

    # Check if the functional form is linear by taking the second derivative
    # of each input with respect to all other inputs.
    vars = [func.symbol_dict['input'][i] for i in range(func.num_inputs)]

    for p in vars:
        for c in vars:
            if sp.diff(func.function, p, c) != 0:
                return False
            else:
                return True

def lagrangian(objective, constraint):
    """
    Solve the model using the Langrangian method. Currently only accepts
    a single objective function and a single constraint function.

    Parameters
    ----------
    objective : object
        An instance of the BaseForms class which includes a function and
        a dictionary of symbols.

    constraint : object
        An instance of the BaseForms class which includes a function and
        a dictionary of symbols.

    Returns
    -------
    solution : dict
        Solution to the model.

    """
    
    # Create a list of the inputs and lambda as symbols.
    l = sp.symbols('lambda')
    vars = [objective.symbol_dict['input'][i] for i in range(objective.num_inputs)] + [l]

    # Solve for utility in terms of the other variables and values.
    o = sp.solve(
        objective.function,
        objective.symbol_dict['dependent']
    )[0]

    # Define the Lagrangian: `U(x_i) - \lambda*(B(x_i) - M)`.
    L = o - l * constraint.function

    # Find first order conditions for each input and lambda.
    foc = [sp.diff(L, var) for var in vars]

    # Solve for the optimal values of goods and lambda.
    opt_values_dict = sp.solve(foc, tuple(vars), dict=True)[0]

    return opt_values_dict