from bs4 import BeautifulSoup

def pasisveikinti(vardas):
    print(f"Sveika, {vardas}!\n" * 10)

def pakelti_laipnsiu(skaicius, laipsnis):
    pakeltas_skacius = skaicius ** laipsnis
    # print(pakeltas_skacius)
    return pakeltas_skacius

def pakelti_kvadratu(skaicius):
    pakeltas_skacius = skaicius ** 2
    # print(pakeltas_skacius)
    return pakeltas_skacius

def kaina_viso(obuoliu_kiekis, obuolio_kaina=1.5):
    viso = obuoliu_kiekis * obuolio_kaina
    return f"{viso}$"


def daug_kvadratu(*args):
    for skaicius in args:
        print(skaicius ** 2)

def spausdinti_teskta(**kwargs):
    for raktas, reiksme in kwargs.items():
        print(raktas, reiksme)


# list comprehensions



if __name__ == "__main__":
    # pasisveikinti("")
    # pakeltas_skaicius_laipsniu = pakelti_laipnsiu(2, 2)

    # rezultatas = kaina_viso(obuoliu_kiekis=3, obuolio_kaina=1.5)
    # print(rezultatas)

    # zodziai = {"pirmas": "as", "antras": "megstu", "trecias": "pythona"}

    # spausdinti_teskta(vardas="Jonas", pavarde="Jonaitis")

    """
     ... -> {vardas: Jonas, pavarde: Jonaitis} -> .items() 
        -> [(vardas, Jonas), (pavarde, Jonaitis)] 
            -> 
    """
    atspausdinti = lambda x: print(x)
    # atspausdinti("As lambda funkcija")

    sarasas = [1,2,3,4,5,6,7,8,9,10]
    
    for i in range(len(sarasas)):
        sarasas[i] = sarasas[i] ** 2



    daugyba_is_saves = [lambda i=skaicius: i*i for skaicius in range(1, 6)]
    for vienas in daugyba_is_saves:
        print(vienas())
    