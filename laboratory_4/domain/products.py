class SamsungProduct:
    def details(self):
        raise NotImplementedError("Each product must implement the 'details' method.")

# Concrete Products
class Smartphone(SamsungProduct):
    def __init__(self, color=None, ram=None, storage=None):
        self.color = color
        self.ram = ram
        self.storage = storage

    def details(self):
        return (
            f"Samsung Smartphone [Color: {self.color}, RAM: {self.ram}GB, "
            f"Storage: {self.storage}GB]"
        )

class TV(SamsungProduct):
    def __init__(self, size=None):
        self.size = size

    def details(self):
        return f"Samsung TV [Size: {self.size}\"]"

class Appliance(SamsungProduct):
    def details(self):
        return "Samsung Appliance with energy-efficient technology."
