with open("programm.txt", "r") as f:
    lines = f.readlines()

variables = {} 

class Token():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"{self.name}: {self.value} "

class num():
    def __init__(self, value) -> None:
        self.value = value

    def eval(self):
        return float(self.value)
    
    def __repr__(self) -> str:
        return f"(NUM: {self.value})"
    
class string():
    def __init__(self, value) -> None:
        self.value = value

    def eval(self):
        return self.value
    
    def __repr__(self) -> str:
        return f"(STRING: {self.value})"

class setVariable():
    def __init__(self, tokens):
        self.name = tokens[0] # 0 = der name
        self.value = tokens[2] # 2 die value, 1 -> gleich 🪧zeichen

    def eval(self):
        variables[self.name.eval()] = self.value
    
    def __repr__(self) -> str:
        return f"(set variable: {self.name} ist {self.value})"

class name():
    def __init__(self, value) -> None:
        self.value = value


    def eval(self):
        if not "gleich" in line:
            # variable wird aufgerufen
            # a ist 3
            # fufu ist a >>>> a = variables[self.value].eval()
        
            return variables[self.value].eval()
        
        self.tokenNames = []
        self.tokenValues = []

        for token in tokens:
            self.tokenNames.append(token.name)
            self.tokenValues.append(token.value)
        
        # index von dem "ist"
        index = self.tokenNames.index("GLEICH")

        #index von der name class (variable)
        index2 = self.tokenValues.index(self.value)
        

        # checken ob es eine richtige variable ist
        # a = b <-
        # wenn ja ist der index größer
        if index2 > index:
            # fufu = dede
            # hier wird value von dede returnt
            return variables[self.value].eval()

        # wenn wir bei einem variable name sind
        # fufu = 3
        # wird fufu returnt
        return self.value

    
    def __repr__(self) -> str:
        return f"(NAME: {self.value})"
    
class plus():
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def eval(self):
        return self.value1.eval() + self.value2.eval()
    
    def __repr__(self) -> str:
        return f"(PLUS: {self.value1} + {self.value2})"   

class mal():
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def eval(self):
        return self.value1.eval() * self.value2.eval()
    
    def __repr__(self) -> str:
        return f"(MAL: {self.value1} * {self.value2})"   
        
class geteilt():
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def eval(self):
        return self.value1.eval() / self.value2.eval()
    
    def __repr__(self) -> str:
        return f"(GETEILT: {self.value1} / {self.value2})" 

class power():
    def __init__(self, value, power):
        self.value = value
        self.power = power

    def eval(self):
        return self.value.eval() ** self.power.eval()
    
    def __repr__(self) -> str:
        return f"(HOCH: {self.value} ^ {self.power})" 
      
class minus():
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def eval(self):
        return self.value1.eval() - self.value2.eval()
    
    def __repr__(self) -> str:
        return f"(MINUS: {self.value1} - {self.value2})"   

class Print():
    def __init__(self, values):     
        self.inhalt = values[2] # print("inhalt") # 0 = print, 1 = OP, 2 = Inhalt, 3 = CP
    
    def eval(self):
        print(self.inhalt.eval())
    
    def __repr__(self) -> str:
        return f"(PRINT: {self.inhalt})" 
    
class false():
    def __init__(self, uselessValue): # value ist eh false
        pass

    def eval():
        return False

    def __repr__(self) -> str:
        return f"(FALSE: falsch)" 

class true():
    def __init__(self, uselessValue) -> None:
        pass

    def eval():
        return True

    def __repr__(self) -> str:
        return f"(TRUE: wahr)" 
    
class VarGeteilt():
    def __init__(self, varName, value) -> None:
        self.varName = varName
        self.value = value
    def eval(self):
        newVar = variables[self.varName.eval()].eval() / self.value.eval()

        if type(newVar) == str:
            variables[self.varName.eval()] = string(newVar)
        else:
            variables[self.varName.eval()] = num(newVar)

        
    def __repr__(self) -> str:
        return f"(Var geteilt: {self.varName.eval()} -> /= {self.value.eval()})" 

