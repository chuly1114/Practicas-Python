

def edad(n, a):
    cont = 0
    for i in range(len(a)):
        if a[i] == n:
            cont = cont + 1
    return cont


def nombre(nom, a):
    for i in range(len(a)):
        if a[i] == nom:
            return True
    return False


def ocurrencia(nom, a):
    i = 0
    b = 0
    while b == 0:
        if a[i] != nom:
            i = i + 1
        else:
            b = 1
    return i


def promedio(a):
    cont = 0
    for i in range(len(a)):
        cont = a[i] + cont
    div = len(a)
    res = cont / div
    return res


def prom_esta(a):
    cont = 0
    for i in range(len(a)):
        cont = a[i] + cont
    div = len(a)
    res = cont / div
    return res


def mayor_edad(arreglo):
    lec = len(arreglo)
    may = arreglo[0]
    for i in range(0, lec):
        if arreglo[i] > may:
            may = arreglo[i]
    return may


def menor_edad(arreglo):
    lec = len(arreglo)
    men = arreglo[0]
    for i in range(0, lec):
        if arreglo[i] < men:
            men = arreglo[i]
    return men


def mayor_estatura(arreglo):
    lec = len(arreglo)
    may = arreglo[0]
    for i in range(0, lec):
        if arreglo[i] > may:
            may = arreglo[i]
    return may


def menor_estatura(arreglo):
    lec = len(arreglo)
    men = arreglo[0]
    for i in range(0, lec):
        if arreglo[i] < men:
            men = arreglo[i]
    return men


def repit(a):
    cont = 0
    lec = len(a)
    for i in range(lec):
        cont1 = 0
        b = a[i]
        for n in range(lec):
            if a[n] == b:
                cont1 = cont1 + 1
        if cont1 > cont:
            cont = cont1
            c = a[i]
    return c

# def eliminar_deportista(nombre:str,deportistas:list[str],):
#     for i in range(len(deportistas)):
#         if deportistas[i] == nombre:
#             return

def ordenar(numero,deportistas,edades,estatura):
    if numero == 13:
        for i in range(len(deportistas)):
