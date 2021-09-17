## Factory Pattern 
Used when to create multiple objects from the same API
- Creational Pattern
- Define an interface for creating objects 
- Let subclasses decide which object 
- Defer instantiation to subclasses
- Also knows as Virtual Constructor

*See __basic__ folder and all files in the directory*
Run the basic approach 
```
>>> python basic/main.py
```
----------------
# Structure of Factory Pattern 
```
        +------------------------------+         +----------------+
        |   AutoFactory:               |         |   AbsAuto:     |
        +------------------------------+         +----------------+
        | Attributes                   |         |   Attributes   |
        |  + autos: Dict(string, class)|         |                |
        | Operations                   |         |   Operations   |
        |  + create_instance(carname)  | ------> |     + start()  |
        |  + load_autos()              |         |     + stop()   |
        +------------------------------+         +----------------+
                                                        /|\
                                                        |
                                                        |
                +----------------------+---------------------+
                |                      |                     |
        +----------------+       +----------------+   other subclasses
        |  ChevyVolt:    |       |   FordFocus:   |
        +----------------+       +----------------+
        |  Attributes    |       |   Attributes   |
        |  Operations    |       |   Operations   |
        |    + start()   | <---- |    + start()   |
        |    + stop ()   |       |    + stop()    |
        +----------------+       +----------------+
        
```

*See __pattern__ folder and all files in the directory*
Run the pattern approach 
```
>>> python pattern/main.py
```

-----------------------------------
## Full Factory Pattern
```
        +----------------+         +-------------------------+
        |  AbsProduct:   |         |  AbsFactory:            |
        +----------------+         +-------------------------+
        |  Attributes    |         |   Attributes            |
        |  Operations    |         |   Operations            |
        |                | ------> |     + create_product()  |
        +--------+-------+         +------------+------------+
                /|\                            /|\
                |                              |
                |                              |
        +-------------------+         +-------------------------+
        |  ConcreteProduct: |         |  ConcreteFactory:       |
        +-------------------+         +-------------------------+
        |  Attributes       |         |   Attributes            |
        |  Operations       | ----->  |   Operations            |
        |                   |         |     + create_product()  |
        +-------------------+         +-------------------------+
 
```
*See __full-factory__ folder and all files in the directory*
Run the full-factory approach 
```
>>> python full-factory/main.py
```