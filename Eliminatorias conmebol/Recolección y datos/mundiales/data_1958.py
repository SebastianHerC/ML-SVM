import pandas as pd 

tablas= pd.read_html('https://es.wikipedia.org/wiki/Clasificaci%C3%B3n_de_Conmebol_para_la_Copa_Mundial_de_F%C3%BAtbol_de_1958#Grupo_2')


tabla_resultados = pd.concat([tablas[6], tablas[7], tablas[9],tablas[10]])

tabla_resultados.to_csv('tabla_resultados1958.csv', index=False)

print("Datos almacenados en tabla_resultados.csv")