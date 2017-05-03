lista=[]
for i in range(6):
    elemento=input("Ingrese el nombre del equipo")
    lista.append(elemento)
for i in range(6):
    for j in range(6):
        if i != j:
            print ("Local: ", lista[i]," Visita: ", lista[j])
