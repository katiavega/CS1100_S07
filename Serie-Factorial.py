#dato de entrada: n (int)
#dato de salida : Suma (int)

def Factorial(num):
    F = 1
    i=2
    while i<=num:
        F = F *i
        i+=1
    return(F)


def main():
    n = int(input("Numero : "))
    Suma =0
    i=1
    while i<=n:
        Suma +=Factorial(i)
        i+=2
    print("La suma de la serie es : ",Suma)


# Llamada a la funcion Principal que tiene por nombre main()
if(__name__ == "__main__"):
    main()
