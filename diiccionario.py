"""diccionario"""

def promedionotas(nota1, nota2, nota3, nota4):
    promedio=round((nota1+nota2+nota3+nota4)/4, 2)
    return promedio

print("el promedio de notas es",promedionotas(3.0,2.1,5.0,4.7))

"""encapsulamiento con diccionario"""
def promedionotas(dicnotas):
    sumatoria1=dicnotas["nota 1"]
    sumatoria2=dicnotas["nota 2"]
    sumatoria3=dicnotas["nota 3"]
    sumatoria4=dicnotas["nota 4"]
    promedio=round((sumatoria1 + sumatoria2 + sumatoria3 + sumatoria4)/4, 2)
    return promedio

""" dicnotas toma los datos por pantalla hecho por mi 
dicnotas={}
dicnotas["nota 1"]= int(input('introduzca la nota1: '))
dicnotas["nota 2"]= int(input('introduzca la nota2: '))
dicnotas["nota 3"]= int(input('introduzca la nota3: '))
dicnotas["nota 4"]= int(input('introduzca la nota4: ')) """


""" otra sintaxis para escribir dicnotas"""
dicnotas={
    "nota 1":3.0,
    "nota 2":4.0,
    "nota 3":5.0,
    "nota 4":6.0,
}
print("el promedio de notas es:",promedionotas(dicnotas))


""" reportar promedio con nombre de estudiante 

def reportarpromedio(dicreporte):
    return dicreporte["estudiante"]+"="+str(dicreporte["promedio"])
    
def generareporte(dicnotas):
    sumatoria=0
    sumatoria +=dicnotas["nota 1"]
    sumatoria +=dicnotas["nota 2"]
    sumatoria +=dicnotas["nota 3"]
    sumatoria +=dicnotas["nota 4"]
    promedio=round(sumatoria/4, 2)
    reportenotas = {
                    "promedio":promedio, 
                    "estudiante":dicnotas["estudiante"]
                    }   
    
    return reportenotas

    dicnotas={
                "nota 1":3.0,
                "nota 2": 4.0,
                "nota 3": 5.0,
                "nota 4": 6.0,
                "estudiante":"antonio",
            }

print(reportarpromedio(generareporte(dicnotas)))"""

otrodiccionario = {"copia": 123.23}
print(otrodiccionario["copia"])

diccionarioEjemploExcel ={"nombre":5+2,"telefono":3363692, "edad":33, "ciudad":"Pereira"}
print(diccionarioEjemploExcel["nombre"])

diccionario = dict(total= 55, descuento= True, subtotal= 15)
print(diccionario["total"])

usuario = {
    'nombre': 'Nombre del usuario',
    'edad' : 23, 
    'curso': 'Curso de Python',
    'skills':{
        'programacion' : True,
        'base_de_datos': False
    },
    'No medallas' : 10
}

print(usuario["skills"]["programacion"])

diccionario = {
     "clave1":234,
     "cadena":True,
     "clave3":"Valor 1",
}
print(diccionario)
print(type(diccionario))

versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones)
"""resetear una variable"""
versiones.clear()
print(versiones)

versiones = dict(python=2.7, zope=2.13, plone=5.1)
versiones.get('plone')
print(versiones.get('plone'))
print(versiones["plone"])

versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones.items())

versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones.pop('zope'))

versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones)
versiones_adicional = dict(django=2.1)
versiones.update(versiones_adicional)
print(versiones)

