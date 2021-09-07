from order import Order
from shippingcost import ShippingCost
from fedexstrategy import FedExStrategy
from upsstrategy import UPSStrategy
from postalstrategy import PostalStrategy


# Test Federal Express shipping
order = Order()
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
print(cost == 3.0)

# Test UPS shipping
order = Order()
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
print(cost == 4.0)

# Test Postal Service shipping
order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
print(cost == 5.0)