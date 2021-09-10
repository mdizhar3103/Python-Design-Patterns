class CommandExecutor(object):
 
    def execute_command(self, args):
        if args[0] == "CreateOrder":
            self.create_order()
        elif args[0] == "UpdateQuantity":
            self.update_quantity(args[1])
        elif args[0] == "ShipOrder":
            self.ship_order()
        else:
            print("Unknown command: " + args[0])
 
    def create_order(self):
        pass
 
    def update_quantity(self, val):
        print(val)
        old_val = 72
        print("Database updated")
        print("Logging updated quantity from %s to %s" %(old_val,val))
 
    def ship_order(self):
        pass 
 
 
import sys
 
if len(sys.argv) < 2:
    print("Usage: python -m BeforeCommand <command>")
    print("""Commands: 
            \n\tCreateOrder 
            \n\tUpdateQuantity number 
            \n\tShipOrder""")
    exit()
 

executor = CommandExecutor()
executor.execute_command(sys.argv[1:])
 
# python temp.py UpdateQuantity 10
