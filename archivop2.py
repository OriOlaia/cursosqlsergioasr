#1) Guardar informacion en un archivo csv
#Lista de alumno (cada alumno es un diccionario)
alumnos =[
    {"legajo": "1001", "nombre" : "Ana", "apellido": "Gomez","edad":21,"promedio": 8.7},
    {"legajo": "1002", "nombre" : "Luis", "apellido": "Perez","edad":19,"promedio": 7.2},
    {"legajo": "1003", "nombre" : "Maria", "apellido": "López","edad":22,"promedio": 9.5},
    {"legajo": "1004", "nombre" : "Juan", "apellido": "Martinez","edad":20,"promedio": 6.8},
]

with open("alumnos.csv", "w", encoding="utf-8") as archivo:
    for alumno in alumnos:
        linea = f"{alumno['legajo']}; {alumno['nombre']}; {alumno['apellido']}; {alumno['edad']}; {alumno['promedio']}\n"
        archivo.write(linea)


#Leer
lista_alumnos = []
with open("alumnos.csv", "r", encoding="utf-8") as archivo:
    for linea in archivo: #Leer cada linea del archivo
        linea = linea.strip() #quita la parte final que seria "\n" | Quitar el salto de linea \n segun Sergio
        campos = linea.split(";") #separa, indicando segun el argumento como el ";", en ese espacio se va a separar | Genera una lista con cada elemento separado por ; segun Sergio
        #Convertimos a tipos correctos
        legajo = campos[0]
        nombre = campos[1]
        apellido = campos[2]
        edad = int(campos[3])
        promedio = float(campos[4])
        alumno_tupla = (legajo, nombre, apellido, edad, promedio)
        alumno_dict = {
            "legajo": legajo,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "promedio": promedio
        }
        lista_alumnos.append(alumno_dict)
    print("Imprimiendo lista...")
    print(lista_alumnos)