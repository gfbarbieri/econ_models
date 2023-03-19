# Overview

Econmodels is an open source library for exploring the core concepts of economics. The framework integrates a market structure with market actors and their decision functions. The module is built on top of Sympy, allowing symbolic logic for generalized examples as well as numeric examples.

## Example Using Functional Forms

Functional forms of common mathematical functions used in economics are avaialble, including Cobb-Douglas and CES functions. There is no particular limit on what other functional forms can be added to the list.

Import `Utility` which gives you access to several fucntional forms of utility functions, including Cobb-Douglas, substitutes, complements, CES, and quasi-linear.


```python
from econmodels.functional_forms.utility import Utility
```

Instantiate the `Utility` class with the functional form of a Cobb-Douglas function.


```python
utility = Utility(func_form='cobb-douglas')
```

Print the utility function.


```python
utility.function
```




$$C - U + {\beta}_{0} {\beta}_{1} {x}_{0}^{{\alpha}_{0}} {x}_{1}^{{\alpha}_{1}}$$



Print the symbols available.


```python
utility.symboldict
```




    {'coefficient': beta,
     'constant': C,
     'dependent': U,
     'exponent': alpha,
     'i': i,
     'input': x}



Print marginal utility of $x_0$, $\frac{\partial U}{\partial x_0}$.


```python
utility.marginal_utility(indx=0).simplify()
```




$${\alpha}_{0} {\beta}_{0} {\beta}_{1} {x}_{0}^{{\alpha}_{0} - 1} {x}_{1}^{{\alpha}_{1}}$$



Print marginal utility of $x_0$ with substitutions.


```python
subs = [
    ['coefficient', (1,2)],
    ['exponent', (1,2)]
]

utility.marginal_utility(indx=0, subs=subs).simplify()
```




$$2 {x}_{1}^{2}$$



Get total utility by substituting values for the goods.


```python
utility.get_utility(input_values=[1,4], constant=None)
```




$$4^{{\alpha}_{1}} {\beta}_{0} {\beta}_{1} + 1$$



## Example using Agents

Agents are usually a combination of a objective function and a constriant function. Agents are also usually given additional methods to maximize the objective given constraints.

Import the agent `Consumer`, which is a combination of a utility function and a budget constraint. 


```python
from econmodels.agents.consumer import Consumer
```

Instantiate the `Consumer` class.


```python
consumer = Consumer()
```

Print the consumers property `utility`. The default utility function is a Cobb-Douglas utility with two goods.


```python
consumer.utility.function
```




$$C - U + {\beta}_{0} {\beta}_{1} {x}_{0}^{{\alpha}_{0}} {x}_{1}^{{\alpha}_{1}}$$



Print the consumers property `budget_constraint`.


```python
consumer.constraint.function
```




$$B - M + {p_{}}_{0} {x}_{0} + {p_{}}_{1} {x}_{1}$$



Maximize utility given the budget constraint. The result populates the property `opt_values_dict`.


```python
consumer.maximize_utility()
```

Print optimal values dictionary.


```python
consumer.opt_values_dict
```




    {x[0]: (-B + M)*alpha[0]/((alpha[0] + alpha[1])*p_[0]),
     lambda: ((-B + M)*alpha[0]/((alpha[0] + alpha[1])*p_[0]))**alpha[0]*((-B + M)*alpha[1]/((alpha[0] + alpha[1])*p_[1]))**alpha[1]*(alpha[0] + alpha[1])*beta[0]*beta[1]/(B - M),
     x[1]: (-B + M)*alpha[1]/((alpha[0] + alpha[1])*p_[1])}



Show the demand for input $x_0$ as a homogenous equation.


```python
consumer.get_demand(indx=0)
```




$$\frac{\left(- B + M\right) {\alpha}_{0}}{\left({\alpha}_{0} + {\alpha}_{1}\right) {p_{}}_{0}} - {x}_{0}$$



Calculate price elasticity of quantity demanded for good 0.


```python
consumer.get_elasticity(input_indx=0, var='p_', var_indx=0)
```




$$- \frac{\left(- B + M\right) {\alpha}_{0} p_{}}{\left({\alpha}_{0} + {\alpha}_{1}\right) {p_{}}_{0}^{2} {x}_{0}}$$



Calculate income elasticity of quantity demanded for good 0.


```python
consumer.get_elasticity(input_indx=0, var='M', var_indx=0)
```




$$\frac{M {\alpha}_{0}}{\left({\alpha}_{0} + {\alpha}_{1}\right) {p_{}}_{0} {x}_{0}}$$



Calculate price elasticity of quantity demanded for good 0 at a point
where the price of good 0 is equal to quantity demanded.


```python
consumer.get_elasticity(input_indx=0, var='p_', var_indx=0, point=(1,1))
```




$$- \frac{\left(- B + M\right) {\alpha}_{0}}{\left({\alpha}_{0} + {\alpha}_{1}\right) {p_{}}_{0}^{2}}$$



Calculate cross-price elasticity of quantity demanded for good 0 with
respect to the price of good 1.


```python
consumer.get_elasticity(input_indx=0, var='p_', var_indx=1)
```




$$0$$


