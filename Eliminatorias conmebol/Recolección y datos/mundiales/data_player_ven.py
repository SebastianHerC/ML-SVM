import pandas as pd
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

urls = [
    'https://sofifa.com/players?type=all&na%5B%5D=61',
    'https://sofifa.com/players?type=all&na%5B0%5D=61&offset=60',
    'https://sofifa.com/players?type=all&na%5B0%5D=61&offset=120',
    'https://sofifa.com/players?type=all&na%5B0%5D=61&offset=180',
]


tablas = []

for url in urls:
    response = requests.get(url, headers=headers)
    tablas_temp = pd.read_html(response.text)
    tablas.extend(tablas_temp)

tabla_resultados = pd.concat(tablas)


tabla_resultados.to_csv('overall_Ven.csv', index=False)

print("Datos almacenados en overall_chile.csv")