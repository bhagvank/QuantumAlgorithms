import math
import random

def ApplyCNOTGate(zerozero,zeroone,onezero,oneone):
    onezero, oneone = oneone, onezero
    return GetQubits(zerozero,zeroone,onezero,oneone)

def ApplyHGate(zerozero,zeroone,onezero,oneone):
    a = zerozero
    b = zeroone
    c = onezero
    d = oneone

    zerozero = a + c
    zeroone  = b + d
    onezero  = a - c
    oneone   = b - d

    normalize()

    return GetQubits(zerozero,zeroone,onezero,oneone)

def ApplyXGate(zerozero,zeroone,onezero,oneone):
    a = zerozero
    b = zeroone
    c = onezero
    d = oneone

    zerozero = c
    zeroone  = d
    onezero  = a
    oneone   = b

    return GetQubits(zerozero,zeroone,onezero,oneone)

def ApplyZGate(zerozero,zeroone,onezero,oneone):
    onezero *= -1
    oneone  *= -1

    return GetQubits(zerozero,zeroone,onezero,oneone)

def ApplyNormalization(zerozero,zeroone,onezero,oneone):
    norm = (abs(zerozero) ** 2 + abs(zeroone) ** 2 +
            abs(onezero) ** 2 + abs(oneone) ** 2) ** 0.5
    zerozero /= norm
    zeroone  /= norm
    onezero  /= norm
    oneone   /= norm
    return GetQubits(zerozero,zeroone,onezero,oneone)

def MeasureQubit(zerozero,zeroone,onezero,oneone):
    zerozeroprob = abs(zerozero) ** 2
    zerooneprob  = abs(zeroone)  ** 2
    onezeroprob  = abs(onezero)  ** 2
    randomchoice = random.random()

    if randomchoice < zerozeroprob:
        zerozero = complex(1)
        zeroone  = complex(0)
        onezero  = complex(0)
        oneone   = complex(0)
        return (0, 0)
    elif randomchoice < zerooneprob:
        zerozero = complex(0)
        zeroone  = complex(1)
        onezero  = complex(0)
        oneone   = complex(0)
        return (0, 1)
    elif randomchoice < onezeroprob:
        zerozero = complex(0)
        zeroone  = complex(0)
        onezero  = complex(1)
        oneone   = complex(0)
        return (1, 0)
    else:
        zerozero = complex(0)
        zeroone  = complex(0)
        onezero  = complex(0)
        oneone   = complex(1)
        return (1, 1)
    
def GetQubits(zerozero,zeroone,onezero,oneone):
    comp = [zerozero, zeroone, onezero, oneone]
    comp = [i.real if i.real == i else i for i in comp]
    comp = [str(i) for i in comp]
    comp = ["" if i == "1.0" else i for i in comp]

    ls = []
    if abs(zerozero) > 0:
        ls += [comp[0] + " |00>"] 
    if abs(zeroone)  > 0:
        ls += [comp[1] + " |01>"] 
    if abs(onezero)  > 0:
        ls += [comp[2]  + " |10>"] 
    if abs(oneone)   > 0:
        ls += [comp[3]   + " |11>"] 

    comp = " + ".join(ls)

    return comp
        
a = 1
b = 0
c = 0
d = 0
zerozero_state = complex(a)
zeroone_state  = complex(b)
onezero_state  = complex(c)
oneone_state   = complex(d)     
result1 = ApplyCNOTGate(zerozero_state,zeroone_state,onezero_state,oneone_state)
print("cnot gate operation - result",result1)
result2 = ApplyXGate(zerozero_state,zeroone_state,onezero_state,oneone_state)
print("xgate operation - result",result2)
result3 = ApplyZGate(zerozero_state,zeroone_state,onezero_state,oneone_state)
print("zgate operation - result",result3)
result4 = ApplyNormalization(zerozero_state,zeroone_state,onezero_state,oneone_state)
print("normalize operation - result",result4)
result5 = MeasureQubit(zerozero_state,zeroone_state,onezero_state,oneone_state)
print("measure gate operation - result",result5)
