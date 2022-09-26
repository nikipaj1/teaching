# Objektinis programavimas

class Kate:
    def __init__(self, spalva, trispalve=False, kojos=4, uodega=1, namine=True):
        self.spalva = spalva
        self.trispalve = trispalve
        self.kojos = kojos
        self.uodega = uodega
        self.namine = namine

    def miaukseti(self, daznis=100):
        print(f"Miau\n"*daznis)
        self.daznis = daznis

    def priskirti_spalva(self, nauja_spalva):
        self.spalva = nauja_spalva

    def __str__(self):
        return f"{self.spalva}-ios spalvos katė, miauksi {self.daznis} kartu. "

# namine_kate = Kate(spalva="balta", trispalve=False, namine=True)    
laukine_kate = Kate(spalva="melyna")    
# namine_kate.spalva = "juoda"
# print(laukine_kate.spalva)
laukine_kate.miaukseti(10)
laukine_kate.priskirti_spalva("žalia")
print(laukine_kate.spalva)
print(str(laukine_kate))

    
# if __name__ == "__main__":
#     namine_kate = Kate(spalva="balta", trispalve=False, namine=True)