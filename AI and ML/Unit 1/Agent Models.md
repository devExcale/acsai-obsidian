# Agent Models

TK

## Table-Driven Agent

A table-driven agent is represented by a sequence of percepts and an action assigned to every sequence. A pre-set table maps an action to every possible sequence and the agents acts solely on this table:

- the sensors read a percept,
- the action corresponding to the sequence of past percepts (including the one just read) is looked up,
- the action is performed through the actuators.

*Python representation of a table-driven agent.*

```python
# Sequence of read percepts
percepts: tuple
# [Percepts sequence -> action] mapping
table: dict

# Agent function
def table_driven_agent(percept) -> action:
	append(percepts, percept)
	action = table[percepts]
	return action
```

> [!failure] Table Size
> 
> The table containing every possible sequence of percepts can't possibly be computed. The number of possible entries is given by
> 
> $$\large
> 	\sum_{t=1}^T {| \mathcal P |}^t
> $$
> 
> where $T$ is the agent lifetime.

## Simple Reflex Agent

A simple reflex agent is an agent that operates on condition rules. The sensors read percepts which are used to understand the current state of the world, then rules are used to determine an action the actuators have to execute.

*Python representation of a simple reflex agent.*

```python
# A structure containing the [condition -> action] rules
rules: a_data_struct

# Agent function
def table_driven_agent(percept) -> action:
	state = interpret_input(percept)
	rule = rule_match(state, rules)
	action = rule.action
	return action
```

## Model-Based Reflex Agent

TK