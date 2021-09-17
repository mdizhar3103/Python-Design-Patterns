from abc import ABCMeta, abstractmethod
 
class AbsAuto(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass
 
    @abstractmethod
    def stop(self):
        pass