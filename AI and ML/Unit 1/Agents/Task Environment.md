# Task Environment

The task environment is the environment that an [agent](/AI and ML/Unit 1/Agents/Agent.md) interacts with.

## Characteristics of an Environment

Various characteristics define an environment, a good agent is developed starting from a correct analysis of the environment.

### Observability

- **Fully observable,** the state of the environment can be fully known;
- **Partially observable.** the state of only a part the environment can be known;
- **Unobservable,** the state of the environment can't be known at all.

The observability of an environment doesn't have to be static and can change.

> [!example] Real world and a camera
> 
> A machine can observe the real world (*environment*) via a camera (*sensors*):
> - during the day the environment is *partially observable*;
> - during the night the environment is *unobservable*.

### Multiplicity

An environment that hosts just a single agent is called a **single-agent** environment, an environment that hosts multiple agents at the same time is called a **multi-agent** environment.

In a multi-agent environment, the agents can either be **competitive** or **cooperative**.

### Stochasticity

Multiple events can happen in an environment, the stochasticity of an environment is an indicator of how much is known of the probability of the events happening.

- **Deterministic,** actions in a deterministic environment have a certain outcome, it is possible to correctly predict how the environment will evolve in time;
- **Non-deterministic,** actions in a non-deterministic environment have outcomes with known probabilities, it may be possible to predict an expectation of how the environment will evolve in time;
- **Stochastic,** actions in a stochastic environment have outcomes with unknown probabilities, it is impossible to predict how the environment will evolve in time.

> [!example] Pac-man's Maze
> 
> Pac-man's maze can be both deterministic and non-deterministic, based on the version of the game.
> 
> - In the first version, there are only points on the ground which will add up to the score and nothing more. This environment is *deterministic*, because the agent knows how it will evolve (it won't evolve at all).
> - In further versions, fruits may pop up randomly in the maze which will add even more to the score. This environment is *non-deterministic*, *stochastic* even, because there's a random component such that the agent won't be able to predict the next state of the environment.

### Episodic or Sequential

An episodic environment is an environment such that the agent's actions have independent consequences, i.e. one action won't affect the next one.

> [!example] Classification
> 
> Many classification types are episodic, because classifying a percept doesn't influence the classification of the next percept.

A sequential environment is an environment such an agent's action may affect the next one.

> [!example] Chess
> 
> A chess board is a sequential environment: single actions have long-term consequences.

### Dynamicity

- **Static,** a static environment won't change with time (*chess*);
- **Dynamic,** a dynamic environment will change with time (*driving*);
- **Semidynamic,** a semidynamic environment won't change with time, but the agent's score will (*e.g. timed chess*).

### Distrete or Continuous

*TK*

### Action's Effect

*TK* (Known / Unknown)