class VarMal():
    def __init__(self, varName, value) -> None:
        self.varName = varName
        self.value = value
    def eval(self):
        newVar = variables[self.varName.eval()].eval() * self.value.eval()

        if type(newVar) == str:
            variables[self.varName.eval()] = string(newVar)
        else:
            variables[self.varName.eval()] = num(newVar)

        
    def __repr__(self) -> str:
        return f"(Var mal: {self.varName.eval()} -> *= {self.value.eval()})" 

class VarMinus():
    def __init__(self, varName, value) -> None:
        self.varName = varName
        self.value = value
    def eval(self):
        newVar = variables[self.varName.eval()].eval() - self.value.eval()

        if type(newVar) == str:
            variables[self.varName.eval()] = string(newVar)
        else:
            variables[self.varName.eval()] = num(newVar)

        
    def __repr__(self) -> str:
        return f"(Var minus: {self.varName.eval()} -> -= {self.value.eval()})" 

class VarAdd():
    def __init__(self, varName, value) -> None:
        self.varName = varName
        self.value = value
    def eval(self):
        newVar = variables[self.varName.eval()].eval() + self.value.eval()

        if type(newVar) == str:
            variables[self.varName.eval()] = string(newVar)
        else:
            variables[self.varName.eval()] = num(newVar)

        
    def __repr__(self) -> str:
        return f"(Var add: {self.varName.eval()} -> += {self.value.eval()})" 

