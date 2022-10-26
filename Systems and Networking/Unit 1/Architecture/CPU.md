# Central Processing Unit

The *Central Processing Unit* is the component that executes actual [instructions](/Systems%20and%20Networking/Unit%201/Architecture/Instructions.md) and computations. In modern [architectures](?TK), there can be multiple processors that work parallelly in order to increase computing power.

![Diagram of a CPU](/assets/cpu_diagram.svg)

## Components

A CPU is composed of many parts, here's a list of the main macro-components:
- [Control Unit](#Control%20Unit)
- [Arithmetic Logical Unit](#Arithmetic%20Logical%20Unit)
- [Address Generation Unit](#Address%20Generation%20Unit)
- [Registers](/Systems%20and%20Networking/Unit%201/Architecture/Registers.md)
- [Cache](/Systems%20and%20Networking/Unit%201/Architecture/Cache.md)

### Control Unit

The *Control Unit* is the unit that *manages* the entire CPU components and behaviours. It tells the other components (e.g. [ALU](#Arithmetic%20Logical%20Unit)) what to do and how to respond to instructions.

### Arithmetic Logical Unit

Also called *Combinatorial Unit*, the *ALU* is the core that executes arithmetic and bitwise logic operations.

It takes in input two operands, which can come from [registers](/Systems%20and%20Networking/Unit%201/Architecture/Registers.md) or [literals](?).

![Arithmetic Logical Unit Diagram](/assets/alu_diagram.png)

### Address Generation Unit

TK

## Instruction Cycle

To execute an [instruction](/Systems%20and%20Networking/Unit%201/Architecture/Instructions.md), the CPU performs *at least* the following 3 steps.
1. **Fetch:** retrieve an instruction from the [central memory](/Systems%20and%20Networking/Unit%201/Architecture/Memory.md), whose address is contained in the [program counter](?TK);
2. **Decode:** interpret the fetched instruction;
3. **Execute:** execute the decoded instruction.