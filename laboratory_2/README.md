# Laboratory Work - Creational Design Patterns

**Author:** Eduard Balamatiuc

---

## Objectives

- Get familiar with Creational Design Patterns (CDPs).
- Choose a specific domain.
- Implement at least 3 CDPs in a Python project.

## Domain Choice

For this project, I selected the manufacturing domain, specifically focusing on a tech manufacturer like Samsung. Samsung is known for producing various electronic devices, from smartphones to TVs, and this diversity aligns well with using multiple creational design patterns.

## Used Design Patterns

1. Singleton
2. Builder
3. Factory Method

## Implementation

In this project, the manufacturing process includes models for different products (e.g., Smartphone, Tablet) and utilizes three creational design patterns to handle product creation efficiently.

### Singleton Pattern

The **Singleton** pattern is used to manage a single, shared product catalog across the system.

- **Singleton Concept**: Ensures that there is only one instance of the `ProductCatalog` class throughout the application.
- **Implementation**: The `ProductCatalog` class contains a method to add products, keeping track of all available products.

Example:
```python
class ProductCatalog:
    _instance = None
    _catalog = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProductCatalog, cls).__new__(cls)
        return cls._instance

    def add_product(self, product):
        self._catalog.append(product)
```

### Builder Pattern

The **Builder** pattern is used to construct complex product objects step-by-step.

- **Builder Concept**: This pattern separates the construction of a complex object (e.g., `Smartphone`) from its representation, allowing for creating different types of smartphones with various configurations.
- **Implementation**: The `SmartphoneBuilder` class defines methods for setting attributes like screen size, RAM, and battery. The `build()` method then returns the constructed smartphone.

Example:
```python
class SmartphoneBuilder:
    def __init__(self):
        self._product = Smartphone()

    def set_screen_size(self, size):
        self._product.screen_size = size
        return self

    def set_ram(self, ram):
        self._product.ram = ram
        return self

    def set_battery(self, battery):
        self._product.battery = battery
        return self

    def build(self):
        return self._product
```

### Factory Method Pattern

The **Factory Method** pattern is used to create specific types of products without specifying their exact class.

- **Factory Method Concept**: This pattern allows for deferring the instantiation of the exact type of product to a factory.
- **Implementation**: The `ProductFactory` contains a `create_product` method that returns an instance of a specific product based on the provided type.

Example:
```python
class ProductFactory:
    def create_product(self, product_type):
        if product_type == "smartphone":
            return Smartphone()
        elif product_type == "tablet":
            return Tablet()
        else:
            raise ValueError("Unknown product type")
```

## Project Structure

```
laboratory_2
├── client
│   ├── main.py
│   └── __init__.py
├── domain
│   ├── products.py
│   ├── builders.py
│   └── __init__.py
├── factory
│   ├── product_factory.py
│   └── __init__.py
├── singleton
│   ├── singleton.py
│   └── __init__.py
└── README.md
```

## Key Components

### 1. `singleton.py`

Defines a `ProductCatalog` class that follows the Singleton pattern.

```python
class ProductCatalog:
    _instance = None
    _catalog = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProductCatalog, cls).__new__(cls)
        return cls._instance

    def add_product(self, product):
        self._catalog.append(product)

    def list_products(self):
        return self._catalog
```

### 2. `builders.py`

Contains the `SmartphoneBuilder` class which uses the Builder pattern to construct `Smartphone` objects.

```python
class SmartphoneBuilder:
    def __init__(self):
        self._product = Smartphone()

    def set_screen_size(self, size):
        self._product.screen_size = size
        return self

    def set_ram(self, ram):
        self._product.ram = ram
        return self

    def set_battery(self, battery):
        self._product.battery = battery
        return self

    def build(self):
        return self._product
```

### 3. `product_factory.py`

Implements a `ProductFactory` class to create products based on the specified type, following the Factory Method pattern.

```python
class ProductFactory:
    def create_product(self, product_type):
        if product_type == "smartphone":
            return Smartphone()
        elif product_type == "tablet":
            return Tablet()
        else:
            raise ValueError("Unknown product type")
```

### 4. `main.py`

The `main.py` file demonstrates the usage of the different classes and design patterns.

```python
from factory.product_factory import ProductFactory
from singleton.singleton import ProductCatalog
from domain.builders import SmartphoneBuilder

def main():
    # Singleton usage
    catalog = ProductCatalog()
    
    # Factory Method usage
    factory = ProductFactory()
    smartphone = factory.create_product("smartphone")
    
    # Builder usage
    builder = SmartphoneBuilder()
    custom_phone = builder.set_screen_size(6.5).set_ram(8).set_battery(4500).build()

    # Add products to catalog
    catalog.add_product(smartphone)
    catalog.add_product(custom_phone)

    # Display catalog
    print("Catalog products:")
    for product in catalog.list_products():
        print(product)

if __name__ == "__main__":
    main()
```

## How to Run

1. Navigate to the `laboratory_2` directory in the terminal.
2. Run the command `python -m client.main` to see the output.

## Conclusions

This project demonstrates the flexibility and modularity brought by the Singleton, Builder, and Factory Method patterns. Each pattern addresses a specific aspect of object creation:

1. **Singleton** ensures a single instance of a shared catalog.
2. **Builder** provides an organized way to construct complex products.
3. **Factory Method** abstracts the instantiation process, allowing easy addition of new product types without modifying existing code.

By applying these creational design patterns, the project is both extensible and well-organized, making it adaptable for future expansion or integration with additional product types.