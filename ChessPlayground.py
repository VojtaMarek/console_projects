SymbolOne="# "
SymbolTwo=". "



def PrintLine(m, a, b): #prints a line, m(lenght, a(1stSimbol), b(2ndSimbol)
    j=3
    while j>0:
        m1=m
        while m1>0:
            i=m1*3
            if (i%6)>0:
                print(3*a, end="")
            else:
                print(3*b, end="")
            m1 -= 1
        print("")
        j -= 1


def CreatePlayGround(m,n):
    while (n-n%2)>0:
        PrintLine(m, SymbolOne,SymbolTwo)
        PrintLine(m, SymbolTwo,SymbolOne)
        n=n-2
    if (n%2)==1:
        PrintLine(m, SymbolOne,SymbolTwo)

print("Lines:")
n = input()
print("Columns:")
m = input()

try:
    CreatePlayGround(int(m),int(n))
except ValueError:
    print("Wrong entry, so lets play chess!")
    CreatePlayGround(8,8)
