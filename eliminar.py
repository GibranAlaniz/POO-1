class Lista:
    def __init__(self):
        self.arregloLista = [2, 3, 5]

    def eliminar(self, indice):
        if 0 <= indice < len(self.arregloLista):
            self.arregloLista.pop(indice)
            print(f"El nuevo arreglo es {self.arregloLista}")
        else:
            print("Índice inexistente")

lista = Lista()
indice = int(input("Ingrese el índice a remover: "))
lista.eliminar(indice)
