import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error


ruta = 'MarathonData.csv'
data = pd.read_csv(ruta)

print(data['Name'])

#info de los datos
print(data.info())
print('______________________________________________________')
#pasar los datos de la columna Wall21 de objeto a numerico
data['Wall21'] =pd.to_numeric(data['Wall21'], errors='coerce')
print(data.info())
print('______________________________________________________')
#Obtener información de la data
print(data.describe())
print('______________________________________________________')
#distribución de los datos
print(data.hist)
for columna in data.columns:
    # Verifica si la columna es de tipo numérico (int64 o float64)
    if data[columna].dtype in ['int64', 'float64']:
        data[columna].hist()
        plt.xlabel(columna)
        plt.ylabel('Frecuencia')
        plt.title(f'Distribución de {columna}')
        plt.show()
print('______________________________________________________')
#eliminar las columnas que no son utiles para la ML
data = data.drop(columns=['Name'])
data = data.drop(columns=['id'])
data = data.drop(columns=['Marathon'])
data = data.drop(columns=['CATEGORY'])
print(data)
print('______________________________________________________')
#cuantos datos nulos existen
print(data.isna().sum())
print('______________________________________________________')
#rellenear con 0 y reemplazo de datos
data['CrossTraining'] =data['CrossTraining'].fillna(0)
data=data.dropna(how='any')
print(data)
print('______________________________________________________')
#codificar los datos no numericos a numericos
print(data['CrossTraining'].unique())
valores_cross = {"CrossTraining":  {'ciclista 1h':1, 'ciclista 3h':2, 'ciclista 4h':3, 'ciclista 5h':4, 'ciclista 13h':5}}
data.replace(valores_cross, inplace=True)
valores_categoria = {"Category":  {'MAM':1, 'M45':2, 'M40':3, 'M50':4, 'M55':5,'WAM':6}}
data.replace(valores_categoria, inplace=True)
print(data)
print('______________________________________________________')
#pintar tiempo de maraton vs los km del corredor en las ultimas 4 semanas previas
plt.scatter(x = data['km4week'], y=data['MarathonTime'])
plt.title('km4week Vs Marathon Time')
plt.xlabel('km4week')
plt.ylabel('Marathon Time')
plt.show()

#velocidad a lo que se corrio con el tiempo de maraton
data = data[data['sp4week'] < 1000]
plt.scatter(x=data['sp4week'], y=data['MarathonTime'])
plt.title('sp4week Vs Marathon Time')
plt.xlabel('sp4week')
plt.ylabel('Marathon Time')
plt.show()
print('______________________________________________________')

#Entrenamiento del modelo
#se separa en 80 y 20

datos_train = data.sample(frac=0.8,random_state=0)
datos_test = data.drop(data.index)

#valor a predecir
entrenamiento = data.pop('MarathonTime')
etiquetas_test = datos_test.pop('MarathonTime')

#Entrenamiento con regresión lineal

modelo = LinearRegression()
modelo.fit(entrenamiento,etiquetas_test)

predicciones = modelo.predict(datos_test)
print(predicciones)

print('______________________________________________________')
#comparación con el valor real

error = np.sqrt(mean_squared_error(etiquetas_test, predicciones))
print("Error porcentual : %f" % (error*100))