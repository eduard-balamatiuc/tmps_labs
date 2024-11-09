class ProductCatalog:
    _instance = None
    _products = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProductCatalog, cls).__new__(cls)
            cls._instance._products = []
        return cls._instance

    def add_product(self, product):
        self._products.append(product)

    def get_products(self):
        return self._products
