import translator as tr

t = tr.Translator()

while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("Scegli un'opzione: ")

    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci una nuova parola: ")
        txt = input()
        t.handleAdd(txt)
        print("hai aggiunto la parola: " + txt)

    if int(txtIn) == 2:
        txt = input("inserisci parola da tradurre: ")
        traduzione = t.handleTranslate(txt)
        print(traduzione)


    if int(txtIn) == 3:
        txt = input("inserisci parola da tradurre: ")
        traduzione = t.handleWildCard(txt)
        print(traduzione)

    if int(txtIn) == 4:
        t.dict.stampa()

    if int(txtIn) == 5:
        break