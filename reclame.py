from functies import decoreer

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro, "
            f"waarover {btw_bedrag} euro btw betaald dient te worden.")

inkomsten_week = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
print(inkomsten_totaal(inkomsten_week, btw_percentage))

def laag_hoog(mijn_lijst):
    return [min(inkomsten_week), max(inkomsten_week)]

inkomsten_week = [220, 430, 125, 160, 205, 90, 345]
print(laag_hoog(inkomsten_week))

def gemiddelde(mijn_lijst):
    gemiddelde_inkomsten = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro."
inkomsten_week = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(inkomsten_week))

def meervoudig(invoer_lijst):
    return [min(inkomsten_week), max(inkomsten_week)]

inkomsten_week = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(inkomsten_week))

decoreer("functies_2")


