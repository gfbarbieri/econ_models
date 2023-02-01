# Overview

Econ Models are classes that allow you to explore specific economic models.

## Included Models:
1. Monopoly model.

## Example Usage

Import the class.


```python
from models.monopolist import Monopolist
```

Instantiate the class.


```python
firm = Monopolist()
```

Print the total revenue and total cost functions.


```python
print(firm.get_total_revenue())
print(firm.get_total_cost())
```

    p*q
    c*q


Print generalized profit function.


```python
print(firm.get_profit())
```

    -c*q + p*q


Print the demand function with quantity as a function of price Q(P), and price as a function of quantity P(Q).


```python
print(firm.get_demand(inverse=False))
print(firm.get_demand(inverse=True))
```

    (a - p)/b
    a - b*q


Print the total revenue function where P is substituted with the inverse demand function.


```python
print(firm.get_total_revenue(p=firm.get_demand(inverse=True)))
```

    q*(a - b*q)


Print marginal revenue and marginal cost functions where P is substituted with the inverse demand function.


```python
print(firm.get_marginal_revenue(p=firm.get_demand(inverse=True)))
print(firm.get_marginal_cost())
```

    a - 2*b*q
    c


Print the generalized profit function where P is substituted with the inverse demand function.


```python
print(firm.get_profit(p=firm.get_demand(inverse=True)))
```

    -c*q + q*(a - b*q)


Find the firm's price elasticity of demand at any price and quantity.


```python
print(firm.price_elasticity())
```

    -p_0/(b*q_0)


Find the profit maximizing price, quantity, and maximum profit.


```python
print(firm.profit_maximization())
```

    (a/2 + c/2, (a - c)/(2*b), -c*(a - c)/(2*b) + (a/2 + c/2)*(a - c)/(2*b))


Find the firm's price elasticity of demand at the profit maximizing price and quantity.


```python
p, q, profit = firm.profit_maximization()

print(firm.price_elasticity(p_0=p, q_0=q).simplify())
```

    (-a - c)/(a - c)


Market demand functions take the form of $P = a - b*Q$. Cost functions take the form of $TC = c*Q$. Set parameters for market demand and cost functions of a = 100, b = 1, and c = 25.


```python
firm = Monopolist(a=100, b=1, c=25)
```

Find profit maximizing price, quantity, maximum profit, and elasticity at the profit maximizing price and quantity.


```python
p, q, profit = firm.profit_maximization()

print(f"The profit maximizing price per unit is {p.evalf()}.")
print(f"The profit maximizing quantity produced is {q.evalf()}.")
print(f"The firm's total profit is {profit.evalf()}.")
print(f"The price elasticity of demand at the profit maximizing price and quantity is {firm.price_elasticity(p_0=p, q_0=q)}.")
```

    The profit maximizing price per unit is 62.5000000000000.
    The profit maximizing quantity produced is 37.5000000000000.
    The firm's total profit is 1406.25000000000.
    The price elasticity of demand at the profit maximizing price and quantity is -5/3.

