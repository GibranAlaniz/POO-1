from numpy import array
import numpy as np

class arreglos:
    def __init__(self, v):
        self.arregloNP = np.array(v)
        self.arregloLista = [v]        
        
    #Insertar
    
    #Para listas
    def insertar(self, v):
        self.arreglosLista.append(v)
        
        
    #Para Numpy
    def insertarNP(self, v, i):
        self.arregloNP = np.insert(self.arregloNP, i , v)
    
    #Eliminar
    
    #Para listas
    def eliminar(self, i):
        self.arregloLista.pop(i)
    
    #Para Numpy
    def eliminarNP(self,i):
        self.arregloNP = np.delete(self.arregloNP, i)
        
     #modificar
     
     #Para lista
    def modificar(self, i, w):
        self.arregloLista[i] = w
        
    #Para tabla
    def modificarMP(self, i, v): 
        self.arregloMP[i] = v
    
     