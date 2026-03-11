lista = []
for i in range(1, 10):
    lista.append(i)

for i in lista:
    if i == 1 or i == 3:
       lista[lista.index(i)] = str(i) + "ero"
    elif i == 2:
       lista[lista.index(i)] = str(i) + "do"
    elif i == 4 or i == 6 or i == 5:
       lista[lista.index(i)] = str(i) + "to"
    elif i == 7:
       lista[lista.index(i)] = str(i) + "mo"
    elif i == 8:
       lista[lista.index(i)] = str(i) + "vo"
    else:
       lista[lista.index(i)] = str(i) + "no"






