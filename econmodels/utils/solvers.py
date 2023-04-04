import sympy as sp

def is_linear(func, quasi=False):
    """
    Check if the functional form is linear.

    Returns
    -------
    bool
        True if the functional form is linear, False otherwise.

    """

    # Check if the functional form is linear by taking the second
    # derivative of each input with respect to all inputs. If the second
    # derivative of the function with respect to any input is not zero, the
    # store False, else store True. 
    vars = [func.symbol_dict['inputs'][i] for i in range(func.num_inputs)]

    linear_vars = []
    for p in vars:
        for c in vars:
            if sp.diff(func.function, p, c) != 0:
                linear_vars.append(False)
            else:
                linear_vars.append(True)

    if not quasi:
        # A linear function will have all True values.
        if all(linear_vars):
            return True
        else:
            return False
    else:
        # A quasi-linear function will have a mix of True and False.
        if True in linear_vars and False in linear_vars:
            return True
        else:
            return False

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
    l = sp.symbols('lambda', real=True, nonnegative=True)
    vars = [objective.symbol_dict['inputs'][i] for i in range(objective.num_inputs)] + [l]

    # Solve for utility in terms of the other variables and values.
    o = sp.solve(
        objective.function,
        objective.symbol_dict['dependent']
    )[0]

    # Define the Lagrangian: `U(x_i) - \lambda*(B(x_i) - M)`.
    L = o - l * constraint.function

    # Find first order conditions for each input and lambda. Store as a
    # dictionary of equations. The key is the variable the derivative of the
    # Lagrangian was calculated with respect to. The value is the derivative
    # of the Langrangian with respect to the variable set equal to zero.
    foc = {}
    for var in vars:
        foc[var] = sp.Eq(sp.diff(L, var), 0)

    # If the utility function is linear, we face an indeterminate (corner) 
    # solution, as the consumer is indifferent along the budget constraint. The
    # marginal rate of substitution (MRS) between the goods is constant and does
    # not depend on the quantities consumed. In that case, compare the utility
    # per dollar for each good. If comparable, return the demand function for
    # the good with the highest utility per dollar. If an equation, symbols, or
    # or equal, return a piecewise function with the conditions for choosing
    # each good.
    if is_linear(objective):  
        # Calculate the utility per dollar for each input as the ratio of the
        # derivative of the utility function with respect to the input to the
        # price of the input. The price of the input is the coefficient of the
        # input in the constraint function. Since the price of the input can
        # be either a number of a symbol, it's easier to find it by calculating
        # the derivative of the constraint function with respect to the input.
        u_p_d = {}

        for var in vars:
            sol = sp.solve(foc[var], l)

            if len(sol) == 1:
                u_p_d[var] = sol[0]

        # If utility per dollar are all numbers, then return the demand for the
        # good with the highest utility per dollar and zero for the other good.
        if all([x.is_number for x in list(u_p_d.values())]):
            print("Return the demand for the good with the highest utility per \
                  dollar and zero for the other goods.")
            
            # Find the input with the highest utility per dollar.
            max_u_p_d = max(u_p_d, key=u_p_d.get)

            # Create optimal values dictionary where the key is the input and
            # the value is the optimal quantity of the input. The input with
            # the highest utility per dollar is set equal to the income divided
            # by the price of the input. The other inputs are set equal to zero.
            opt_values_dict = {}
            for var in list(u_p_d.keys()):
                if var == max_u_p_d:
                    if constraint.dependent_value == 'symbols':
                        opt_values_dict[var] = constraint.symbol_dict['dependent'] / var
                    else:
                        opt_values_dict[var] = constraint.dependent_value / var
                else:
                    opt_values_dict[var] = 0
        else:
            print("Return a piecewise function with the conditions for choosing \
                  each good.")
            # Create the piecewise demand functions for each input. The
            # conditions are the utility per dollar for each input. If the
            # utility per dollar for the first input is greater than the maximum
            # utility per dollar for the other inputs, then the demand for the
            # first input is equal to the income divided by the price of the
            # first input. Otherwise, the demand for the first input is zero.
            # The same logic applies to all other inputs.
            opt_values_dict = {}
            for var in list(u_p_d.keys()):
                opt_values_dict[var] = sp.Piecewise(
                    (constraint.symbol_dict['dependent'] / var, u_p_d[var] >= sp.Max(*u_p_d.values())), (0, True)
                )

        return opt_values_dict
    # If the utility function is not linear, solve for the optimal values of
    # the inputs and lambda. If the solution is too complex for a general
    # symbolic solver, raise an error. This is a limitation of SymPy and
    # algebraic solvers generally.
    try:
        opt_values_dict = sp.solve(foc, tuple(vars), dict=True)[0]
        
        return opt_values_dict
    except NotImplementedError as e:
        print(e)
        print("The solution is too complex for a general symbolic solver. \
              Try making the problem simplier by replacing symbols, \
              especialliy exponents with numeric values.")
          