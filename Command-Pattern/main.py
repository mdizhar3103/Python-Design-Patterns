from create_order import CreateOrder
from update_order import UpdateOrder
from ship_order import ShipOrder
from no_command import NoCommand
import sys

 
def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    return dict([clas.name, clas] for clas in commands)
 
def print_usage(commands):
    print("Usage: python -m Command CommandName [arguments]")
    print("Commands: ")
    for command in commands.values():
        print("\t %s" % command.description)
 
def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    if len(args) > 1:
        return command(args)
    else:
        return command() 

if __name__ == "__main__":
    commands = get_commands()
    if len(sys.argv) < 2:
        print_usage(commands)
        exit()
    
    # Find and execute the command
    command = parse_command(commands ,sys.argv[1:])
    command.execute()
