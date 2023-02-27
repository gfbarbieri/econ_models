Overview
========

This section provides an overview of the main classes and functions of econ_models and how
I designed them to be used. For more detailed information of each class or functions, please
refer to the :doc:`guide` and :doc:`reference`.

Structure
---------

The basic structure of econ_mdoels is as follows:
1. The properties of an economic agent are functions such as :class:`Production`, :class:`Utility`,
:class:`Budget_Constraint`, or :class:`Cost_Structure`. Properties of a market include :class:`Market`, which
can be used to quickly create market demand and supply functions. Ultimatley, combinations of properties
will be used to define economic agents.
2. Agent types are the decision makers in any economic model, such as :class:`Firm` or :class:`Consumer`, etc..
Agent types are combinations of properties, giving agents the ability to produce, consumer, or otherwise decide
how to use inputs. Agents are expected to have the ability decide how to use inputs and in what quantities,
typically through maximization of a benefit (profit, utility) given a constraint (budget constraint, technological
limitations, or a cost structure).
3. Models are made up of either ageny types or market-level properties. Markets are the primary interest of this
module and it is what we seek to explore most indepthly. The market library should contain examples of how to use
the agent types to generate models and explore their implications.