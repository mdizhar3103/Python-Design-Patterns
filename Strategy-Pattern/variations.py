# Strategy Pattern Implementation
from abc import ABCMeta, abstractmethod
 

class Order(object):
    pass


class ShippingCost(object):
 
    def __init__(self, strategy):
        self._strategy = strategy
 
    def shipping_cost(self, order):
        return self._strategy(order)
 

# function strategy
def fedex_strategy(order):
    return 3.00
 

# lambda strategy
ups_strategy = lambda order: 4.00


order = Order()

# Test Federal Express shipping
strategy = fedex_strategy
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
print(cost == 3.0)
 
 
# Test UPS shipping
cost_calculator = ShippingCost(ups_strategy)
cost = cost_calculator.shipping_cost(order)
print(cost == 4.0)


# Test Postal Service Shipping
cost_calculator = ShippingCost(lambda order: 5.00)
cost = cost_calculator.shipping_cost(order)
print(cost == 5.0)