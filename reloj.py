s= input("Ingrese la hora actual")
hora, minuto, segundo = s.split(':')
hora= int(hora)
minuto= int(minuto)
segundo=int(segundo)
for i in range (10):
    print (hora, minuto, segundo)
    if (segundo < 59):
        segundo += 1
    else:
        segundo=0
        if (minuto < 59):
            minuto += 1
        else:
            minuto=0
            if (hora < 23):
                hora += 1
            else:
                hora=0
