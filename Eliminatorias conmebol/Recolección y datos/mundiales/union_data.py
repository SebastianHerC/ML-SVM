import pandas as pd
import os


archivos_csv = ['tabla_resultados1958.csv', 
                'tabla_resultados1966.csv', 
                'tabla_resultados1970.csv',
                'tabla_resultados1974.csv',
                'tabla_resultados1978.csv',
                'tabla_resultados1982.csv',
                'tabla_resultados1986.csv',
                'tabla_resultados1990.csv',
                'tabla_resultados1998.csv',
                'tabla_resultados2002.csv',
                'tabla_resultados2006.csv',
                'tabla_resultados2010.csv',
                'tabla_resultados2014.csv',
                'tabla_resultados2018.csv',
                'tabla_resultados2022.csv',]

directorio = 'C:/Users/seba-/Desktop/Python/OTROS/Machine learning/Eliminatorias conmebol'


datos_combinados = pd.DataFrame()


for archivo in archivos_csv:
    ruta_completa = os.path.join(directorio, archivo)
    datos = pd.read_csv(ruta_completa)
    datos_combinados = pd.concat([datos_combinados, datos], ignore_index=True)


datos_combinados.to_csv('data.csv', index=False)

print("Los datos se han combinado y guardado en 'datos_combinados.csv'")
