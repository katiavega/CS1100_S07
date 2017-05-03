#halla el area de un triangulo, solo si con 3 puntos se puede formar un triangulo
#dato de entrada :  x1,y1, x2,y2, x3,y3 (float)
#dato de salida  : Area (float)

import math

def DameLado(x1,y1,x2,y2):
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distancia


def EsTriangulo(x1,y1,x2,y2,x3,y3):
     L1 = DameLado(x1,y1,x2,y2)
     L2 = DameLado(x2,y2,x3,y3)
     L3 = DameLado(x3,y3,x1,y1)

     if (L1 + L2 > L3) and (L2 + L3 > L1)  and (L3 + L2 > L1):
         return(True)
     else:
         return(False)


def Area(x1,y1,x2,y2,x3,y3):
     L1 = DameLado(x1,y1,x2,y2)
     L2 = DameLado(x2,y2,x3,y3)
     L3 = DameLado(x3,y3,x1,y1)
     semip = (L1 +L2 + L3)/2
     area = math.sqrt(semip*(semip-L1) * (semip-L2) * (semip-L3))
     return area


# Funcion Principal
def  main():
    print("Coordenada del primer punto ")
    x1 = float(input("x1 : "))
    y1 = float(input("y1 : "))

    x2 = float(input("x2 : "))
    y2 = float(input("y2 : "))

    x3 = float(input("x3 : "))
    y3 = float(input("y3 : "))

    if EsTriangulo(x1,y1,x2,y2,x3,y3):
        print("El area es ", Area(x1,y1,x2,y2,x3,y3))
    else:
        print("No es triangulo ")
    print("Gracias por usar el programa!!!")


# Llamada a la funcion Principal que tiene por nombre main()
if(__name__ == "__main__"):
    main()
