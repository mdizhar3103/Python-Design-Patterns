from autofactory import AutoFactory

factory = AutoFactory()
 
for carname in 'ChevyVolt', "FordFocus", "JeepSahara", "Tesla":
    car = factory.create_instance(carname)
    car.start()
    car.stop()
