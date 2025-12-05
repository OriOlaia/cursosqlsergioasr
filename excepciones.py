

def elegir_numero():
    x = int(input("Ingresar un numero: "))
    if x==17:
        raise 'Error al elegir un numero'
    return x


try:
    elegir_numero()
except:
    print("Ocurrió un error al seleccionar un numero")



def existe(nombre_archivo):
    try:
        f=open(nombre_archivo, "r")
        return 1
    except:
        return 0

print("Intento de apertura de archivo")
r=existe("acciones.txt")
print(r)



#print("Intento de apertura de archivo")
#try:
#    f = open("inexistente.txt","r")
#except:
#    print("No existe el archivo")