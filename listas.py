nombres=[]
edades=[]
for x in range(5):
    nom=input("Ingrese el nombre de la persona:")
    nombres.append(nom)
    ed=input("Ingrese la edad de la persona:")
    edades.append(ed)

print("nombres de las pesonas mayores de edad:")
for x in range(5):
    
    if edades[x] >= str(18):
        print(nombres[x])

t2 = ('a',)
print(type(t2))
