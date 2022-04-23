db_connection = "127.0.0.1","5432","root","nomina"

for parametro in db_connection:
    print(parametro)
else:
    print("""El comando PostgreSQL es: 
$ psql -h {server} -p {port} -U {user} -d {db_name}""".format(
        server=db_connection[0], port=db_connection[1], 
        user=db_connection[2], db_name=db_connection[3]))


lista = [1, 2.5, 'DevCode', [5,6] ,4]

print(lista[0]) # 1
print(lista[1]) # 2.5
print(lista[2]) # DevCode
print(lista[3]) # [5,6]
print(lista[3][0]) # 5
print(lista[3][1]) # 6
print('Hicimos este cambio ->',lista[1:4]) # [2.5, 'DevCode']
print(lista[1:6]) # [2.5, 'DevCode', [5, 6], 4]
print(lista[1:6:2]) # [2.5, [5, 6]]
print("Hola Estructura de Lenguajes")