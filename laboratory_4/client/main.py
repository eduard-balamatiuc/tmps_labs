from domain.facades import ProductManager
from domain.adapters import ThirdPartyLaptop, LaptopAdapter
from domain.decorators import ExtendedWarrantyDecorator, AccessoriesDecorator
from domain.observers import InventoryObserver, NotificationObserver

def main():
    # Create an instance of the ProductManager Facade
    manager = ProductManager()

    manager.catalog.add_observer(InventoryObserver())
    manager.catalog.add_observer(NotificationObserver())

    # Using Facade to add Samsung products
    manager.add_product("Smartphone", color="Blue", ram=4, storage=64)
    manager.add_product("TV", size=55)

    # Integrating a third-party product using Adapter
    third_party_laptop = ThirdPartyLaptop()
    adapted_laptop = LaptopAdapter(third_party_laptop)
    manager.catalog.add_product(adapted_laptop)

    # Using Decorator to add features to a product
    appliance = manager.factory.create_product("Appliance")
    decorated_appliance = ExtendedWarrantyDecorator(
        AccessoriesDecorator(appliance)
    )
    manager.catalog.add_product(decorated_appliance)

    # Display the catalog
    manager.show_catalog()

if __name__ == "__main__":
    main()
