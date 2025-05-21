from enum import Enum

class Dias(Enum):
    LUNES = "lunes"
    MARTES = "martes"
    MIERCOLES = "miércoles"
    JUEVES = "jueves"
    VIERNES = "viernes"
    SABADO = "sábado"
    DOMINGO = "domingo"

def validar_dia(dia):
    if not isinstance(dia, Dias):
        raise TypeError("Error: El valor no es un miembro de la enumeración Dias")
    print(f"Valor correcto: {dia.value}")

contador = 0

while contador < 5:
    try:
        entrada = input("Ingrese un día de la semana en minúsculas: ")
        dia_enum = Dias(entrada)
        validar_dia(dia_enum)
    except ValueError:
        print("Error: Día no válido.")
    except TypeError as e:
        print(e)
    finally:
        contador += 1
        print(f"Intento {contador}/5 completado.")

print("Fin del programa.")
