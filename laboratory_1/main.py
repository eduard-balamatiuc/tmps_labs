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