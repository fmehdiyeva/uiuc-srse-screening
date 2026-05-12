Comparison of PBT and SMT-Based Strategies

* Feasibility: 
Translating basic constraints—such as integer bounds and linear arithmetic—into SMT is straightforward and highly effective. However, the feasibility drops sharply when dealing with complex data structures. Mapping Pydantic's internal data models, custom validation decorators, and dynamic typing into first-order logic formulas requires significant manual modeling overhead.

* Differences: 
Hypothesis (PBT) relies on structured, diverse random sampling. It excels at testing a wide breadth of the input space to uncover unhandled exceptions. In contrast, Z3 (SMT) is deterministic. It does not explore the space randomly; rather, it uses logical solvers to find a single, guaranteed satisfying assignment if one exists (often defaulting to boundary values like 0). While SMT guarantees constraint satisfaction, it lacks the diverse exploration of PBT.

* Limitations: 
A major limitation of SMT-based generation in this context is the inability to easily model arbitrary Python semantics. For example, if a PBT constraint relies on a complex regex pattern for string validation or invokes a third-party library's behavior, expressing those exact semantics purely as SMT constraints is often impractical or computationally intractable compared to simply filtering random inputs.