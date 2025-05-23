
class Rectangle:
    def __init__(self, width, length) -> None:
        self.width = width
        self.length = length

    def calculate_area(self) -> int | float:
        return self.width * self.length

    def calculate_perimeter(self) -> int | float:
        return 2 * (self.width + self.length)


rectangle = Rectangle(5, 3)  # 5:width & 3:length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
