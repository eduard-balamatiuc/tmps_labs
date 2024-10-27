class Smartphone:
    def __init__(self):
        self.color = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"Samsung Smartphone [Color: {self.color}, RAM: {self.ram}GB, Storage: {self.storage}GB]"

class SmartphoneBuilder:
    def __init__(self):
        self.smartphone = Smartphone()

    def set_color(self, color):
        self.smartphone.color = color
        return self

    def set_ram(self, ram):
        self.smartphone.ram = ram
        return self

    def set_storage(self, storage):
        self.smartphone.storage = storage
        return self

    def build(self):
        return self.smartphone
