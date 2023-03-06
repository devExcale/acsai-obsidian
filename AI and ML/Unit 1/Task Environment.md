# Task Environment

The task environment is the environment that an [agent](/AI%20and%20ML/Unit%201/Agents.md) interacts with. There are various characteristics that define an environment.

## Characteristics

### Observability of an Environment

- **Fully observable:** the state of the environment can be fully known;
- **Partially observable:** the state of only a part the environment can be known;
- **Unobservable:** the state of the environment can't be known at all.

The observability of an environment doesn't have to be static and can change.

> [!example] Real world and a camera
> 
> A machine can observe the real world (*environment*) via a camera (*sensors*):
> - during the day the environment is *partially observable*;
> - during the night the environment is *unobservable*.

### Multiplicity of an Environment

An environment that hosts just a single agent is called **single-agent**, an environment that hosts multiple agents at the same time is called **multi-agent**.

In a multi-agent environment, the agents can either be **competitive** or **cooperative**.

### Other

**Deterministic / Non-deterministic:** an environment is called *deterministic* if it abides to some rules that makes it possible to predict how it will evolve in time, otherwise it's called *non-deterministic*.

> [!example] Pac-man's Maze
> 
> There are two versions of the maze in pac-man.
> - In the first version, there are only points on the ground which will add up to the score and nothing more. This environment is deterministic, because the agent knows how it will evolve (it won't evolve at all).
> - In further versions, fruits may pop up randomly in the maze which will add even more to the score. This environment is non-deterministic, because there's a random component such that the agent won't be able to predict the next state of the environment.

**Episodic / Sequential:** TK the order of actions may matter (sequential)

**Static / Semi-dynamic / Dynamic:** TK

**Discrete / Continuous:** TK

**Action's effect:** Known / Unknown TK
