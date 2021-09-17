from .abs_factory import AbsFactory
from autos.nullcar import NullCar


class NullFactory(AbsFactory):

    def create_auto(self):
        name = 'Invalid Car'
        self.nc = nc = NullCar(name)
        nc.name = name
        return nc
