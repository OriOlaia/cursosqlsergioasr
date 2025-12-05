def imprimirLista(lista):
    for valor in lista:
        print(valor)



gerencias = list()

gerencias.append("Comercial")
gerencias.append("Marketing")
gerencias.append("Atención al cliente")
gerencias.append("Administración")
gerencias.append("Recursos humanos")
gerencias.append("TIC")

muebles = ["mouse", "monitor", "gabinete", "escritorio"]
# print(gerencias)
# print("La version final de la lista es la siguiente: ")
# i=0
# for gerencia in gerencias:
#     i=i+1
#     print(f"{i} - {gerencia}")

imprimirLista(gerencias)

print(muebles[1]) #monitor
muebles[1]="pizarra"
print (muebles[1]) #pizarra

del muebles[1] #elimina el valor que está en la posición 1
print(muebles)
print(muebles[1])