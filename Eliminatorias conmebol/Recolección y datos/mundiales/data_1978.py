import pandas as pd 

tablas= pd.read_html('https://es.wikipedia.org/wiki/Clasificaci%C3%B3n_de_Conmebol_para_la_Copa_Mundial_de_F%C3%BAtbol_de_1978')

tabla_resultados = pd.concat([tablas[18], tablas[19], tablas[21],tablas[22]])

tabla_resultados.to_csv('tabla_resultados1978.csv', index=False)

print("Datos almacenados en tabla_resultados.csv")