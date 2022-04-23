n = 5
while n > 0:
    print(n)
    n = n - 1
print('Despegue!')

def factorial(n: int) -> int:
    resultado = 1
    numero_actual = 2
    while numero_actual <= n:
        resultado = resultado * numero_actual
        numero_actual += 1
    return resultado

print(factorial(4))

i = 1
while i < 10:
    i = i + 1
    print(i)
    
print("Terminé")

"""bucle sin else"""
promedio, total, contar = 0.0, 0, 0
print("Introduzca la nota de un estudiante (-1 para salir): ")
grado = int(input())
while grado != -1:
    total = total + grado
    contar = contar + 1
    print("Introduzca la nota de un estudiante (-1 para salir): ")
    grado = int(input())
promedio = total / contar
print("Promedio de notas del grado escolar es: " + str(promedio))


"""bucle con else y mensaje repetido"""
promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "
grado = int(input(mensaje))
while grado != -1:
    total = total + grado
    contar += 1
    grado = int(input(mensaje))
else:
    promedio = total / contar
    print("Promedio de notas del grado escolar: " + str(promedio))

    variable = 10


"""bucle con brinco"""
while variable > 0:
    variable = variable -1
    if variable == 5:
        continue
    print('Actual valor de variable:', variable) # no imprime el 5

"""sucesion de fibonacci"""
a, b = 0, 1
while b < 100:
    print(b),
    a, b = b, a + b

"""for con rango"""
for x in range(0, 3):
    print("Estamos en la iteración " + str(x))

"""rango con incremento de 2"""
for j in range(0, 10, 2):
    print("Estamos en la iteración " + str(j))

"""rango con decremento de 2"""
for j in range(10, 0, -2):
    print("Estamos en la iteración " + str(j))

"""bucle con diccionarios"""
datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}
clave = datos_basicos.keys()
valor = datos_basicos.values()
cantidad_datos = datos_basicos.items()

for clave, valor in cantidad_datos:
    print(clave + ": " + valor)