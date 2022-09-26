
"""
kaire_apacia -> [x1, y1]
desine_virsus -> [x2, y2]
"""

class Kvadratas:
    def __init__(self, kaire_apacia, desine_virsus):
        if desine_virsus[0] - kaire_apacia[0] != desine_virsus[1] - kaire_apacia[1]:
            raise ValueError("Ne kvadratas!")
        self.kaire_apacia = kaire_apacia
        self.desine_virsus = desine_virsus
        # self.kaire_virsus = [kaire_apacia[0], desine_virsus[1]]
        self.kaire_virsus, self.desine_apacia = self.gauti_abi_koordinates(kaire_apacia, desine_virsus)

    def gauti_abi_koordinates(self, kaire_apacia, desine_virsus):
        return ([kaire_apacia[0], desine_virsus[1]], [kaire_apacia[0], desine_virsus[1]])

    def apskaiciuoti_krastine(self):
        krastine = self.desine_virsus[0] - self.kaire_virsus[0]
        return krastine

    def pastumti_horizontaliai(self, x):
        self.kaire_apacia[0]  += x
        self.desine_virsus[0] += x
        self.kaire_virsus[0]  += x
        self.desine_apacia[0] += x
        print(
            self.kaire_apacia,
            self.desine_virsus,
            self.kaire_virsus,
            self.desine_apacia
        )

    def pastumti_vertikaliai(self, y):
        self.kaire_apacia[1]  += y
        self.desine_virsus[1] += y
        self.kaire_virsus[1]  += y
        self.desine_apacia[1] += y
        print(
            self.kaire_apacia,
            self.desine_virsus,
            self.kaire_virsus,
            self.desine_apacia
        )
    
    def gauti_koordinates(self):
         print(
            "Kaire apacia: " + str(self.kaire_apacia),
            "Desine virsus: " + str(self.desine_virsus),
            "Kaire virsus:  " + str(self.kaire_virsus),
            "Desine apacia: " + str(self.desine_apacia),
            sep="\n"
        )

def apskaiciuoti(skaicius1: float, skaicius2: float) -> float:
    return skaicius1 + skaicius2

def grazinti_dvi_reiksmes():
    return "vienas", "du"


kvadratas = Kvadratas([0,0], [1,1])
# print(kvadratas.apskaiciuoti_krastine())
# kvadratas.pastumti_vertikaliai(1)
# kvadratas.gauti_koordinates()
var1, var2 = grazinti_dvi_reiksmes()
print(var1)