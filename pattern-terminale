print("0 = white")
print("1 = black")
print()
slot = 3
npattern = 8
lspattern = []
pattern = []

#creazione comando per trasformare numeri decimali in binari
def binario(numero):
	Q = 1
	dividendo = numero
	while Q != 0:
		R = int(dividendo % 2)
		Q = int(dividendo / 2)
		dividendo = Q
		pattern.append(R)

#creazione comando per controllare che ci siano abbastanza slot
def controllo(lista):
	lunghezza = len(pattern)
	while lunghezza < slot:
			pattern.insert(0, 0)
			lunghezza = len(pattern)

#generazione di tutti i pattern possibili da 0 a 32
for i in range(3,33):

#trasformazione in binario e creazione pattern
	for k in range(npattern):
		pattern = []
		binario(k)
		pattern.reverse()
		controllo(pattern)
		lspattern.append(pattern)

#stampa della lista con le caratteristiche
	for s in range(npattern):
		npieni = lspattern[s].count(1)
		output = "P" + str(slot) + "--" + str(npieni) + "C" + "--" + "  |  " + str(lspattern[s])
		print(output)

#modifica variabili
	print()
	lspattern = []
	int(slot) 
	int(npieni)
	slot = slot + 1
	npattern = npattern*2
