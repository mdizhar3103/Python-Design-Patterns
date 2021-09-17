from abc import ABCMeta, abstractmethod

class AbsAuto(metaclass=ABCMeta):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    