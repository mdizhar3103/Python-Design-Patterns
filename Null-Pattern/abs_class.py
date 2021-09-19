from abc import ABCMeta, abstractmethod
 
class AbsClass(metaclass=ABCMeta):
    @abstractmethod
    def do_something(self,value):
        pass
