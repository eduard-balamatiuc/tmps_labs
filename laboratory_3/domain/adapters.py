from domain.products import SamsungProduct

# Third-party product with an incompatible interface
class ThirdPartyLaptop:
    def get_specifications(self):
        return "Third-Party Laptop [Specs: Intel i7, 16GB RAM, 512GB SSD]"

# Adapter class to make ThirdPartyLaptop compatible with SamsungProduct
class LaptopAdapter(SamsungProduct):
    def __init__(self, third_party_laptop):
        self.laptop = third_party_laptop

    def details(self):
        return self.laptop.get_specifications()
