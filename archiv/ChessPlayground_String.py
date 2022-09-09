SymbolOne="O"
SymbolTwo="X"
List=[]


def PrintList(a): #prints list with structure [[O,X,O],[X,O,X],[O,X,O]]
    for i in range(len(a)) : 
        for j in range(len(a[i])) : 
            print(a[i][j], end="")
        print()   

def AddLine(m, p, a, b): #Adds a line, m(lenght), a(1stSimbol), b(2ndSimbol)
    j=1
    global List
    
    while j>0:
        m1=m
        while m1>0:
            i=m1*3 #total of characters in line still to add
            x=""
            if (i%6)>0:
                x=(3*a)
            else:
                x=(3*b)
            
            List[p] += x #[[radek],[radek]]
            p += 1
            m1 -= 1
        j -= 1
    return p


def Play(m,n):
    while n>0:
        p = 0
        if (n-n%2)>0:
            AddLine(m, p, SymbolOne, SymbolTwo)
            n -= 1
            AddLine(m, p, SymbolTwo, SymbolOne)
            n -= 1
        elif (n%2)==1:
            AddLine(m, p, SymbolOne, SymbolTwo)
            n -= 1


Play(3,3)
print(List)
PrintList(List)


