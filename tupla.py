def imprimirTupla(tuplas):
    for valor in tuplas:
        print(valor)

def instruccion(action):
    i=0
    for num in action:
        i=i+1
        print(f"{i} - {num}")

colores_primarios = ["rojo", "amarillo", "azul"]
acciones=["Puerta cerrada","Ingresar contraseña","Puerta abierta"]
muebles=["Escritorio","Mesa", "Heladera", "Cama", "Cocina"]

# print(acciones)

#i=0
#for x in colores_primarios:
#    i=i+1
#    print(f"{i} - {x}")

print(acciones[1])

#imprimirTupla(colores_primarios)
#imprimirTupla(acciones)
#instruccion(acciones)