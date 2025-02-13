import math

class Figuras:
    def perimetro(nlados, lado):
        if nlados == 3:
            return lado * 3
        elif nlados == 4:
            return lado * 4
        elif nlados >= 5:
            return lado * nlados
        else:
            return None

    def area(nlados, lado):
        if nlados == 3:
            altura = math.sqrt((lado ** 2) - ((lado / 2) ** 2))
            return (lado * altura) / 2
        elif nlados == 4:
            return lado * lado
        elif nlados >= 5:
            return (nlados * lado ** 2) / (4 * math.tan(math.pi / nlados))
        else:
            return None

    def calcular(nlados, lado):
        p = Figuras.perimetro(nlados, lado)
        a = Figuras.area(nlados, lado)
        return f"El perímetro de la figura es {p} y el área es {a}"

print(Figuras.calcular(3, 5))


