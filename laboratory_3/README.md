Structural Design Patterns

Author: Eduard Balamatiuc

---

**Objectives:**
- Get familiar with Structural Design Patterns (SDPs).
- Continue working on the domain from the previous lab.
- Implement at least 3 SDPs for this domain.

**Used Design Patterns:**
1. Adapter Pattern
2. Decorator Pattern
3. Facade Pattern

---

**Implementation**

In this lab, I extended my previous project by implementing three structural design patterns to enhance functionality.

1. **Adapter Pattern**

I used the Adapter Pattern to integrate third-party products into my system. This pattern lets incompatible interfaces work together by wrapping the incompatible class with an adapter that implements the expected interface.

For instance, I had a `ThirdPartyLaptop` class with a different interface. To adapt it, I created a `LaptopAdapter`:

```python
class LaptopAdapter(SamsungProduct):
    def __init__(self, third_party_laptop):
        self.laptop = third_party_laptop

    def details(self):
        return self.laptop.get_specifications()
```

This adapter makes the third-party laptop compatible with my `SamsungProduct` interface, allowing it to be added to the product catalog seamlessly.

2. **Decorator Pattern**

The Decorator Pattern was implemented to add new functionalities to existing products at runtime without altering their structure.

I created a base decorator class:

```python
class ProductDecorator(SamsungProduct):
    def __init__(self, product):
        self.product = product

    def details(self):
        return self.product.details()
```

Then, I made concrete decorators like `ExtendedWarrantyDecorator`:

```python
class ExtendedWarrantyDecorator(ProductDecorator):
    def details(self):
        return f"{self.product.details()} + Extended Warranty"
```

This way, I could dynamically add features like extended warranties or accessories to products.

3. **Facade Pattern**

To simplify the complex interactions within the system, I applied the Facade Pattern by creating a `ProductManager` class. This class provides a simple interface for the client code to interact with the subsystem.

Here's a part of the `ProductManager`:

```python
class ProductManager:
    def __init__(self):
        self.catalog = ProductCatalog()
        self.factory = ProductFactory()

    def add_product(self, product_type, **kwargs):
        ...

    def show_catalog(self):
        ...
```

By using the facade, the client code doesn't need to interact with multiple classes directly.

---

**Conclusions / Screenshots / Results**

By working on this lab, I learned how structural design patterns can improve the architecture of a software system. They help in organizing code, promoting reusability, and making the system more adaptable to changes.

- The **Adapter Pattern** allowed me to integrate external products without modifying existing code.
- With the **Decorator Pattern**, I could add features to products dynamically, improving flexibility.
- The **Facade Pattern** simplified the interface for clients, making the system more user-friendly.

---

**Sample Output:**

```
Catalog Products:
Samsung Smartphone [Color: Blue, RAM: 4GB, Storage: 64GB]
Samsung TV [Size: 55"]
Third-Party Laptop [Specs: Intel i7, 16GB RAM, 512GB SSD]
Samsung Appliance with energy-efficient technology. + Extended Warranty + Additional Accessories
```

This output shows that the products, including the adapted third-party laptop and the decorated appliance, are all integrated into the catalog successfully.

