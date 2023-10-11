import operator
import re

opciones = {
    "+": operator.add, 
    "-": operator.sub, 
    "*": operator.mul, 
    "/": operator.truediv, 
    "%": operator.mod
    }

entrada = input()
lista = re.findall('[+-/*//]|\d+', entrada)

print(lista[1] > lista[3])
print(ord(lista[1]))
print(ord(lista[3]))

# r = 0.0
# count = 0
# for operation in range(int((lista.__len__() -1) / 2)):
#     op = operation+count+1; oper1 = operation+count; oper2 = operation+count+2

#     r = opciones[lista[op]](float(lista[oper1]), float(lista[oper2]))

#     lista[oper2] = r
#     count += 1

# print(int(r) if int(r) == r else r)
