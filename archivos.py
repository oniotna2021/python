#guardado de archivos

import pandas as pd

data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

datosDataFrame = pd.DataFrame(data)

print(datosDataFrame)

#Acaba la implementacion

datosDataFrame.to_csv('example2.csv')
""",sep=';'"""

#lectura de archivos

df = pd.read_csv('example.csv')
df

# sin cabecera
df = pd.read_csv('example.csv', header=None)
df

# eliminar columnas
df = pd.read_csv('example.csv',
                 skiprows = 1,
                 names=['UID', 'First Name', 'Last Name', 'Age', 'Sales #1', 'Sales #2'])
print(type(df['Sales #2'][2]))

#ignorar valores nulos

df = pd.read_csv('example.csv',
                 skiprows=1,
                 names=['UID', 'First Name', 'Last Name', 'Age', 'Sales #1', 'Sales #2'],
                 na_values=['?'],
                 index_col=['First Name', 'Last Name'])
print(df)