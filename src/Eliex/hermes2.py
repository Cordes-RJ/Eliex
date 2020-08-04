# -*- coding: utf-8 -*-

PiF = "" # PiF Global

class Satchel:
    def __init__(self):
        self.PiF = inputPiF()
        self.Title = inputTitle()
        self.Authors = inputAuthors()
        self.AuthorLastNames = self.getLastNames(self.Authors)
        self.Platforms = inputPlatforms()
        self.Year = inputYear()
        self.Callsign = self.ProduceCallSign()
        self.KWs = inputKWs()
    def getLastNames(self,Author):
        if len(self.Authors) == 0:
            return []
        new = []
        for author in self.Authors:
            new.append(separateAuthorFromInitials(author))
        return new
    def ProduceCallSign(self):
        if len(self.AuthorLastNames) == 0 and len(self.Platforms) == 0:
            callsign = "Unknown"
        elif len(self.AuthorLastNames) == 0:
            callsign = self.Platforms[0]
        elif len(self.AuthorLastNames) > 3:
            callsign = self.AuthorLastNames[0] + "EtAl"
        else:
            callsign = ""
            for author in self.AuthorLastNames:
                callsign += author
        if self.Year == "":
            return callsign+"ND"
        else:
            return callsign+self.Year
    def ProduceINIstring(self):
        INI = ""
        INI+= "Title = " + "\"" + self.Title + "\"" + "\n"
        INI+= "ProjectInFocus = " + backlinkBracket("_PiF_" + self.PiF) + "\n"
        INI+= "YearPublished = " + backlinkBracket("_YEAR_" + self.Year) +"\n"
        if len(self.Authors) > 0: 
            INI+= "Authors = "
            for author in self.Authors:
                INI+= backlinkBracket("_O_" + author) + ","
            INI+= "\n"
        if len(self.Platforms) > 0:
            INI+= "Platforms = "
            for platform in self.Platforms:
                INI+= backlinkBracket("_X_" + platform) + ","
            INI+= "\n"
        if len(self.KWs) > 0: 
            INI+= "KeyWords = "
            for KW in self.KWs:
                INI+= backlinkBracket("_KW_" + KW) + ","
            INI+= "\n"
        return INI
            
def inputKWs():
    print("\nIf there are any other Keywords you'd like to add, add here, hit ENTER with blank input to continue")
    KWs = []
    while True:
        userinput = input("\nInput KeyWord/KeyWord Callsign or hit ENTER to complete: ")
        if userinput == "":
            return KWs
        else:
            KWs.append(userinput)      
    
def backlinkBracket(string):
    return "[[" + string + "]]"

# separateAuthorFromInitials is a utility function which separates the last name of an author from initials
def separateAuthorFromInitials(author):
    delimit = 0
    for i in range(len(author)):
        if author[i] == "_":
            delimit = i + 1
            break
    return author[delimit:len(author)]

def inputTitle():
    return input("\nPlease input title: ")
    
# inputAttributePrompt handles the looping insertion of key attributes
def inputPiF():
    global PiF
    userinput = input("\nInput Project in Focus (PiF) callsign, hit ENTER to use last PiF used: ")
    if userinput == "":
        if PiF == "":
            PiF = "MISC"
    else:
        PiF = userinput
    return PiF

def inputAuthors():
    print("\nPlease input one Author Callsign at a time using ENTER to submit, in format XY_LastName, hit ENTER with blank input to continue")
    Authors = []
    while True:
        userinput = input("\nInput Author Callsign or hit ENTER to complete: ")
        if userinput == "":
            return Authors
        else:
            Authors.append(userinput)

def inputPlatforms():
    print("\nPlease input one Platform Callsign at a time using ENTER to submit, hit ENTER with blank input to continue")
    print("\n*Remember to use a correct prefix for the most appropriate Institution type, PUB_ for Publishing House | GOV_ for Government Org | JRN_ for journal | WEB_ for website | TNK_ for Think Tank | CMP_ for Company")
    Platforms = []
    while True:
        userinput = input("\nInput Platform Callsign or hit ENTER to complete: ")
        if userinput == "":
            return Platforms
        else:
            Platforms.append(userinput)

def inputYear():
    return input("\nPlease input the year published: ")

#%%
test = [Satchel()]
x = test[0].ProduceINIstring()