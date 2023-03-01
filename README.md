# Overview

EconModels is an open source library for exploring the core concepts of economics. The framework integrates a market structure with market actors and their decision functions. The module is built on top of Sympy, allowing symbolic logic for generalized examples as well as numeric examples.

## Example Using Agent Properties

Import the property `Utility`.


```python
from econmodels.properties.utility import Utility
```

Instantiate the `Utility` class.


```python
utility = Utility()
```

Print the utility function.


```python
utility.function
```




$$- U + {\beta}_{0} {\beta}_{1} {x}_{0}^{{\alpha}_{0}} {x}_{1}^{{\alpha}_{1}}$$



Print the symbols available.


```python
utility.symbol_dict
```




    {'dependent': U, 'input': x, 'coeff': beta, 'exponent': alpha, 'i': i}



## Example Using Economic Agents

Import the economic acter `Consumer`.


```python
from econmodels.consumer import Consumer
```

Instantiate the `Consumer` class.


```python
consumer = Consumer()
```

Print the consumers property `utility`. The default utility function is a Cobb-Douglas utility with two goods.


```python
consumer.utility.function
```




$$- U + {\beta}_{0} {\beta}_{1} {x}_{0}^{{\alpha}_{0}} {x}_{1}^{{\alpha}_{1}}$$



Print the consumers property `budget_constraint`.


```python
consumer.budget_constraint.function
```




$$- M + {p}_{0} {x}_{0} + {p}_{1} {x}_{1}$$



Maximize utility given the budget constraint.


```python
consumer.max_utility()
```

Print the resulting demand for input $x_0$.


```python
consumer.get_demand(index=0)
```




$$\frac{M {\alpha}_{0}}{\left({\alpha}_{0} + {\alpha}_{1}\right) {p}_{0}} - {x}_{0}$$


