import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

ruta ='Linear regression\Insurance Dataset\simplelinearregression.csv'
data=pd.read_csv(ruta)

X = data[['Age']]  # Features (características)
y = data['Premium']  # Target (variable objetivo)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

mse = mean_squared_error(y_test, predicciones)
print("Error Cuadrático Medio (MSE):", mse)

print("Predicciones:")
print(predicciones)
