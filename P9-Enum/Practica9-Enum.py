from enum import Enum

class Consecutive(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5

print(Consecutive.Martes)
print(Consecutive.Martes.value)
print(type(Consecutive.Martes))
print(type(Consecutive.Martes.value))