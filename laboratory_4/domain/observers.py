class Observer:
    def update(self, product):
        pass

class InventoryObserver(Observer):
    def update(self, product):
        print(f"Inventory updated: {product.details()} added to stock")

class NotificationObserver(Observer):
    def update(self, product):
        print(f"Notification: New product {product.details()} is now available")