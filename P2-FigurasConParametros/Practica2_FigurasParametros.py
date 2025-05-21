import math
class figura():
    def AreaFigura (nlados, medida):
        if nlados == 3:
            area = (math.sqrt(3) / 4) * (medida ** 2)
            print("el aréa del triangulo es: ", area)
        elif nlados == 4:
            area = medida * medida
            print("el aréa del cuadrado es: ", area)
        elif nlados == 5:
            p = medida * 5
            a = medida / 1.45
            area = (p * a) / 2
            print("el aréa del pentagono es: ", area)
    def PerimetroFigura(nlados, medida):
        if nlados == 3:
            perimetro = nlados*medida
            print("el perimetro del trianfulo es: ", perimetro)
        elif nlados == 4:
            perimetro = nlados*medida
            print("el perimetro del cuadrado es: ", perimetro)
        elif nlados == 5:
            perimetro = nlados*medida
            print("el perimetro del pentagono es: ", perimetro)

figura.AreaFigura(3, 4)
figura.PerimetroFigura(3, 4)
            