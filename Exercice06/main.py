# Fonction calculate_average
def calculate_average(numbers: list[int]) -> float:
    return sum(numbers)/len(numbers)


numbers = [10, 20, 30, 40, 50]

average = calculate_average(numbers)
print("La moyenne est :", average)
