from domain.products import SamsungProduct

# Base Decorator
class ProductDecorator(SamsungProduct):
    def __init__(self, product):
        self.product = product

    def details(self):
        return self.product.details()

# Concrete Decorators
class ExtendedWarrantyDecorator(ProductDecorator):
    def details(self):
        return f"{self.product.details()} + Extended Warranty"

class AccessoriesDecorator(ProductDecorator):
    def details(self):
        return f"{self.product.details()} + Additional Accessories"
