class Appliance():
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

class Refrigerator(Appliance):
    def __init__(self, manufacturer, agent):
        Appliance.__init__(self, manufacturer)
        self.agent = agent

    def __str__(self):
        return "The " + self.manufacturer + " refrigerator contains refrigerant " + self.agent

my_refrigerator = Refrigerator("Samsung", "R134a") # R134a is the refrigerant (cooling agent) used
print(my_refrigerator)
