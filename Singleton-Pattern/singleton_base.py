class Singleton(object):
    _instances = {} # dict([cls, instance])
 
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        #     print("executed Singleton __new__ inside")
        # print("executed Singleton __new__ outside")
        return cls._instances[cls]