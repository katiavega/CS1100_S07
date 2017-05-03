#Entradas Cirque du Soleil - Séptimo Día Perú
#Domingo 18 de junio de 2017 21:00h. Jockey Club, Lima, Perú

#Dato de entrada:  n (int), Ubicacion (string)
#Dato de salida :  Pases uno a continuacion de otro.

def GeneraPases(num, Lugar):
#num es el numero de l pase, y
#lugar: es el lugar
    print("$"*90)
    print("{:^90}".format("Cirque du Soleil - Séptimo Día Perú"))
    print("{:^90}".format("P A S E  -- P A S E -- P A S E "))
    print("Numero    :" + str(num))
    Lugar = "Ubicacion : " + Lugar
    print("{:90}".format(Lugar))
    print("{:90}".format("Domingo 18 de junio de 2017 21:00h. Jockey Club, Lima, Perú"))
    print("{:90}".format("Prohibida su venta..."))
    print("$"*90)
    print("")
    print("Corte aqui -8>----8>"*4)
    print("\n")


def main():
    n = int(input("Ingrese en numero de pases que desea generar : "))
    ubicacion = input("Ubicacion : ")
    print("\n\n")
    for x in range(n):
        GeneraPases(x+1,ubicacion)
    print("Gracias por usar el programa !")


# Llamada a la funcion Principal que tiene por nombre main()
if(__name__ == "__main__"):
    main()
