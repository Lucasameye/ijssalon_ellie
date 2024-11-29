a = 4
def mijn_functie(a):
    return a * a
print(mijn_functie(a))

def decoreer(tekst=""):
    def mijn_functie2(a=12,b=3):
        return (a + b, a - b, a * b, a / b) 
    print(mijn_functie2())



