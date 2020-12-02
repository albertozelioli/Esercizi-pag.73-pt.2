numero = []
x = 1
potenza = 2
ncifre = int(input("Inserire il numero di cifre che compongono il numero binario: "))
print("Inserire le cifre del numero binario (0 o 1) da destra verso sinistra")
cifra = int(input("Inserire la prima cifra: "))
if cifra == 1:
    prodotto = cifra
    numero.append(prodotto)

while True:
    if x != ncifre:
        cifra = int(input("Inserire la cifra successiva: "))
        x = x + 1
        if cifra == 1:
            prodotto = cifra*potenza
            numero.append(prodotto)
            potenza = potenza*2
    else:
        break

print("Il numero decimale corrispondente al numero binario scritto è", sum(numero))
