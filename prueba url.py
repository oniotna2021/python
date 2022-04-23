import pandas as pd
c = pd.read_csv("https://raw.githubusercontent.com/danieljpadilla2011/publico/main/datosP87.csv",sep=';')
cdframe = pd.DataFrame(c)
print(cdframe)