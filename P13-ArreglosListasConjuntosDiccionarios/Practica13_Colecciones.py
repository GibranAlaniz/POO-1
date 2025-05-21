import numpy as np
lista_mixta = [
    42,
    42,                  
    3.14,               
    "Hola mundo",        
    True,                
    [1, 2, 3],           
    None                 
]
    
print("Lista mixta: ", lista_mixta)

lista_np = np.array([1,2,3,4,5,5])

print("lista numpy: ", lista_np)

print("##############################")
print("_________-De lista a Tuplas________")
print("##############################")

tupla_lista = tuple(lista_mixta)

print("tupla_lista: ",tupla_lista)

tupla_lista_np = tuple(lista_np)

print("tupla_lista_np: ", tupla_lista_np)

print("##############################")
print("___________De lista a conjuntos____________")
print("##############################")

conjunto_lista_np = set(lista_np)

print("conjunto_lista_np: ", conjunto_lista_np)

conjunto_lista_mixta = set(lista_mixta[:5])

print("conjunto_lista_mixta: ", conjunto_lista_mixta)

print("##############################")
print("#        Diccionario         #")
print("##############################")
persona = {
    "nombre": "Gibran Alaniz",          
    "edad": 18,                           
    "altura": 1.75,                       
    "es_estudiante": True,                
    "cursos": ["Python", "Data Science"]  
}

print("Diccionario: ", persona)

#Falta lo del append, pop, ...

lista = [22, "mayo", 2.006, True, "Gibran", 777, 666, "pokemon"]

print("##############################")
print("#          append            #")#Insertar elemento hasta el final
print("##############################")

lista.append(888)
print(lista)

print("##############################")
print("#          Insert            #")#Instertar elemento en una parte especifica de la lista
print("##############################")

lista.insert(1, "Hola")
print(lista)

print("##############################")
print("           Extend             ")#Atascar una lista dentro de ottra lista
print("##############################")

lista.extend([1, "Hola"])
print(lista)

print("##############################")
print("#          Index             #")#Saber en que posicion esta un elemento en la lista
print("##############################")

print(lista)
print(lista.index(True))

print("##############################")
print("#          Count             #")#Conocer cuantas veces está x valor en la lista
print("##############################")

print(lista)
print(lista.count(1))

print("##############################")
print("#          In list           #")#Pa saber si un valor existe en la lissta
print("##############################")

x = (22 in lista)
print(x)