class Parser():
    def __init__(self) -> None:
        self.rules1 = [[("NUM"), "expr", num], [("STRING"), "expr", string], [("NAME"), "expr", name], [("TRUE"), "expr", true], [("FALSE"), "expr", false]]
        self.rules05 = [[("expr","HOCH", "expr"), "expr", power]]
        self.rules2 = [[("expr", "MAL", "expr"), "expr", mal], [("expr", "GETEILT", "expr"), "expr", geteilt]]
        self.rules3 = [[("expr", "PLUS", "expr"), "expr",plus], [("expr", "MINUS", "expr"), "expr", minus]]
        self.rules35 = [[("expr", "PLUS", "GLEICH", "expr"), "statement", VarAdd], [("expr", "MINUS", "GLEICH", "expr"), "statement", VarMinus], [("expr", "MAL", "GLEICH", "expr"), "statement", VarMal], [("expr", "GETEILT", "GLEICH", "expr"), "statement", VarGeteilt]]
        self.rules4 = [[("PRINT", "DOPPELPUNKT", "expr"), "statement", Print], [("expr", "GLEICH", "expr"), "statement", setVariable]]

    def parse(self, tokens):
        self.tokens = tokens
        self.tokenNames = []
        self.tokenValues = []
        for token in tokens:
            self.tokenNames.append(token.name)
            self.tokenValues.append(token.value)
    
        for rule in self.rules1:
            i = 0
            for tokenName, tokenValue in zip(self.tokenNames, self.tokenValues):
                if tokenName == rule[0]:
                    self.tokenNames[i] = rule[1]
                    self.tokenValues[i] = rule[2](tokenValue) 
        
                i += 1
        while len(self.tokenNames) > 1:
            for rule in self.rules05:
                i = 0

                # geht durch alle tokens 
                # -1 weil wir den index haben wollen
                while i <= len(self.tokenNames) - 1:
                    tokenName = self.tokenNames[i]
                    tokenValue = self.tokenValues[i]

                    # eher die nächsten 2 aber halt das token gerade eingerechnet
                    nextDreiTokenNames = self.tokenNames[i:i+3] # next 3 tokens
                    nextDreiTokenValues = self.tokenValues[i:i+3] # next 3 tokens
                    
                    # schauen ob die token kombination in den rules sind
                    if nextDreiTokenNames == list(rule[0]):

                        #klasse wird instastiatet mit den 2 values der rechnung
                                        #value 1            #value2
                        klasse = rule[2](nextDreiTokenValues[0], nextDreiTokenValues[2])

                        
                        # so dass NUR eine expr übrig bleibt
                        # man kann immer i verwenden da sich alles nach links verschiebt wenn ein element gepopt wird
                        self.tokenNames.pop(i)
                        self.tokenNames.pop(i)
                        self.tokenValues.pop(i)
                        self.tokenValues.pop(i)
                        
                        #  value von der expr wird auf die klasse gesetzt (zb mal)
                        self.tokenValues[i] = klasse
                    
                    i += 1
            for rule in self.rules2:
                i = 0
                while i < len(self.tokenNames) - 2:
                    tokenName = self.tokenNames[i]
                    tokenValue = self.tokenValues[i]

                    nextDreiTokenNames = self.tokenNames[i:i+3] # next 3 tokens
                    nextDreiTokenValues = self.tokenValues[i:i+3] # next 3 tokens
                    if nextDreiTokenNames == list(rule[0]):
                                        #value 1            #value2
                        klasse = rule[2](nextDreiTokenValues[0], nextDreiTokenValues[2])


                        # so dass nur eine expr übrig bleibt
                        self.tokenNames.pop(i)
                        self.tokenNames.pop(i)
                        self.tokenValues.pop(i)
                        self.tokenValues.pop(i)

                        self.tokenValues[i] = klasse
                    
                    i += 1
            for rule in self.rules3:
                i = 0
                while i < len(self.tokenNames) - 2:
                    tokenName = self.tokenNames[i]
                    tokenValue = self.tokenValues[i]

                    nextDreiTokenNames = self.tokenNames[i:i+3] # next 3 tokens
                    nextDreiTokenValues = self.tokenValues[i:i+3] # next 3 tokens
                    if nextDreiTokenNames == list(rule[0]):
                                        #value 1            #value2
                        klasse = rule[2](nextDreiTokenValues[0], nextDreiTokenValues[2])


                        # so dass nur eine expr übrig bleibt
                        self.tokenNames.pop(i)
                        self.tokenNames.pop(i)
                        self.tokenValues.pop(i)
                        self.tokenValues.pop(i)

                        self.tokenValues[i] = klasse
                    
                    i += 1



            # nur für var add (eigentlich dumm aber egal)
            for rule in self.rules35:
                i = 0
                
                while i < len(self.tokenNames):
                    tokenName = self.tokenNames[i]
                    tokenValue = self.tokenValues[i]


                    # da das hier für variablen adden ist, immer 4 token
                    #  1  2  3 4
                    # var +  = x
                    nextDreiTokenNames = self.tokenNames[i:i+4] # next 3 tokens
                    nextDreiTokenValues = self.tokenValues[i:i+4] # next 3 tokens
                    if nextDreiTokenNames == list(rule[0]):

                                        #value 1            #value2
                        klasse = rule[2](nextDreiTokenValues[0], nextDreiTokenValues[3])

                        
                        
                        self.tokenNames.pop(i)
                        self.tokenNames.pop(i) # drei elemente der rule werden gepopt
                        self.tokenNames.pop(i)

                        self.tokenNames[i] = rule[1] # das letzte element muss nicht gelöscht werden, es wird einfach nur ersetzt mit "statement"

                        self.tokenValues.pop(i)
                        self.tokenValues.pop(i)
                        self.tokenValues.pop(i)

                        self.tokenValues[i] = klasse

                    i += 1

            
            for rule in self.rules4:
                i = 0
                
                # durch jedes token durchgehen
                while i <= (len(self.tokenNames) - len(rule[0])) :# nur so lange wie die tokens lang sind
                    
                    nextDreiTokenNames = self.tokenNames[i:i+len(rule[0])] # next 3 tokens
                    nextDreiTokenValues = self.tokenValues[i:i+len(rule[0])] # next 3 tokens
                    if nextDreiTokenNames == list(rule[0]):
                        klasse = rule[2](nextDreiTokenValues)
                        
                        for j in range (len(rule[0]) - 1):
                            # i = current token 
                            #j wie oft popen
                            #j ist so oft wie das statement lang ist
                            self.tokenNames.pop(i)
                            self.tokenValues.pop(i)

                        self.tokenValues[i] = klasse

                        self.tokenNames[i] = rule[1] # statement
                        
                    
                    i += 1

        return self.tokenValues[0] # return ast, [0] weil token values eine liste mit nur einem element ist

