# Behavioral Design Patterns

**Author:** Eduard Balamatiuc

---

## Objectives:
- Implement behavioral design patterns to manage communication between objects
- Extend the previous laboratory work with new functionalities
- Implement at least one behavioral design pattern

## Used Design Pattern:
- Observer Pattern

---

## Implementation Details

### 1. Observer Pattern Core Components

#### Base Observer Interface
```python
class Observer:
    def update(self, product):
        pass
```
This abstract base class defines the contract that all concrete observers must follow. The `update` method is intentionally left empty as it serves as an interface that concrete observers will implement according to their specific notification needs.

#### Concrete Observers
```python
class InventoryObserver(Observer):
    def update(self, product):
        print(f"Inventory updated: {product.details()} added to stock")

class NotificationObserver(Observer):
    def update(self, product):
        print(f"Notification: New product {product.details()} is now available")
```
Each concrete observer implements the `update` method differently:
- `InventoryObserver`: Simulates updating inventory records
- `NotificationObserver`: Simulates sending notifications to interested parties

The observers use the `product.details()` method, which was already implemented in our product classes from the previous laboratory work, maintaining consistency across the system.

### 2. Subject Implementation (ProductCatalog)

```python
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
```
The `ProductCatalog` maintains its singleton pattern from the previous implementation while adding observer functionality. The `_observers` list is initialized in `__new__` to ensure it's created only once, maintaining the singleton's integrity.

```python
    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, product):
        for observer in self._observers:
            observer.update(product)

    def add_product(self, product):
        self._products.append(product)
        self.notify_observers(product)
```
Key methods:
- `add_observer`: Registers new observers to the notification list
- `notify_observers`: Iterates through all observers and calls their `update` method
- `add_product`: Enhanced to trigger notifications after adding a product

### 3. Integration with Existing Architecture

```python
def main():
    manager = ProductManager()
    
    # Initialize observers
    manager.catalog.add_observer(InventoryObserver())
    manager.catalog.add_observer(NotificationObserver())

    # Product additions with different creation patterns
    manager.add_product("Smartphone", color="Blue", ram=4, storage=64)  # Uses Builder
    manager.add_product("TV", size=55)  # Direct instantiation
    
    # Adapter pattern integration with observer
    third_party_laptop = ThirdPartyLaptop()
    adapted_laptop = LaptopAdapter(third_party_laptop)
    manager.catalog.add_product(adapted_laptop)  # Triggers observers
    
    # Decorator pattern with observer
    appliance = manager.factory.create_product("Appliance")
    decorated_appliance = ExtendedWarrantyDecorator(
        AccessoriesDecorator(appliance)
    )
    manager.catalog.add_product(decorated_appliance)  # Triggers observers
```

The integration showcases how the Observer pattern works seamlessly with:
- Builder Pattern (Smartphone creation)
- Direct instantiation (TV creation)
- Adapter Pattern (Third-party laptop)
- Decorator Pattern (Appliance with extensions)

## Design Decisions and Their Implications

1. **Singleton Maintenance**
   - The observer list is part of the singleton instance
   - Ensures all parts of the system work with the same observers
   - Prevents multiple notification systems from existing

2. **Observer Implementation**
   - Kept observers simple with print statements for demonstration
   - In a real system, these would connect to actual inventory systems or notification services
   - Easy to extend with new observer types without modifying existing code

3. **Integration with Existing Patterns**
   - Observer pattern complements existing structural patterns
   - Notifications work regardless of how products are created or modified
   - Maintains single responsibility principle while adding new functionality

## How to Run

1. Navigate to the `laboratory_4` directory in the terminal.
2. Run the command `python -m client.main` to see the output and how the observtry pattern wokrs through the notification system.

## Conclusions

The Observer pattern implementation successfully:
- Added real-time notification capabilities
- Maintained existing design pattern functionality
- Provided a flexible foundation for future extensions

The pattern's integration demonstrtes how behavioral patterns can enhance structural patterns without compromising their benefits or increasing coupling.

This implementation shows practical application of the Observer pattern while maintining clean architecture and demonstrating how different design patterns can work together in a cohesive system.