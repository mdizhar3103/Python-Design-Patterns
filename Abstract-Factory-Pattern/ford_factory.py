from abs_factory import AbsFactory
from ford import *


class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()
 
    @staticmethod
    def create_sport():
        return FordMustang()
 
    @staticmethod
    def create_luxury():
        return LincolnMKS()
 
