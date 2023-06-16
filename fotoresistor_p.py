import serial
import time
import csv
from datetime import datetime

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1) 

def read():
    data = arduino.readline() 
    return data

print("Estamos trabajando para usted")

time.sleep(4) ## Los 4 primeros valores son blancos


while True:
    value = read()
    value = int(value)
    # Definir el nombre del archivo
    archivo = "archivo_.txt"
    max_filas = 10

    # Generar los datos aleatorios
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    hora_actual = datetime.now().strftime("%H:%M")
    estado = "'Prendido'" if value > 700 else "'Apagado'"

    # Agregar los datos a la tabla
    nueva_fila = [fecha_actual, hora_actual, value  , estado]

    # Abrir el archivo en modo de escritura y leer los datos existentes
    with open(archivo, "r") as file:
        reader = csv.reader(file, delimiter=";")
        filas = list(reader)

    # Insertar la nueva fila en la segunda posición (después de las columnas)
    filas.insert(1, nueva_fila)

    # Verificar el número de filas y eliminar las que superen el límite
    if len(filas) > max_filas:
        filas = filas[:max_filas]

    # Guardar los datos actualizados en el archivo
    with open(archivo, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        for fila in filas:
            writer.writerow(fila)
        
    print(value) # printing the value
    time.sleep(0.01)