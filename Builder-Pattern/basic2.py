class Computer(object):
    def display(self):
        print("Custom Computer:")
        print("\t{:>10}: {}".format("Case", self.case))
        print("\t{:>10}: {}".format("Mainboard", self.mainboard))
        print("\t{:>10}: {}".format("CPU", self.cpu))
        print("\t{:>10}: {}".format("Memory", self.memory))
        print("\t{:>10}: {}".format("Hard drive", self.hard_drive))
        print("\t{:>10}: {}".format("Video card", self.video_card))
 
computer = Computer()
computer.case = "Cooler Master N300"
computer.mainboard = "MSI 970"
computer.cpu = "Intel Core i7-4770"
computer.memory = "Corsair Vengeance 16GB"
computer.hard_drive = "Seagate 2TB"
computer.video_card = "GeForce GTX 1070"
 
computer.display()
