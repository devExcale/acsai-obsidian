# Agent

An agent is something that interacts dynamically with an environment.

![Agent Logic Diagram](/assets/Diagram%20-%20Agent.bmp)

An agent is composed of
- **sensors,** which are used to read from the environment (the possible readings are called *percepts*);
- **some kind of logic,** which turns the percepts into actions (by decision making);
- **actuators,** which are used to perform the actions and interact with the *environment*.

> [!example] Agents
> 
> Example of agents are web browsers, robots, automatic vacuum cleaners.

The rigorous definition of an agent is 

$$\large
	f : \mathcal P^* \nrightarrow \mathcal A,
$$

which basically means that an agent is a **partial function** (maps only a subset of the whole domain) that partially maps the **[closure](?TK) of percepts** to a **set of actions**.

The agent function is integral part of the agent diagram: percepts are fed in by the sensors and actions are executed by the actuators.

## Goal Based Agent

An agent can be designed to act not towards a final goal, but towards getting the **most performance** out of every step. This is called a **goal-based agent**, and the criteria which decides the rankings of performance is called **performance measure**.

Performance measures should be built according to what the agent should achieve, and not how it should be achieved.

> [!example] Chess Analogy
> 
> A good goal-based chess agent's performance measure could be composed of abstract *strategy points*. Some moves may give more strategy points than others, and better yet if the performance measure can give even more strategy points to moves that will be useful in the future. This way, the agent's goal is to win the chess game by maximising the awarded strategy points.
> 
> A bad agent, for example, will always try to eat every piece or to check the king. Doing this isn't the best way to win a chess game.

### PEAS

PEAS is an acronym that indicates the base structure of every goal-based agent. It stands for:

- *Performance measure*
- *Environment*
- *Actuators*
- *Sensors*

> [!example] pac-man
> 
> The pac-man ghosts are agents with the following PEAS.
> 
> - **Performance Measure:** could be the distance from pac-man or how close it is from catching it (by some sort of criteria)
> - **Environment:** the maze
> - **Actuators:** whatever moves the ghost
> - **Sensors:** whatever it uses to understand theirs and pac-man's position in the maze and if pac-man is energized
