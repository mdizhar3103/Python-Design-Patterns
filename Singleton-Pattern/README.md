## Singleton Pattern
Used to control access to class instances
- Creational Pattern
- Ensure a class has only one instance
- Control access to limited resources
    - Device access 
    - Buffer pools
    - Web/DB connection pool
- Provide a global point of access
- Class responsible for its instances 
- Lazy construction 
**Demo - Logging Subsystem, Log events to a file**
- Only one instance can write to the file
- Need to control access 
- Classic Singleton pattern
> See: singletonbasic.py, loggerbasic.py
*Note: Singleton are considered Harmful*
- Hard to Test
- Carry Global State 
- Violates S of SOLID
- Non standard Class access
--------------------------------------------
**Using two instances - SOLID principle**
*See: singleton_base.py, logger_base.py*
```
python logger_base.py
```
> Using this approach in single file we are 
> able to add two instances data
> But we fixed SOLID principle violation
--------------------------------------------
**Using abc module - Metaclass**
*See: singleton_meta.py, logger_meta.py*
```
python logger_meta.py
```
> Control building of class, class's class, class is instance of class 
--------------------------------------------
**Using Monostate - Python Dynamic behaviour**
*See: monostate.py, logger_mono.py*
```
python logger_mono.py
```
--------------------------------------------
**Note: Use Singleton Pattern carefully**