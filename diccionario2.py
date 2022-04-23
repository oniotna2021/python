""" largo de cadena"""
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

print(len(usuario))
print(len(usuario["skills"]))

"""borrar clave de la cadena"""

versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
print(versiones)
del versiones["python"]
print(versiones)