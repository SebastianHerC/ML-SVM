import pandas as pd 

tablas= pd.read_html('https://es.wikipedia.org/wiki/Clasificaci%C3%B3n_de_Conmebol_para_la_Copa_Mundial_de_F%C3%BAtbol_de_1986')

tabla_resultados = pd.concat([tablas[25], tablas[27], tablas[28],tablas[30],tablas[46], tablas[45],tablas[44],tablas[43]])

tabla_resultados.to_csv('tabla_resultados1986.csv', index=False)

print("Datos almacenados en tabla_resultados.csv")