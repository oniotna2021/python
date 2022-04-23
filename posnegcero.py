num=int(input("Introduzca el numero: "))

if num > 0:
    print("el numero ",num,"es positivo")
elif num < 0:
    print("el numero ",num,"es negativo")
else:
    print("el numero ",num,"es neutro")

if num%2 == 0 :
    print('num es par')
else :
    print('num es inpar')

num1=int(input("Introduzca el numero 1: "))
num2=int(input("Introduzca el numero 2: "))

if num1 > num2 :
    print("num1 es mayor de num2")
else:
    print("num2 es mayor de num1")

    """ se puede comparar caracteres con comilla simple '' """

letra = 'a'

if letra == 'a':
    print('La letra es a')
else:
    print('La letra es distinta de a')

""" practica de la estructura try except"""

temperatura_fahr = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(temperatura_fahr)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print("La temperatura en celcius es: ",cel)
except:
    print('Please enter a number')

""" Valor de una cadena de caracteres cero es la primera posicion """

fruta = 'fresa'
longitud=len(fruta)
print(longitud)
letra = fruta[1]
print(letra)
print(fruta[0:3])

saludo = '¡Hola, mundo!'
nuevo_saludo = 'J' + saludo[1:]
print(nuevo_saludo)

""" operador in """
'a' in 'banana'

"ola" in "banana"

""" orden """

palabra='carro'
if palabra < 'banana':
    print('Tu palabra,' + palabra + ', viene antes de banana')
elif palabra > 'banana':
    print('Su palabra,' + palabra + ', viene después de banana.')
else:
    print('Está bien, su palabra es banana')

""" transformar a mayuscula """
palabra_nueva = palabra.upper()
print(palabra_nueva)

""" posicion de una letra en la palabra"""
letra = input('introduzca la letra: ')
index = palabra.find(letra)
print("la posicion de su letra es: ",index)

"""elimnimar espacios"""
linea = '        Aquí vamos            '
linea.strip()

