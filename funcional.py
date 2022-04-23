"dos funciones envueltas"

def suma(val1=0, val2=0):
    return val1+val2

def operacion(funcion, val1=0, val2=0):
    return funcion(val1,val2)

funcion_suma=suma
resultado=operacion(suma,10,20)
print(resultado)

"creacion de una funcion"
def crear_funcion(operador):
    if operador =='+':
        def suma(val1=0 , val2=0):
            return val1+val2
        return suma

def operacion(funcion, val1=0, val2=0):
    return funcion(val1, val2)

funcion_suma=crear_funcion('+')
resultado=operacion(funcion_suma,10,20)
print(resultado)

"lambda"
suma=lambda val1=0, val2=0: val1 + val2
operacion=lambda operacion, val1=0, val2=0: operacion(val1,val2)
resultado=operacion(suma,10,20)
print(resultado)

con_valores= lambda val, val1=10 ,val2=10 : val+val1+val1
print(con_valores)

"""primer ejemplo map"""

def cuadrado(elemento=0):
    return elemento*elemento
lista=[1,2,3,4,5,6,7,8,9,10]
resultado=list(map(cuadrado,lista))
print(resultado)

"""map con lamda y funcion"""
def calculo(lista):
    resultado2=list(map(lambda elemento:elemento*elemento,lista))
    return resultado2

lista=[1,2,4,4,5,6,7,8,9,10]


print(calculo(lista))


"""map solo con lambda"""
lista2=[1,2,4,4,5,6,7,8,9,10]
resultado3=list(map(lambda elemento:elemento*elemento,lista2))
print(resultado3)

"""pow para potencias"""

from math import pow
numeros=[2,3,4]
potencias=[3,2,4]
potenciados=list(map(pow,numeros,potencias))
print(potenciados)

"""funcion filter"""
def mayor_a_cinco(elemento):
    return elemento>5
tupla=(5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado=tuple(filter(mayor_a_cinco,tupla))
print("la tupla de numeros mayores que 5 es: ",resultado)
resultado=len(resultado)
print("la cantidad de nuemero mayores de 5 es: ",resultado)

tupla2=(5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado=tuple(filter(lambda elemento:elemento>5,tupla2))
print("la tupla de numeros mayores que 5 es lambda: ",resultado)
resultado=len(resultado)
print("la cantidad de nuemero mayores de 5 es lambda: ",resultado)

tupla2=(5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado=tuple(filter(lambda elemento:elemento%2==0,tupla2))
print("la tupla de numeros pares es lambda: ",resultado)
resultado=len(resultado)
print("la cantidad de nuemero pares lambda: ",resultado)

"""pares usando filter lambda"""
items=(1,2,3,4,7,8,11,12,14,56,77)
pares=tuple(filter(lambda x: x % 2 ==0  ,items))
print("pares usando filter lambda: ",pares)

"""acumulador, sumar valores de una lista"""
from functools import reduce
lista=[1,2,3,4]
def funcion_acumulador(acumulador=0, elemento=0):
    return acumulador+elemento
resultado=reduce(funcion_acumulador,lista)
print(resultado)

"""acumulador con lambda"""
lista1=[1,2,3,4]
resultado2=reduce(lambda acumulador1=0 , elemento1=0:acumulador1 + elemento1, lista1)
print(resultado2)