def puntajeTotal (datos) -> str: 
    nombre=datos[0]
    rc=datos[1]
    ri=datos[2]
    rb=20-rc-ri
        
    total=5*rc-2*ri-rb

    reporte=str("El puntaje obtenido por el candidato "+nombre+" es: "+str(total))

    return reporte

datos=["Pedro Maya",15,2]

print(puntajeTotal(datos))