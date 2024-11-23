from domain.products import Smartphone, TV, Appliance

class ProductFactory:
    def create_product(self, product_type):
        if product_type == "Smartphone":
            return Smartphone()
        elif product_type == "TV":
            return TV()
        elif product_type == "Appliance":
            return Appliance()
        else:
            raise ValueError("Unknown Product Type")
