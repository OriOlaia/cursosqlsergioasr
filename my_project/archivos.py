### FUNCION
def almacenar(escritura):
    for info in escritura:
        f.write(info+"\n")

### ESCRITURA
f = open("acciones.txt","w") #La letra "w" significa que va a ser de escritura
gerencias=["Comercial","Markenting","Finanzas"]

#f.write(gerencias[0])

#for gerencia in gerencias:
#    f.write(gerencia+"\n")

almacenar(gerencias)

#i=0
#for gerencia in gerencias:
#    i=i+1
#    f.write(f"{i} - {gerencia}")

### LECTURA
#f = open("acciones.txt","r") #La letra "r" solo lectura