 
def contaminantes (ruta_archivo, anio, codRes):
    try:
        import pandas as pd
        c = pd.read_csv(ruta_archivo,sep=';')
        frameres= pd.DataFrame(c)
        year=frameres['codAnio'].tolist()
      
        ciudad=frameres['CodCiud'].tolist()
        punmuestreo=frameres['PunMues'].tolist()
        local=frameres['Localidad'].tolist()
        caliper=frameres['Calibracion'].tolist()
        contador1=frameres['Cont1'].tolist()
       
        contador2=frameres['Cont2'].tolist()
        contador3=frameres['Cont3'].tolist()
        mes=frameres['Mes'].tolist()
        temper=frameres['Temperatura'].tolist()
        suma1=0
        suma2=0
        suma3=0
        tamaño=len(year)
        repet=0
        ciudadres1="hola"
        ciudadres2="hola"
        ciudadres3="hola"

        if codRes==3:
        
            mayor1=0
            mayor2=0
            mayor3=0

            for y in range(0,tamaño):
                if year[y]==anio:
                    if contador1[y]>=mayor1:
                        mayor1=contador1[y]
                        suma1=ciudad[y]
                      
            for y in range(0,tamaño):
                if year[y]==anio:
                    if contador2[y]>=mayor2:
                        mayor2=contador2[y]
                        suma2=ciudad[y]
                       
            for y in range(0,tamaño):
                if year[y]==anio:
                    if contador3[y]>=mayor3:
                        mayor3=contador3[y]
                        suma3=ciudad[y]
    
            respuesta=[suma1,suma2,suma3]
        
        
        if codRes==1:
            
            for y in range(0,tamaño):
                if year[y]==anio:
                    suma1=suma1+contador1[y]
                    suma2=suma2+contador2[y]
                    suma3=suma3+contador3[y]
            respuesta=[suma1,suma2,suma3]

        if codRes==2:
            for y in range(0,tamaño):
                if year[y]==anio:
                    repet=repet+1
                    suma1=suma1+contador1[y]
                    suma2=suma2+contador2[y]
                    suma3=suma3+contador3[y]
            
    
            suma1=suma1/repet
            suma2=suma2/repet
            suma3=suma3/repet
    
            respuesta=[suma1,suma2,suma3]



    except:
        respuesta="no se pudo"   
    
   
    
    

    
    
    

    
    return respuesta

codRes=3
anio=2015
ruta_archivo="https://raw.githubusercontent.com/danieljpadilla2011/publico/main/datosP87.csv"


print(contaminantes(ruta_archivo,anio,codRes))