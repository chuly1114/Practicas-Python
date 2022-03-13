def fun_menor(a):
    """Encuentra menor valor en arreglo a
    (list)-> int
    """
    menor = a[0]
    for i in range(1, len(a)):
        if menor > a[i]:
            menor = a[i]
    return menor


#
def fun_mayor(a):
    """Encuentra mayor valor en arreglo a
    (list)-> int
    """
    mayor = a[0]
    for i in range(1, len(a)):
        if mayor < a[i]:
            mayor = a[i]
    return mayor


def main():
    n = int(input(""))
    for i in range(n):
        m = input("")
        m = m.split(",")
        for i in range(len(m)):
            m[i] = int(m[i])
        menor = fun_menor(m)
        mayor = fun_mayor(m)
        print(str(menor) + "," + str(mayor))


main()
