listacittà = []
listamax = []
listamin = []
listaesc = []
città = 0
tempmax = 0
tempmin = 0
tempesc = 0
x = 1
print("Inserire il valore dell'escursione termica da prefissare: ")
valorepref = int(input())

while x == 1:
    città += 1
    tempmax += 1
    tempmin += 1
    tempesc += 0
    print("Inserire il nome della città", città,": ")
    nome = input()
    listacittà.append(nome)
    print("Inserire la temperatura massima registrata oggi a", nome,": ")
    temp1 = int(input())
    listamax.append(temp1)
    print("Inserire la temperatura minima registrata oggi a", nome,": ")
    temp2 = int(input())
    listamin.append(temp2)
    esctermica = temp1 - temp2
    if esctermica > valorepref:
        listaesc.append(esctermica)
    else:
        pass
    scelta = input("Per terminare l'elenco scrivere STOP, altrimenti scrivere un altra lettera o parola qualsiasi: ")
    if scelta == "STOP":
        break
    
numerocittà = len(listaesc)
listaesc.reverse()
print("Il numero delle città che hanno superato il valore prefissato sono", numerocittà, "e i rispettivi valori in ordine decrescente sono i seguenti:", listaesc)
