import sympy as sp
import pytest
from econmodels.agents.consumer import Consumer
from econmodels.functional_forms.utility import Utility
from econmodels.functional_forms.constraint import Input_Constraint

def test_init():

    consumer = Consumer()
    
    assert consumer.num_goods == 2
    
    assert consumer.utility == Utility(consumer.num_goods)
    
    assert consumer.constraint == Input_Constraint(consumer.num_goods)

def test_maximize_utility():

    consumer = Consumer()

    consumer.maximize_utility()

    assert consumer.utility.maximize_utility() == sp.Matrix([
        [sp.Symbol('C')/sp.Symbol('P_0')],
        [sp.Symbol('C')/sp.Symbol('P_1')]
    ])

def test_get_demand():
    consumer = Consumer()
    consumer.maximize_utility()
    demand = consumer.get_demand()

    assert demand == sp.Matrix([
        [sp.Symbol('C')/sp.Symbol('P_0')],
        [sp.Symbol('C')/sp.Symbol('P_1')]
    ])