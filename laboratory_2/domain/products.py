class SamsungProduct:
    def details(self):
        raise NotImplementedError("Each product must have a 'details' method")

class Smartphone(SamsungProduct):
    def details(self):
        return "Samsung Smartphone with advanced features."

class TV(SamsungProduct):
    def details(self):
        return "Samsung Smart TV with UHD resolution."

class Appliance(SamsungProduct):
    def details(self):
        return "Samsung Appliance with energy-efficient technology."
