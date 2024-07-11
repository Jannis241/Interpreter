# nach .dede dateien suchen
# dann hier im terminal eingeben: start "name der datei.dede"
# dann wird diese datei ausgeführt
variables = {}  # dict with all stored variables ->  name : value


class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"{self.name}: {self.value}"


class Lexer:
    def __init__(self) -> None:
        pass

    def createTokens(self, line):
        self.tokenList = []
        i = 0
        while i < len(line):
            char = line[i]
            if char == "(":
                newToken = Token("lParent", "(")
                self.tokenList.append(newToken)

            if char == ")":
                newToken = Token("rParent", ")")
                self.tokenList.append(newToken)

            if char == "+":
                newToken = Token("PLUS", "+")
                self.tokenList.append(newToken)

            if char == "-":
                newToken = Token("MINUS", "-")
                self.tokenList.append(newToken)

            if char == "^":
                newToken = Token("HOCH", "^")
                self.tokenList.append(newToken)

            if char == ":":
                newToken = Token("DOPPELPUNKT", ":")
                self.tokenList.append(newToken)

            if char == "/":
                newToken = Token("GETEILT", "/")
                self.tokenList.append(newToken)

            if char == "=":
                newToken = Token("GLEICH", "=")
                self.tokenList.append(newToken)
            if char == "*":
                newToken = Token("MAL", "*")
                self.tokenList.append(newToken)

            if char in "123456789.":
                # found the start of a number
                number = ""
                while line[i] in "123456789.":
                    number += line[i]
                    i += 1
                    if i >= len(line):
                        break
                i -= 1
                newToken = Token("NUM", number)
                self.tokenList.append(newToken)

            abc = "abcdefghijklmnopqrstuvwxyzäöüß"

            # names -> print, für, während, variablen usw
            if char.lower() in abc and line[i] != '"':
                text = ""
                while line[i] in abc:
                    text += str(line[i])
                    i += 1
                    if i >= len(line):
                        break

                if text == "ja":
                    newToken = Token("TRUE", "ja")
                    self.tokenList.append(newToken)

                elif text == "nein":
                    newToken = Token("FALSE", "nein")
                    self.tokenList.append(newToken)

                elif text == "schreibe":
                    newToken = Token("PRINT", "schreibe")
                    self.tokenList.append(newToken)

                elif text == "falls":
                    newToken = Token("IF", "falls")
                    self.tokenList.append(newToken)

                elif text == "sonst":
                    newToken = Token("ELSE", "sonst")
                    self.tokenList.append(newToken)
                else:
                    newToken = Token("NAME", text)
                    self.tokenList.append(newToken)
                i -= 1

            # strings
            if char.lower() == '"':
                text = ""
                i += 1
                while line[i] != '"':
                    text += str(line[i])
                    i += 1

                newToken = Token("STRING", text)
                self.tokenList.append(newToken)
            i += 1

        # nochmal durch alles tokens gehen um zu gucken ob vor einer nummer ein minus ist

        i = 0
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


class Parser:
    pass


def start():
    lexer = Lexer()
    parser = Parser()

    with open("text.txt", "r") as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        line = line.split("#")[0]
        tokenList = lexer.createTokens(line)
        print(f"Tokens für line {idx + 1}: {tokenList}")


start()
