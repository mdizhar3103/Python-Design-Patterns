# Command Pattern - Command Line Programs (Request processing object)
- Behavioral Pattern
- Encapsulates a request on the object
- Parametrize objects
- Queues and log operations
- Undoable operations and macros (sequences of commands)
- Also known as: 
    - Action pattern
    - Transactional pattern 

**Demo:** - Command Line Order Processing Program 
- Three operations:
    - CreateOrder
    - UpdateQuantity
    - ShipOrder
- Parse the command line arguments
- Execute the command
- Notify the user and log the results
*See basic.py*
## Structure of Command Pattern
        +-------------------------+         +-------------------------+
        |  Invoker::              |         | AbsCommand:             |
        +-------------------------+         +-------------------------+
        |  Attributes             |         |   Attributes            |
        |  Operations             |         |   Operations            |
        |    + set_command()      | ---->   |       + execute()       |
        |                         |         |       + undo()          |
        +--------+----------------+         +------------+------------+
                                                     /|\
                                                      |
                                                      |
        +-------------------------+         +-------------------------+
        | Reciever:               |         | ConcreteCommand:        |
        +-------------------------+         +-------------------------+
        |  Attributes             |         |   Attributes            |
        |  Operations             |         |   Operations            |
        |    + action()           | <------ |       + execute()       |
        |                         |         |       + undo()          |
        +-------------------------+         +-------------------------+
                /|\                                 /|\ 
                 |                                   |
        +-------------------------+                  |
        | Client  :               |                  |
        +-------------------------+                  |
        |  Attributes             |                  |
        |  Operations             | -----------------+
        +-------------------------+         

## Implementation
For each operation create each file as command operation
- CreateOrder     *See create_order.py*
- UpdateQuantity  *See update_order.py*
- ShipOrder       *See ship_order.py*
**Note:** *See no_command.py when no command is issue*

Finally test program using python command
```python
python main.py UpdateQuantity 10
```
*See main.py*
