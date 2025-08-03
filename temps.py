import os
from pathlib import Path
from datetime import datetime, date, time
import csv
from csv import writer

current_datetime = datetime.now()
print(f"Current Date and Time: {current_datetime}")

data_folder = "temps_folder"
archivo = "temps.csv"

folder_path = Path(data_folder)
file_path = folder_path / archivo

# Crear la carpeta si no existe.
folder_path.mkdir(exist_ok=True)

header = ["FECHA", "TEMP_MIN", "TEMP_MAX"]

# Pida al usuario que ingrese la temperatura minima y maxima del dia (numeros decimales)
inp_fecha = input("Por favor introduzca la fecha del dia que quiere reportar las temperaturas: ")

# Valide que la entrada sea numerica, y en caso contrario muestre un error simple y termine
while True:
    try:
        inp_temp_min = int(input("Introduzca la temperatura minima que se registro el dia seleccionado: "))
        break
    except ValueError:
        print("Por favor solo utilice numeros para la temperatura minima.")

while True:
    try:
        inp_temp_max = int(input("Introduzca la temperatura maxima que se registro el dia seleccionado: "))
        break
    except ValueError:
        print("Por favor solo utilice numeros para la temperatura maxima.")

data = [inp_fecha, inp_temp_min, inp_temp_max]

# Crea un script que:
# Verifique si existe el archivo data/temps.csv
file_exists = file_path.exists()

# Si NO existe, crea el archivo con encabezados "fecha", "temperatura_min", "temp_max"
# Anada una fila con la fecha actual y las temperaturas ingresadas al archivo temps.csv
with open(file_path, 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    if not file_exists:
        csv_writer.writerow(header)
    csv_writer.writerow(data)

print(f"Archivo CSV '{file_path}' se creo correctamente con los datos ingresados")

