from domain.products import Smartphone, TV, Appliance

class ProductFactory:
    @staticmethod
    def create_product(product_type):
        if product_type == "Smartphone":
            return Smartphone()
        elif product_type == "TV":
            return TV()
        elif product_type == "Appliance":
            return Appliance()
        else:
            raise ValueError("Unknown Product Type")
