import csv


with open('Eliminatorias conmebol/Selecciones/Uruguay/overall_Uru.csv', mode='r', newline='', encoding='utf-8') as file:

    reader = csv.reader(file, delimiter=',')
    

    rows = [row for row in reader]


with open('overall_uru.csv', mode='w', newline='', encoding='utf-8') as new_file:

    writer = csv.writer(new_file, delimiter=',')
    

    writer.writerow(['Name', 'Age', 'Overall rating', 'Potential', 'Team & Contract', 'Value', 'Wage', 'Total'])
    

    for row in rows[1:]:
        writer.writerow(row)

print("Datos reorganizados y guardados en 'nuevo_archivo.csv'")