class Lexer():
    def lex(self, line):

        self.tokenList = []
        i = 0

        while i < len(line):

            char = line[i]

            if char == "(":
                self.tokenList.append(Token("OP", "("))

            if char == ")":
                self.tokenList.append(Token("CP", ")"))

            if char == "+":
                self.tokenList.append(Token("PLUS", "+"))
            
            if char == "-":
                self.tokenList.append(Token("MINUS", "-"))

            

            if char == "^":
                self.tokenList.append(Token("HOCH", "^"))
            if char in "1234567890.":
                number = ""
                
                while line[i] in "1234567890.":
                    number += line[i]
                    i += 1
                    if i >= len(line):
                        break
                i -= 1
                self.tokenList.append(Token("NUM", number))

            if char == ":":
                self.tokenList.append(Token("DOPPELPUNKT", ":"))

            if char == "/":
                self.tokenList.append(Token("GETEILT", "/"))

            if char == "*":
                self.tokenList.append(Token("MAL", "*"))
            # names
            if char.lower() in "abcdefghijklmnopqrstuvwxyzäöüß" and line[i] != '"':
                text = ""
                while line[i] in "abcdefghijklmnopqrstuvwxyzäöüß":
                    text += str(line[i])
                    i += 1
                    if not i < len(line):
                        break
                if text == "gleich":
                    self.tokenList.append(Token("GLEICH", "gleich"))
                elif text == "plus":
                    self.tokenList.append(Token("PLUS", "+"))
                elif text == "minus":
                    self.tokenList.append(Token("MINUS", "-"))
                elif text == "mal":
                    self.tokenList.append(Token("MAL", "*"))
                elif text == "geteilt":
                    self.tokenList.append(Token("GETEILT", "/"))
                elif text == "wahr":
                    self.tokenList.append(Token("TRUE", "wahr"))
                elif text == "falsch":
                    self.tokenList.append(Token("FALSE", "falsch"))
                elif text == "schreibe":
                    self.tokenList.append(Token("PRINT", "schreibe")) 
                elif text == "falls":
                    self.tokenList.append(Token("IF", "falls"))
                elif text == "sonst":
                    self.tokenList.append(Token("ELSE", "sonst")) 
                else:
                    self.tokenList.append(Token("NAME", text))
                i -= 1

            #strings
            if char.lower() == '"':
                text = ""
                i += 1
                while True:
                    if line[i] != '"':
                        text += str(line[i])
                        i += 1
                    else:
                        break 
                self.tokenList.append(Token("STRING", text))  

            i += 1

        # checken für minus zahlen
        #-1 weil das letzte zeichen in der liste eh kein minus sein kann
        i=0
        while i <= len(self.tokenList) - 1:
            token = self.tokenList[i]
            if token.name == "MINUS":                
                if i == 0 and self.tokenList[i + 1].name == "NUM":
                    self.tokenList.pop(i)
                    self.tokenList[i].value = "-" + self.tokenList[i].value
                    
                    
                if self.tokenList[i - 1].name != "NUM" and self.tokenList[i + 1].name == "NUM":
                    self.tokenList.pop(i)
                    self.tokenList[i].value = "-" + self.tokenList[i].value
                    
            i += 1
        
        return self.tokenList    

lexer = Lexer()
parser = Parser()
for lineIndex, line in enumerate(lines):
    line = line.split("#")[0]   
    tokens = lexer.lex(line)
    #print(f"Token list for line {lineIndex + 1}: {tokens}")
    if len(tokens) >= 1:
        ast = parser.parse(tokens)
        ast.eval()
    





    


