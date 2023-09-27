import pandas as pd 

tablas= pd.read_html('https://es.wikipedia.org/wiki/Chile_en_la_clasificaci%C3%B3n_de_Conmebol_para_la_Copa_Mundial_de_F%C3%BAtbol_de_1982')


tabla_resultados = pd.concat([tablas[4], tablas[5], tablas[6],tablas[7]])

tabla_resultados.to_csv('tabla_resultados1982.csv', index=False)

print("Datos almacenados en tabla_resultados.csv")