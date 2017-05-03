#dato de entrada: Frase (String)
#dato de salida : Mensaje

def EsPalindroma(Cad):
    tam = len(Cad)
    Comparaciones = tam//2
    izq=0
    der=tam-1
    while((izq < Comparaciones)  and (Cad[izq]==Cad[der])):
        izq+=1
        der-=1
    if izq==Comparaciones:
        return(True)
    else:
        return(False)


def main():
    Frase = input("Frase : ")
    if (EsPalindroma(Frase)==True ):
        print("Es Palindroma")
    else:
        print("No es Palindroma")


# Llamada a la funcion Principal que tiene por nombre main()
if(__name__ == "__main__"):
    main()
