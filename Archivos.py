import os
import struct
file_name = "El Mercado"
if os.path.exists(file_name):
    fp = open(file_name, "r+b")
else:
    fp = open(file_name, "w+b")

formato = "ldl"
codigo= 34
precio = 45.5
stock = 12
contenido = struct.pack(formato, codigo, precio, stock) #transformar datos enteros en una secuencia de bytes



#Ejercicio
# 1. Crear un archivo binario si este no existe, sino lo abrimos
# 2. Transformar 3 datos enteros en una secuencia de bytes o flujo de bytes
# 3. Guardar la secuencia de bytes en un archivo binario

#1
file_1 = "Archivo Binario"
if os.path.exists(file_name):
    fpi = open(file_name, "r+b")
else:
    fpi = open(file_name, "w+b")

#2
formato2 = "lll"
entero1 = 3
entero2 = 6
entero3 = 734

contenido = struct.pack(formato2, entero1, entero2, entero3)

fpi.write(contenido)

#n: cantidad de bytes q' va a leer
n = struct.calcsize(formato2) #Return the size of the struct (and hence of the bytes object produced by pack(format, ...))

contenido = fp.read(n)

var = struct.unpack(formato2, contenido)

print(var)

fpi.close()
