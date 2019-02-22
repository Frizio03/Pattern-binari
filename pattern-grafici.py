from tkinter import *
from tkinter import messagebox

app = Tk()
app.geometry("800x600")

#creazione legenda
Leg = Label(app, text = "| 0 = White |")
Leg.place(x = 20, y = 400)
Leg2 = Label(app, text = "| 1 = Black  |")
Leg2.place(x = 20, y = 420)

#creazione bottoni
B = Button(app, text = "Precedente")
B.place(x = 0, y = 0)
C = Button(app, text = "Successivo")
C.place(x = 732, y = 0)

# creazione campi di ricerca
S = Label(app, text = "Numero slot")
S.place(x = 140, y = 0)
E1 = Entry(app, bd = 5)
E1.place(x = 220, y = 0)

N = Label(app, text = "Slot pieni")
N.place(x = 400, y = 0)
E2 = Entry(app, bd = 5)
E2.place(x = 470, y = 0)

#creazione variabili
slot = 3
npattern = 8
lspattern = []
pattern = []
lsnpieni = []
altezza = 35
larghezza = 0

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
for i in range(3, 7):

#trasformazione in binario e creazione pattern
	for k in range(npattern):
		pattern = []
		binario(k)
		pattern.reverse()
		controllo(pattern)
		npieni = pattern.count(1)
		lspattern.append(pattern)

#creazione dell'output tutto in formato stringa
		output = "P" + str(slot) + " -- " + str(npieni) + "C" + " -- " + "  |  " + str(lspattern[k])

		stampa = Label(app, text = output)
		stampa.place(x = larghezza, y = altezza)
#creazione label per stampare i pattern --> non utilizzati i label --> sono scomodi
	#	labelframe = LabelFrame(app, text = "")
	#	labelframe.place(x = 0, y = altezza)
	#	stampa = Label(labelframe, text = output)
	#	stampa.pack(side = side)
		altezza = altezza + 30

#modifica variabili per pattern successivi
	lspattern = []
	lsnpieni = []
	int(slot) 
	int(npieni)
	slot = slot + 1
	npattern = npattern*2
	larghezza = larghezza + 150
	altezza = 35


#impostazione finestra in loop
app.mainloop()







# creazione barra di scorrimento per stampa pattern --> tentativo non riuscito
#	scrollbar = Scrollbar(app)
#	scrollbar.pack( side = RIGHT, fill = Y )

#	mylist = Listbox(app, yscrollcommand = scrollbar.set )
#	for s in range(npattern):
#		npieni = lspattern[s].count(1)
#		output = "P" + str(slot) + " -- " + str(npieni) + "C" + " -- " + "  |  " + str(lspattern[s])
#		mylist.insert(END, output)

#	mylist.pack( side = LEFT, fill = BOTH )
#	scrollbar.config( command = mylist.yview )

#chr()    ord()  --> per convertire da ASCII a carattere e viceversa
