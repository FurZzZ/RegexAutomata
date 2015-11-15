import graphviz as gv
from graphviz import Digraph
"""
concatenation: ab
alternative: a|b
all: a*
once or more: +
"""

class State:
    def __init__(self, stateName, isFinalState, fromWhichState, influencedBy):
        self.stateName = stateName
        self.isFinalState = isFinalState
        self.fromWhichState = fromWhichState
        self.influencedBy = influencedBy


class Automat:
    def __init__(self, automataName, stateCollection):
        self.automataName = automataName
        self.stateCollection = stateCollection

class FinalnyAutomat:
    def __init__(self, automataName, automataCollection):
        self.automataName = automataName
        self.automataCollection = automataCollection

class Application:
    def __init__ (self, regex):
        self.regex = regex

    def drawGraph(self, stateList, nazwa):
        example = "Example";
        iterator = 1;
        dot = Digraph(comment='Automata')
        SprawdzZero = False
        for x in stateList:

            if x.fromWhichState == "--":
                print("Printing...")
            else:
                if x.isFinalState == True:
                    #dot.node(x.stateName, x.stateName,style="filled",color=".7 .3 1.0")
                    dot.node(x.stateName, x.stateName)
                    dot.edge(x.fromWhichState, x.stateName, label = x.influencedBy)
                else:
                    dot.node(x.stateName, x.stateName)
                    dot.edge(x.fromWhichState, x.stateName, label = x.influencedBy)
        iterator += 1
        dot.save(nazwa+".gv")
        import os
        os.execl('/usr/bin/dot', 'dot', '-Tpng', nazwa+'.gv', '-o '+nazwa+'.png')



    def run(self):
        positionInRegex = 0
        numberOfTheStateName = 0
        numberOfTheStateNameNNN = 0
        isFinalState = False
        splitedRegex = self.regex.split("|")
        numberOfAutomatas = str(len(splitedRegex))
        bracketPosition = []
        bracketPositionChar = []
        stateList = []
        isBracketOpen = 0
        positionOfBracket = -1
        #Iteruj po automatach, i
        for i in numberOfAutomatas:
            #For each state we are adding start State named S0
            zeroState = State("S0", False, "--", "-")
            stateList.append(zeroState)
            numberOfTheStateName = 1
            numberOfTheStateNameNNN = 1
            for fragmentRegex in splitedRegex:
                positionInRegex = 0
                numberOfTheStateName = 1
                positionOfBracket = -1
                for c in fragmentRegex:
                    if c == "(":
                        isBracketOpen = 1
                        bracketPositionChar.append(positionInRegex)
                        bracketPosition.append(numberOfTheStateName)

                    elif c == "+":
                        #if bracket is closed
                        if isBracketOpen == 0:
                            try:
                                #If -1 then it means there wasn't bracket until now.
                                if positionOfBracket == -1:
                                    newState = State("S" + str(numberOfTheStateNameNNN-1), True, stateList[numberOfTheStateNameNNN-1].stateName, fragmentRegex[positionInRegex-1])
                                    stateList.append(newState)
                                else:
                                    if positionInRegex+1 == len(fragmentRegex):
                                        newState = State( stateList[numberOfTheStateNameNNN-1].stateName, True,"S" + str(numberOfTheStateNameNNN-1), fragmentRegex[positionOfBracketChar+1])
                                    else:
                                       newState = State( stateList[numberOfTheStateNameNNN-1].stateName, False,"S" + str(numberOfTheStateNameNNN-1), fragmentRegex[positionOfBracketChar+1]) 
                                    stateList.append(newState)
                                    numberOfTheStateName += 1
                                    numberOfTheStateNameNNN += 1
                            except NameError:
                                print ("Not definied")
                        else:
                            newState = State("S" + str(numberOfTheStateNameNNN-1), True, stateList[numberOfTheStateNameNNN].stateName, fragmentRegex[positionInRegex-1])
                            stateList.append(newState)
                    elif c == "*":
                        #if brackets are closed
                        if isBracketOpen == 0:
                            try:
                                #When -1 -> there won't have been bracket until this time
                                if positionOfBracket == -1:
                                    newState = State("S" + str(numberOfTheStateNameNNN-1), True, stateList[numberOfTheStateNameNNN-1].stateName, fragmentRegex[positionInRegex-1])
                                    stateList.append(newState)
                                else:
                                    if positionInRegex+1 == len(fragmentRegex):
                                        newState = State( stateList[numberOfTheStateNameNNN-2].stateName, True,"S" + str(numberOfTheStateNameNNN-1), fragmentRegex[positionOfBracketChar+1])
                                    else:
                                      newState = State( stateList[numberOfTheStateNameNNN-2].stateName, False,"S" + str(numberOfTheStateNameNNN-1), fragmentRegex[positionOfBracketChar+1])  
                                    stateList.append(newState)
                                    numberOfTheStateName += 1
                                    numberOfTheStateNameNNN += 1
                            except NameError:
                                print ("Not definied")
                        else:
                            newState = State("S" + str(numberOfTheStateNameNNN-1), True, stateList[numberOfTheStateNameNNN].stateName, fragmentRegex[positionInRegex-1])
                            stateList.append(newState)
                    elif c == ")":
                        isBracketOpen = 0
                        positionOfBracket = bracketPosition.pop()
                        positionOfBracketChar = bracketPositionChar.pop()
                        if len(bracketPosition) != 0:
                            isBracketOpen = 1

                    else:
                        if len(fragmentRegex) == 1 or len(fragmentRegex) == 2:
                            helper = True
                        else:
                            helper = False
                        if(numberOfTheStateName == 1):
                            newState = State ("S" + str(numberOfTheStateNameNNN), helper, "S0", c )
                            #numberOfTheStateNameNNN += 1
                        else:
                            newState = State("S" + str(numberOfTheStateNameNNN), helper, "S" + str(numberOfTheStateNameNNN-1), c)
                        stateList.append(newState)
                        numberOfTheStateName += 1
                        numberOfTheStateNameNNN += 1
                    positionInRegex += 1  
            for x in stateList:
                print ("| from state: " + str(x.fromWhichState) + " to state: " + str(x.stateName) + " influenced by: " + str(x.influencedBy) + " is ending state? : " + str(x.isFinalState) + " |") 
        return stateList         





if __name__ == '__main__':
    #Some tests...
    #app = Application("a|b+(cd)+|e|f|gh")
    #State = app.run()
    #Rysuj = app.drawGraph(State, "Example1")
    #print("done...")
    #app2 = Application("a+")
    #State2 = app2.run()
    #Rysuj2 = app2.drawGraph(State2, "Example2")
    #print("done...")
    #app3 = Application("a*")
    #State3 = app3.run()
    #Rysuj3 = app3.drawGraph(State3, "Example3")
    #print("done...")
    app4 = Application("a*b|(b*c)a")
    State4 = app4.run()
    Rysuj4 = app4.drawGraph(State4, "Example4")
