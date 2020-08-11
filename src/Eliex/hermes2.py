# -*- coding: utf-8 -*-


PiF = "" # PiF Global

# Satchel is a self-contained, duct-taped input-manager and attribute storage object
class Satchel:
    def __init__(self):
        self.PiF,self.Title,self.Year,self.Authors,self.Platforms,self.KWs,self.Teams = "","","",[],[],[],[] # Teams added
    def Create(self):
        """
        x = input("Enter Fire-and-Forget String or hit ENTER to continue: ")
        if x != "":
            amng = attributes.AttributeManager()
            amng.readIn(x)
            self.PiF = amng['DEFAULT']['PiF']
            self.PiF = amng['DEFAULT']['Title']
            self.PiF = amng['DEFAULT']['Year']
            self.PiF = amng['DEFAULT']['Authors']
            self.PiF = amng['DEFAULT']['Platforms']
            self.PiF = amng['DEFAULT']['KWs']
        """
        pos = 0
        FuncOrder = [inputPiF,inputTitle,inputYear,inputAuthors,inputPlatforms,inputKWs,inputTeams]
        while True:
            var, cancel, back = FuncOrder[pos]()
            if cancel:
                return self,True
            if back:
                if pos == 0:
                    print("\nAlready at start! type \"cancel\" to exit or continue from current position")
                else:
                    pos = pos-1
            else:
                if pos == 0:
                    self.PiF = var
                elif pos == 1:
                    self.Title = var
                elif pos == 2:
                    self.Year = var
                elif pos == 3:
                    self.Authors = var
                elif pos == 4:
                    self.Platforms = var
                elif pos == 5:
                    self.KWs = var
                elif pos == 6:  # teams added
                    self.Teams = var
            if back:
                pass
            else:  
                pos += 1
            if pos>6: # teams added, from 5 to 6
                break
        # auto, gets last names from authors and gets callsign
        self.AuthorLastNames = self.getLastNames(self.Authors)
        self.Callsign = self.ProduceCallSign()
        return self,False
        
        """
        
        
        self.PiF,cont = inputPiF()
        if cont == False:
            return False
        
        # input title, back returns to pif
        self.Title, cont, back = inputTitle()
        if cont == False:
            return False
        if back == False:
            self.PiF,cont = inputPiF()
            self.Title, cont, back = inputTitle()
            
        # input authors, back returns to title
        self.Authors, cont, back = inputAuthors()
        if cont == False:
            return False
        if back == False:
            self.Title, cont, back = inputTitle()
            self.Authors, cont, back = inputAuthors()
        # input platforms, back returns to authors
        self.Platforms, cont, back = inputPlatforms()
        if cont == False:
            return False
        if back == False:
            self.Authors, cont, back = inputAuthors()
            self.Platforms, cont, back = inputPlatforms()
        # input year, back returns to platforms
        self.Year, cont, back = inputYear()
        if cont == False:
            return False
        if back == False:
            self.Platforms, cont, back = inputPlatforms()
            self.Year, cont, back = inputYear()
        # input kws, back returns to year
        self.KWs, cont, back = inputKWs()
        if cont == False:
            return False
        if back == False:
            self.Title, cont, back = inputTitle()
            self.Authors, cont, back = inputAuthors()
        """
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
        INI+= "ProjectInFocus = " + backlinkBracket("_PiF_ " + self.PiF) + "\n"
        INI+= "YearPublished = " + backlinkBracket("_Y_ " + self.Year) +"\n"
        if len(self.Authors) > 0: 
            INI+= "Authors = "
            for author in self.Authors:
                INI+= backlinkBracket("_O_ " + author) + ","
            INI+= "\n"
        if len(self.Platforms) > 0:
            INI+= "Platforms = "
            for platform in self.Platforms:
                INI+= backlinkBracket("_X_ " + platform) + ","
            INI+= "\n"
        if len(self.KWs) > 0: 
            INI+= "KeyWords = "
            for KW in self.KWs:
                INI+= backlinkBracket("_KW_ " + KW) + ","
            INI+= "\n"
        if len(self.Teams) > 0:  # teams added
            INI+= "Teams = "
            for team in self.Teams:
                INI+= backlinkBracket("_T_ " + team) + ","
            INI+= "\n"
        return INI
                 
    
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

def checkForSpecialCase(userinput):
    if userinput == "cancel" or userinput == "Cancel":
        return "",True, False
    if userinput == "back" or userinput == "Back":
        return "",False, True
    return userinput,False, False

# inputAttributePrompt handles the looping insertion of key attributes
def inputPiF():
    global PiF
    userinput = input("\nInput Project in Focus (PiF) callsign, hit ENTER to use last PiF used: ")
    userinput, cancel, back = checkForSpecialCase(userinput)
    if cancel or back:
        return "",cancel, back
    if userinput == "":
        if PiF == "":
            PiF = "MISC"
    else:
        PiF = userinput
    return PiF, False, False

def inputTitle():
    userinput = input("\nPlease input title: ")
    userinput, cancel, back = checkForSpecialCase(userinput)
    if cancel or back:
        return "", cancel, back
    return userinput, False, False

def inputYear():
    userinput = input("\nPlease input the year published: ")
    userinput, cancel, back = checkForSpecialCase(userinput)
    if cancel or back:
        return "", cancel, back
    return userinput, False, False

def inputAuthors():
    print("\nPlease input one Author Callsign at a time using ENTER to submit, in format XY_LastName, hit ENTER with blank input to continue")
    Authors = []
    while True:
        userinput = input("\nInput Author Callsign or hit ENTER to complete: ")
        userinput, cancel, back = checkForSpecialCase(userinput)
        if cancel or back:
            return [], cancel, back
        if userinput == "":
            return Authors, False, False
        else:
            Authors.append(userinput)

def inputPlatforms():
    print("\nPlease input one Platform Callsign at a time using ENTER to submit, hit ENTER with blank input to continue")
    print("\nIMPORTANT: Remember to use a correct prefix for the most appropriate Institution type, PUB_ for Publishing House | GOV_ for Government Org | JRN_ for journal | WEB_ for website | TNK_ for Think Tank | CMP_ for Company")
    Platforms = []
    while True:
        userinput = input("\nInput Platform Callsign or hit ENTER to complete: ")
        userinput, cancel, back = checkForSpecialCase(userinput)
        if cancel or back:
            return [], cancel, back
        if userinput == "":
            return Platforms, False, False
        else:
            Platforms.append(userinput)
    
def inputKWs():
    print("\nIf there are any other Keywords you'd like to add, add here, hit ENTER with blank input to continue")
    KWs = []
    while True:
        userinput = input("\nInput KeyWord Callsign or hit ENTER to complete: ")
        userinput, cancel, back = checkForSpecialCase(userinput)
        if cancel or back:
            return [], cancel, back
        if userinput == "":
            return KWs, False, False
        else:
            KWs.append(userinput) 
            
def inputTeams(): # Teams added
    print("\nPlease add the teams which apply, (case sensitive): Blue, Red, Green")
    Teams = []
    while True:
        userinput = input("\nInput Team or hit ENTER to complete: ")
        userinput, cancel, back = checkForSpecialCase(userinput)
        if cancel or back:
            return [], cancel, back
        if userinput == "":
            return Teams, False, False
        else:
            Teams.append(userinput) 


#test, success = Satchel().Create()
#x = test.ProduceINIstring()