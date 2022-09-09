SymbolOne="# "
SymbolTwo=". "
pole=""


def PrintLine(m, n, a, b): #prints a line, m(lenght, a(1stSymbol), b(2ndSymbol)
    radek=""
    global pole
    j = 0
    while j<4:
        m1 = m
        while m1>0:
            i = m1*3
            x = ""
            if (i%6)>0:
                x=(3*a)
            else:
                x=(3*b)
            radek[j]=x
            m1 -= 1
        pole[n]=[radek]
        print("")
        j += 1


def CreatePlayGround(m, n):
    while (n%2)>0:
        PrintLine(m, n, SymbolOne,SymbolTwo)
        PrintLine(m, n, SymbolTwo,SymbolOne)
        n=n-2
    if (n%2)==1:
        PrintLine(m, SymbolOne,SymbolTwo)


CreatePlayGround(8, 8)
