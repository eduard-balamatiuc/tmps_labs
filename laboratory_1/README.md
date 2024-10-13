# Laboratory Work 1 - SOLID Principles

**Author:** Eduard Balamatiuc

## Objectives

Implement 2 Principles of SOLID in a Python project.

## Implementation

For this Laboratory Work, I have implemented two principles of SOLID:

1. Single Responsibility Principle (SRP)
2. Open/Closed Principle (OCP)

I have created a simple application that calculates areas of different shapes. The application includes the following components:

- Shape classes (Circle, Rectangle)
- Area Calculator service
- Main script to demonstrate functionality

### SRP - Single Responsibility Principle

The Single Responsibility Principle is implemented by separating the concerns of different classes:

- **Shape classes** (Circle, Rectangle): Each shape class is responsible only for representing its specific shape and calculating its own area.
- **AreaCalculator**: This class is solely responsible for calculating the area of any given shape.
- **Main script**: Responsible for creating shape instances and using the AreaCalculator to display results.

### OCP - Open/Closed Principle

The Open/Closed Principle is implemented through the use of a common `Shape` abstract base class:

- The `Shape` class defines an abstract `area()` method.
- Specific shape classes (Circle, Rectangle) inherit from `Shape` and implement their own `area()` method.
- The `AreaCalculator` class is open for extension (new shapes can be added) but closed for modification (it doesn't need to change when new shapes are added).

## Project Structure

```
tmsp_labs
└── laboratory_1
    ├── __init__.py
    ├── main.py
    ├── models
    │   ├── __init__.py
    │   ├── circle.py
    │   ├── rectangle.py
    │   └── shape.py
    └── services
        ├── __init__.py
        └── area_calculator.py
```

## Key Components

### 1. `shape.py`

This file defines the abstract `Shape` class, which serves as a base for all shape classes:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

The `Shape` class uses Python's `abc` module to create an abstract base class with an abstract `area()` method. This enforces that all subclasses must implement their own `area()` method.

### 2. `circle.py`

The `Circle` class implements a specific shape:

```python
from .shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
```

This class inherits from `Shape` and provides its own implementation of the `area()` method, specific to circles.

### 3. `rectangle.py`

Similarly, the `Rectangle` class implements another shape:

```python
from .shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

### 4. `area_calculator.py`

The `AreaCalculator` class is responsible for calculating the area of any shape:

```python
from laboratory_1.models.shape import Shape

class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()
```

This class demonstrates both SRP and OCP. It has a single responsibility (calculating area) and is open for extension (works with any subclass of `Shape`) but closed for modification (doesn't need to change when new shapes are added).

### 5. `main.py`

The main script demonstrates the usage of the implemented classes:

```python
from laboratory_1.models.circle import Circle
from laboratory_1.models.rectangle import Rectangle
from laboratory_1.services.area_calculator import AreaCalculator

def main():
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)

    calculator = AreaCalculator()

    print(f'Circle area: {calculator.calculate_area(circle)}')
    print(f'Rectangle area: {calculator.calculate_area(rectangle)}')

if __name__ == "__main__":
    main()
```

This script creates instances of different shapes and uses the `AreaCalculator` to compute and display their areas.

## How to Run

To run the project:

1. Navigate to the `tmsp_labs` directory in your terminal.
2. Run the command: `python -m laboratory_1.main`

This will execute the main script and display the areas of a circle and a rectangle.

## Conclusions

Through the implementation of the Single Responsibility Principle and the Open/Closed Principle, the application has become more modular and extensible. Each class has a clear, single responsibility, making the code easier to understand and maintain. The use of an abstract base class for shapes allows for easy addition of new shapes without modifying existing code.

This project demonstrates how SOLID principles can be applied even in a simple application to create a more robust and flexible design. The separation of shapes into individual classes and the use of a generic `AreaCalculator` show how we can write code that's both focused in its responsibilities and open to future extensions.