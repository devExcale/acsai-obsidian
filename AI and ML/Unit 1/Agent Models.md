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

> [!info] Stateless Agent
> 
> The Simple Reflex Agent is a *stateless* agent, in the sense that the agent decides on an action by rules which are applied to the current state of the environment, without keeping track of the past.


![Simple Reflex Agent Diagram](/assets/Diagram%20-%20Agent%20Simple%20Reflex.bmp)

*Python representation of a simple reflex agent.*

```python
# A structure containing the [condition -> action] rules
rules: any

# Agent function
def simple_reflex_agent(percept) -> action:
	state = interpret_input(percept)
	rule = rule_match(state, rules)
	return rule.action
```

## Model-Based Reflex Agent

The model-based reflex agent is similar to the simple reflex one. It reasons with rules too, but it keeps track of the previous states and actions which help decide in a resulting action.

A model-based reflex agent requires:

- **transition model,** a description of how the the next state depends on the current state and action (e.g. [automa](?TK));
- **sensor model,** a description of how the current world state is reflected in the agent's percepts.

> [!info] Stateful Agent
> 
> The Model-Based Reflex Agent is a *stateful* agent, in the sense that the agent decides on an action based on the current state, which is related to information of past states and actions

![Model-Based Reflex Agent Diagram](/assets/Diagram%20-%20Agent%20Model-Based%20Reflex.bmp)

*Python representation of a model-based reflex agent.*

```python
# A structure containing the [condition -> action] rules
rules: any
# State transition descriptor
transition_model: any
# [Percepts -> environment state] descriptor
sensor_model: any
# Current state of the environment
# (known by the agent)
current_state: state
# Most recent action
last_action: action

# Agent function
def model_reflex_agent(percept) -> action:
	current_state = update_state(current_state, last_action, percept, transition_model, sensor_model)
	rule = rule_match(current_state, rules)
	last_action = rule.action
	return last_action
```

## Goal-Based Agent

TK

![Goal-Based Agent Diagram](/assets/Diagram%20-%20Agent%20Goal-Based.bmp)

## Utility-Based Agent

TK

![Utility-Based Agent Diagram](/assets/Diagram%20-%20Agent%20Utility-Based.bmp)

## Learning Agent

TK

![Learning Agent Diagram](/assets/Diagram%20-%20Agent%20Learning.bmp)