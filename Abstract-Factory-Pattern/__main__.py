from ford_factory import FordFactory
from gm_factory import GMFactory


for factory in FordFactory, GMFactory:
    car = factory.create_economy()
    car.start()
    car.stop()
    print("=======================")
    car = factory.create_sport()
    car.start()
    car.stop()
    print("=======================")
    car = factory.create_luxury()
    car.start()
    car.stop()
    print("=======================")
