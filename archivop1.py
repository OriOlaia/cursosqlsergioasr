### MI VERSION (corregir)
def numeros_azar():
    x = int(input("Ingresa un numero: "))
    if x > 0 and x < 10:
        raise 'Error 456'
    else:
        if x > 11 and x < 20:
            raise 'Error 457'
        else:
            if x > 21 and x < 30:
                raise 'Error 458'
    return x

continuar = "c"
terminar = "q"

while continuar == "c":
    try:
        if numeros_azar():
            continuar = input("Desea continuar?")
        else:
            terminar = input("Terminar el programa")  
    except:
        print("Ocurrió un error")

### VERSION ELIAS
