print("Inserire il numero decimale che si vuole convertire in binario: ")
ndec = int(input())
nbin = []
risultato = ndec

while risultato != 0:
    resto = risultato % 2
    risultato = risultato // 2
    nbin.append(resto)
print("Il numero decimale",ndec,"convertito in binario è:")

for cifra in reversed(nbin):
    print(cifra)
