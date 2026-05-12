Project Analyzed: Pydantic

1. Number of PBTs: 133
2. Number of PBTs with explicit constraints: 9

Explanation: 
I identified the total number of property-based tests by searching for the `@given` decorator across the repository. The subset of tests with explicit constraints was identified by searching within those results for specific strategy arguments (e.g., `min_value`, `max_value`) and the `assume()` function, which restrict the input generation space.