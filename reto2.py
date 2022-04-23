def calculosalario(datos):
    horast=datos["cantidadHoras"]
    valorbase=datos["valorHora"]
    distanciakm=datos["distanciaVive"]
   
    
    if horast > 40:
        extra=horast-40
        valorbase2=valorbase*1.7
        valorextra=valorbase2*extra
        salariobase=valorbase*40
        salario=salariobase+valorextra
        
    
        
        if salario < 480000:
             
            if distanciakm >= 0 :
                if distanciakm <= 5 :
                        salario2=salario+salario*0.1

                if distanciakm > 5 :
                    if distanciakm < 20 :
                        salario2=salario+salario*0.15
         
                if distanciakm > 5 :
                    if distanciakm >= 20 :
                        salario2=salario+salario*0.20
        
        if salario >= 480000:
            if salario <= 816000:
                salarioimp=salario-salario*0.2
                if distanciakm >= 0 :
                    if distanciakm <= 5 :
                        salario2=salarioimp*1.05

                if distanciakm > 5 :
                    if distanciakm < 20 :
                        salario2=salarioimp*1.08
         
                if distanciakm >= 20 :
                        salario2=salarioimp*1.12


        if salario > 816000:
            salarioimp=salario*0.7
            if distanciakm >= 20 :
                salario2=salarioimp*1.06
        



        return salario2

    else:
        salario=valorbase*horast

        if salario < 480000:
             
                if distanciakm >= 0 :
                    if distanciakm <= 5 :
                        salario2=salario+salario*0.1

                if distanciakm > 5 :
                    if distanciakm < 20 :
                        salario2=salario+salario*0.15
         
                if distanciakm > 5 :
                    if distanciakm >= 20 :
                        salario2=salario+salario*0.20
        
        if salario >= 480000:
             if salario <= 816000:
                salarioimp=salario-salario*0.2
                if distanciakm >= 0 :
                    if distanciakm <= 5 :
                        salario2=salarioimp*1.05

                if distanciakm > 5 :
                    if distanciakm < 20 :
                        salario2=salarioimp*1.08
         
                if distanciakm >= 20 :
                        salario2=salarioimp*1.12


        if salario > 816000:
            salarioimp=salario*0.7
            if distanciakm >= 20 :
                salario2=salarioimp*1.06
        

        number= str(salario)
        
        
        return number

datos = {"nombreEmpleado":"Luis Iglesias","cantidadHoras":45,"valorHora":25000,"distanciaVive":25}    

print(calculosalario(datos))
print("El salario después de impuestos del empleado",datos["nombreEmpleado"],"es : $",calculosalario(datos))