import re

# Ruta completa al archivo original
archivo_original = r'resultados\data_resultados.csv'

# Ruta completa al archivo donde se guardarán los datos formateados
archivo_formateado = r'C:\Users\seba-\Desktop\Python\OTROS\Machine learning\Eliminatorias conmebol\resultados\resultados.csv'

# Abre el archivo CSV original
with open(archivo_original, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Define una función para formatear los registros
def format_record(line):
    # Utiliza una expresión regular para extraer la información necesaria
    match = re.match(r'"([\d\w\s:,]+),([\d\w\s:,]+),([\d\w\s:,]+),([\d\w\s:,]+),""(.+)""', line)
    if match:
        date, team1, score, team2, location = match.groups()
        return f'"{date.strip()},{team1.strip()},{score.strip()},{team2.strip()},"{location.strip()}"\n'
    return line

# Formatea todos los registros
formatted_lines = [format_record(line) for line in lines]

# Abre un nuevo archivo CSV para escribir los registros formateados
with open(archivo_formateado, 'w', encoding='utf-8') as new_file:
    new_file.writelines(formatted_lines)

print(f"Datos formateados y guardados en '{archivo_formateado}'")
