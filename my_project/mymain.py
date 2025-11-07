import my_package as fc ## al agregar as lo que hace es crear o abreviar el nombre, en este caso es fc para tener en referencia.

if __name__ == "__main__":
    a=input("Ingrese el valor de a: ")
    b=input("Ingrese otro valor de b: ")
    c=fc.add(float(a),float(b))
    d=fc.concact(a,b)

    print(f"El resultado de la suma a y b es: {c}")
    print(f"El resultado de cocatenar a y b es {d}")