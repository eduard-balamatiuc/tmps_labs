from factory.product_factory import ProductFactory
from singleton.singleton import ProductCatalog
from domain.builders import SmartphoneBuilder

# Singleton Example
catalog = ProductCatalog()

# Factory Method Example
smartphone = ProductFactory.create_product("Smartphone")
tv = ProductFactory.create_product("TV")
appliance = ProductFactory.create_product("Appliance")

catalog.add_product(smartphone)
catalog.add_product(tv)
catalog.add_product(appliance)

print("Catalog Products:")
for product in catalog.get_products():
    print(product.details())

# Builder Example
custom_smartphone = (
    SmartphoneBuilder()
    .set_color("Black")
    .set_ram(8)
    .set_storage(128)
    .build()
)
catalog.add_product(custom_smartphone)
print("\nCustom Smartphone:", custom_smartphone)
