## Observer Pattern 
- Heavily used in Event Monitoring
- The behavioral pattern used to control some operation one to many relationships between a set of objects.
- When the state of one object changes, its dependents are notified
- Also known as:
    - Dependent Pattern
    - Publish-Subscribe Pattern

 
## Structure of Observer Pattern
```
        +----------+
        |          |
        | Observer | <==========>\
        |          |              \
        +----------+               \
        +----------+                \
        |          |                 \       +---------+ 
        | Observer | <===============>       | Subject | 
        |          |                 /       +---------+
        +----------+                /
        +----------+               /
        |          |              /
        | Observer | <==========>/
        |          |          
        +----------+      
         
        <============> means - notify, Get/Set state
 
        UML Diagram +---+
        			    |
        			   \|/
        +-------------------------+         +-------------------------+
        |AbsSubject:              |         | AbsObserver:            |
        +-------------------------+         +-------------------------+
        |  Attributes             |         |   Attributes            |
        |  Operations             |         |   Operations            |
        |    + Attach(Observer)   | ------> |       + Update()        |
        |    + Detach(Observer)   |         |                         |
        |    + Notify()           |         |                         |
        +--------+----------------+         +------------+------------+
                /|\                                     /|\
                 |                                       |
                 |                                       |
        +-------------------------+         +-------------------------+
        |ConcreteSubject:         |         | ConcreteObserver:       |
        +-------------------------+         +-------------------------+
        |  Attributes             |         |   Attributes            |
        |       + Subject State   |         |       + Observer State  |
        |  Operations             |         |   Operations            |
        |    + Attach(Observer)   | <------ |       + Update()        |
        |    + Detach(Observer)   |         |                         |
        |    + GetState()         |         |                         |
        |    + Notify()           |         |                         |
        +-------------------------+         +-------------------------+
```

## Demo - Dashboard for tech support center
KPIs:
- open tickets
- New tickets in last hours
- Closed tickets in last hours

**Note:** Dashboard is the observer, KPI is a subject or publisher

*See basic.py - for normal approach*
**Note:**  
- Real application is MVC: Model - Subject and View - Observer 
- Many applications are GUIs based apps

*The code implemented using SOLID principle has some bugs to improve that we need to use context managers.*