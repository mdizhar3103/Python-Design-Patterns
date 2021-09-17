from abc import ABCMeta, abstractmethod


class AbsFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_auto(self):
        pass