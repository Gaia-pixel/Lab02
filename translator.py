from dictionary import Dictionary


class Translator:

    def __init__(self, dict=Dictionary()):
        self.dict = dict

    def printMenu(self):
        print("1. Aggiungi nuova parola \n2. Cerca una traduzione \n3. Cerca con wildcard \n4. Stampa dizionario \n5. Exit")
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit


    def loadDictionary(self, dict):
       self.dict.loadDictionary()
       # dict is a string with the filename of the dictionary

    def handleAdd(self, entry):
        input = entry.split(" ")
        self.dict.addWord(input)
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

    def handleTranslate(self, query):
       return self.dict.translate(query)
        # query is a string <parola_aliena>


    def handleWildCard(self,query):
        return self.dict.translateWordWildCard(query)
        # query is a string with a ? --> <par?la_aliena>
