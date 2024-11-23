class ProductCatalog:
    _instance = None
    _products = []
    _observers = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProductCatalog, cls).__new__(cls)
            cls._instance._products = []
            cls._instance._observers = []
        return cls._instance

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, product):
        for observer in self._observers:
            observer.update(product)

    def add_product(self, product):
        self._products.append(product)
        self.notify_observers(product)

    def get_products(self):
        return self._products