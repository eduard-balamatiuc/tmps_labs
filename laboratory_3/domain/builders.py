from domain.products import Smartphone

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
