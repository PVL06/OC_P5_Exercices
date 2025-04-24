
def square(number: int) -> int | None:
    try:
        return number ** 2
    except TypeError:
        print("Le paramètre doit être un nombre !")


print(square(4))
print(square("a"))
