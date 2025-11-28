
### ESCRITURA

gerencias=["Comercial","Markenting","Finanzas"]

    #creando nombre de funcion, despues en el argumento, el primero para archivo y
    # el siguiente la lista de valores que se va almacenar
def guardarLista(nombre_archivo, lista):
    f = open(nombre_archivo, "w")
    for elementos in lista:
        f.write(elementos+"\n")
    f.close()

#guardarLista("otras_acciones.txt", gerencias) # Primero es archivo y segundo lista

### LECTURA

f = open("acciones.txt", "r")
contenido = f.read()
print(contenido)

#Definir las funciones necesarias para:
    #Crear una tupla de 10 numeros
    #Almacenar la tupla en un archivo llamado numeros.txt

numeros = [1,2,3,4,5,6,7,8,9,10]
def numTupla(nombre_archivo,tupla):
    f = open(nombre_archivo,"w")
    for num in tupla:
        f.write(f"{num} \n")
    f.close()

numTupla("numeros.txt",numeros)
    