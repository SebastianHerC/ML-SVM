import csv
import pandas as pd

# Datos originales
ruta = 'resultados/tu_archivo_formateado.csv'
data = pd.read_csv(ruta, header=None, names=["Datos"])

# Crear un nuevo DataFrame con columnas separadas
nuevo_data = pd.DataFrame(columns=["fecha", "local", "resultado", "visita", "ciudad"])

for index, row in data.iterrows():
    partes = row["Datos"].split(',')
    fecha = partes[0].strip()
    local = partes[1].strip()
    resultado = partes[2].strip()
    visita = partes[3].strip()
    ciudad = partes[4].strip('"').strip()
    
    # Agregar una nueva fila al nuevo DataFrame
    nuevo_data = pd.concat([nuevo_data, pd.DataFrame({"fecha": [fecha], "local": [local], "resultado": [resultado], "visita": [visita], "ciudad": [ciudad]})])

# Resetear los índices del nuevo DataFrame
nuevo_data.reset_index(drop=True, inplace=True)

# Guardar los datos separados en un nuevo archivo CSV
nuevo_data.to_csv('datos_separados.csv', index=False)

print("Los datos han sido separados en 5 columnas y guardados en 'datos_separados.csv'")


