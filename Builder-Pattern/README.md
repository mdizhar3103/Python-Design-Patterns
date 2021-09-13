## Builder Pattern - used for building complex objects
- Creational Pattern
- Separates construction of an object from its representation
- Encapsulates object construction
- Multi-Step construction process
- Implementation can vary
- The client sees only the abstraction

*See basic.py*
*See basic2.py*
---------------
**Using SOLID principle**
*See computer.py, mycomputer.py*
Another approach: *See mycomputer2.py*
> Note: This code has a maintenance problem if the code > is copied and applied to another product we need to change the other functions.

**Structure of Builder Pattern**

        +-------------------------+         +-------------------------+
        |  Director:              |         |  AbsBuilder:            |
        +-------------------------+         +-------------------------+
        |  Attributes             |         |   Attributes            |
        |  Operations             |         |   Operations            |
        |    + Construct()        | ------> |       + BuildPart()     |
        +--------+----------------+         +------------+------------+
                                                        /|\
                                                         |
                                                         |
        +-------------------------+                      |
        |ConcreteBuilder:         |                      |
        +-------------------------+                      |
        |  Attributes             |                      |
        |  Operations             |                      |
        |    + BuildPart()        | ---------------------+
        |    + GetResult()        |
        +-------------------------+  

*See abs_builder.py, mycomputer_builder.py, director.py*