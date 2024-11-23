from singleton.singleton import ProductCatalog
from factories.product_factory import ProductFactory
from domain.builders import SmartphoneBuilder
from domain.products import TV

class ProductManager:
    def __init__(self):
        self.catalog = ProductCatalog()
        self.factory = ProductFactory()

    def add_product(self, product_type, **kwargs):
        if product_type == "Smartphone":
            # Use Builder pattern for Smartphone
            builder = SmartphoneBuilder()
            for key, value in kwargs.items():
                if hasattr(builder, f"set_{key}"):
                    getattr(builder, f"set_{key}")(value)
            product = builder.build()
        elif product_type == "TV":
            # Directly create TV instance
            product = TV(**kwargs)
        else:
            # Use Factory for other products
            product = self.factory.create_product(product_type)
        self.catalog.add_product(product)

    def show_catalog(self):
        print("\nCatalog Products:")
        for product in self.catalog.get_products():
            print(product.details())
