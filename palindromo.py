numero=222
centena=numero//100
decena=(numero-centena*100)//10
unidad=numero-centena*100-decena*10

print(centena)
print(decena)
print(unidad)
def palidromo(numero:int)->bool:
    centena=numero//100
    decena=(numero-centena*100)//10
    unidad=numero-centena*100-decena*10

    if centena == unidad:
        resultado = True
    else:
        resultado = False
    return resultado
    
   

def espar(numero:int)->bool:
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado

def clasificar_chocolate(codigo:int)->str:
    if palidromo(codigo):
        if espar(codigo):
            resultado = "SWEET"
        else:
            resultado = "BITTER"
    else:
        if espar(codigo):
            resultado = "CINNAMON"
        else:
            resultado = "LIGHT"
    return resultado            

print(clasificar_chocolate(123))
print(clasificar_chocolate(222))   
print(clasificar_chocolate(111))
print(clasificar_chocolate(505)) 
print(clasificar_chocolate(576)) 