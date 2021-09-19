from abs_factory import AbsFactory
from gm import *


class GMFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return ChevySpark()
 
    @staticmethod
    def create_sport():
        return ChevyCamaro()
 
    @staticmethod
    def create_luxury():
        return CadillacCTS()

