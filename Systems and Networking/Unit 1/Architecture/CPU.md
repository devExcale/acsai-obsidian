# Central Processing Unit

The *Central Processing Unit* is the component that executes actual [instructions](/Systems and Networking/Unit 1/Architecture/Instructions.md) and computations. In modern [architectures](?TK), there can be multiple processors that work parallelly in order to increase computing power.

![Diagram of a CPU](/assets/Diagram - CPU.svg)

## Components

A CPU is composed of many parts, here's a list of the main macro-components:
- [Control Unit](#Control Unit)
- [Arithmetic Logical Unit](#Arithmetic Logical Unit)
- [Address Generation Unit](#Address Generation Unit)
- [Registers](/Systems and Networking/Unit 1/Architecture/Registers.md)
- [Cache](/Systems and Networking/Unit 1/Architecture/Cache.md)

### Control Unit

The *Control Unit* is the unit that *manages* the entire CPU components and behaviours. It tells the other components (e.g. [ALU](#Arithmetic Logical Unit)) what to do and how to respond to instructions.

### Arithmetic Logical Unit

Also called *Combinatorial Unit*, the *ALU* is the core that executes arithmetic and bitwise logic operations.

It takes in input two operands, which can come from [registers](/Systems and Networking/Unit 1/Architecture/Registers.md) or [literals](?).

![Arithmetic Logical Unit Diagram](/assets/Diagram - ALU.png)

### Address Generation Unit

TK

## Instruction Cycle

To execute an [instruction](/Systems and Networking/Unit 1/Architecture/Instructions.md), the CPU performs *at least* the following 3 steps.
1. **Fetch:** retrieve an instruction from the [central memory](/Systems and Networking/Unit 1/Architecture/Memory.md), whose address is contained in the [program counter](?TK);
2. **Decode:** interpret the fetched instruction;
3. **Execute:** execute the decoded instruction.
