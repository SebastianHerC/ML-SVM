import csv

# Abre el archivo CSV de entrada con delimitación de coma y codificación UTF-8
with open('Eliminatorias conmebol\Selecciones\Colombia\overall_Col.csv', mode='r', newline='', encoding='utf-8') as file:
    # Utiliza el delimitador de coma para leer el archivo
    reader = csv.reader(file, delimiter=',')
    
    # Lee las filas del archivo CSV
    rows = [row for row in reader]

# Abre un nuevo archivo CSV para escritura con delimitación de coma y codificación UTF-8
with open('overall_col.csv', mode='w', newline='', encoding='utf-8') as new_file:
    # Utiliza el delimitador de coma para escribir el archivo
    writer = csv.writer(new_file, delimiter=',')
    
    # Escribe las columnas en el nuevo archivo CSV
    writer.writerow(['Name', 'Age', 'Overall rating', 'Potential', 'Team & Contract', 'Value', 'Wage', 'Total'])
    
    # Escribe los datos reorganizados en el nuevo archivo CSV
    for row in rows[1:]:  # Ignora la primera fila con los encabezados originales
        writer.writerow(row)

print("Datos reorganizados y guardados en 'nuevo_archivo.csv'")