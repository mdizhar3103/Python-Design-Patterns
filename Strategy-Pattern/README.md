## Strategy Pattern - most used pattern

Demo: *Shipping Cost calculator*
> Must support:
  - Federal Express
  - UPS
  - Postal Service

> Must be extendable (add new shippers)

## SOLID Principles of Object-Oriented Design

- **Single Responsibility** - A class should have only one responsibility
- **Open-closed** - A class should be open for extension using inheritance
- **Liskov Substitution Principle** - Base class should extend the parent class without breaking anything
- **Interface segregation** - Many specific interfaces are better than do it all interfaces. 
- **Dependency Inversion** - We should program towards abstraction, not towards implementation

```
open basic.py 
```

## Strategy Pattern Structure

                    +-------------------------+
                    |Context:                 |
                    +-------------------------+
                    |  Attributes             |
                    |  Operations             |
                    |    + ContextInterface() |
                    |    + __init__(Strategy) |
                    +-------------------------+
                                 |
                                 |
                                \|/
                    +------------+--------------+
                    |Strategy:                  |
                    +---------------------------+
                    |  Attributes               |
                    |  Operations               |
                    |    + AlgorithmInterface() |
                    +------------+--------------+
                                /|\
                                 |
                    +------------+--------------+
                    |ConcreteState:             |
                    +---------------------------+
                    |  Attributes               | ................ many subclasses
                    |  Operations               |
                    |    + AlgorithmInterface() |
                    +------------+--------------+

## Above Scenario Structure

                +-------------------------+
                |ShippingCost             |
                +-------------------------+
                |  Attributes             |
                |  Operations             |
                |    + shipping_cost()    |
                |    + __init__(Strategy) |
                +-------------------------+
                             |
                             |
                            \|/
                +------------+--------------+
                |AbStrategy:                |
                +---------------------------+
                |  Attributes               |
                |  Operations               |
                |    + calculate()          |
                +------------+--------------+
                            /|\
                             |
                +------------+--------------+
                |FedexStrategy:             |
                +---------------------------+
                |  Attributes               | ..... similar for ups, and others.
                |  Operations               |
                |    + calculate()          |
                +---------------------------+

- See main.py for implementation

**Note:** Strategy Variation have different approaches-
- Strategies as function
- Strategies as lambdas

See variations.py for implementation 
