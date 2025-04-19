import re
class Dictionary:
    def __init__(self, dict={}):
        self.dict = dict

    def loadDictionary(self):
        file = open("dictionary.txt", "r").readlines()
        for line in file:
            riga = line.strip().split()
            if len(riga) == 2:
                self.dict[riga[0]] = riga[1]

        # dict is a string with the filename of the dictionary

    def addWord(self, txtIn):
         if len(txtIn) == 2:
            if txtIn[0] not in self.dict:
                self.dict[txtIn[0]] = txtIn[1]
                file = open("dictionary.txt", "a")
                file.write("\n"+txtIn[0] + " " + self.dict[txtIn[0]])
            else:
                print(txtIn[0] + self.dict[txtIn[0]])

    def translate(self, daCercare):
       return self.dict[daCercare]
        #for k,v in self.dict.items():
            #if daCercare == k:
                #return v


    def stampa(self):
        for k,v in self.dict.items():
            parolaAliena = k
            traduzione = v
            print(parolaAliena + " " + traduzione)


    def translateWordWildCard(self, wildCard):
        # Replace "?" with "." to use regex
        wildCard = wildCard.replace("?", ".")
        print(wildCard)
        matchCounter = 0
        sb = []

        for w in self.dict.keys():
            # Use regex matching for "alienWord" with the modified wild card
            if re.search(wildCard, w):
                matchCounter += 1
                sb.append(self.dict.get(w))

        # Return concatenated translations if there are matches
        if matchCounter != 0:
            return sb
        else:
            return None