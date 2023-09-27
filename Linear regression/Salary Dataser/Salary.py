import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

ruta ='Linear regression\Salary Dataser\Salary_dataset.csv'
data=pd.read_csv(ruta)
data = data.drop('Unnamed: 0', axis=1)
data['YearsExperience'] = data['YearsExperience'].astype(int)
data['Salary'] = data['Salary'].astype(int)



X = data[['YearsExperience']]  # Features (características)
y = data['Salary']  # Target (variable objetivo)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

mse = mean_squared_error(y_test, predicciones)
print("Error Cuadrático Medio (MSE):", mse)

print("Predicciones:")
print(predicciones)