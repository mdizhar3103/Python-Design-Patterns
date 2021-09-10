from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand


class ShipOrder(AbsCommand, AbsOrderCommand):
    name = "ShipOrder"
    description = "Shipping Order"
 
    def execute(self):
        print("Order Shipped")
