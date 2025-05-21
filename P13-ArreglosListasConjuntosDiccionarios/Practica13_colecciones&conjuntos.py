A = {1,3,5,6,7}
B = {78,9,8,12}
U = B.union(A) # Se puede usar tambien A | B
print(U)

print("------------------")

conA = {23, 54, 79, 1 , 2, 3, 4}
conB = {45, 66, 89, 1, 2, 3, 4}
I = conB.intersection(conA) #Se peude usar tambien A & B
print(I)

print("------------------")

conjuntoA = {45, 66, 89, 1, 2, 3, 4}
conjuntoB = {23, 54, 79, 1 , 2, 3, 4}
D = conjuntoA.difference(conjuntoB) #Se peude usar tambien A - B
print(D)

print("-------------------------------------------------------------------------------------")

cA = {45, 66, 89, 1, 2, 3, 4}
cB = {23, 54, 79, 1 , 2, 3, 4}
DS = cA.symmetric_difference(cB) #Se peude usar tambien A ^ B
print(DS)

print("_____________________________________________________________________________________")

dic = {
   'x': "equis",
   'y': "ye",
   'd': "De"
}
dic2 = dict(x="equis", y="ye", d="de")

print(dic.get('x'))
print(dic.get('z'))
dic['x'] = "equisD"
dic['z'] = "Zeta"

del dic['y']
x = dic.get('y')
print(x)
print('x' in dic)
llaves = dic.keys()
print(llaves)
valores = dic.values()
p = dic.items()
print(p)