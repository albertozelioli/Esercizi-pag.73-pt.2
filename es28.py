listanomi = []
listalanci = []
studenti = 0
lanci = 0
x = 1

while x == 1:
    studenti += 1
    lanci += 1
    print("Inserire il nome dello studente", studenti,": ")
    studente = input()
    print("Inserire il lancio in metri dello studente:", lanci, ": ")
    lancio = int(input())
    listanomi.append(studente)
    listalanci.append(lancio)
    scelta = input("Per terminare l'elenco scrivere STOP, altrimenti scrivere un altra lettera o parola qualsiasi: ")
    if scelta == "STOP":
        break
lanciomag = max(listalanci)
print ("Il lacio dello studente vincitore è di", lanciomag, "metri")

