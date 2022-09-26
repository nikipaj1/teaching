# class Gyvunas:
#     def __init__(self, vardas, spalva):
#         self.vardas = vardas
#         self.spalva = spalva

#     def begti(self):
#         print("Bėgu")


# class Vezlys(Gyvunas):
#     def begti(self):
#         super().begti()
#         print("Aš lėtai einu, ne bėgu")


# vezlys = Vezlys("Tadas", "Rudas")
# vezlys.begti()


from re import A


class Tevas:
    def __init__(self, vardas, pavarde="Jonaitis"):
        self.vardas = vardas
        self.pavarde = pavarde

    def pakviesti(self):
        return self.vardas


class Vaikas(Tevas):
    def __init__(self, vardas, pavarde, mokymosi_istaiga):
        super().__init__(vardas)
        self.mokymosi_istaiga = mokymosi_istaiga

    def tecio_vardas(self):
        return self.pakviesti()


tevas = Tevas("Rokas", "Budreika")
vaikas = Vaikas("Urtė", "Budreikaitė", "Čiurlionio menų gimnazija")

# print(tevas.mokymosi_istaiga)
# print(vaikas.mokymosi_istaiga)
# print(tevas.pavarde)
# print(vaikas.tecio_vardas())


################################
class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    pass


class IslaiduIrasas(Irasas):
    pass


biudzetas = []
irasas1 = PajamuIrasas(2000)
irasas2 = IslaiduIrasas(20)
biudzetas.append(irasas1)
biudzetas.append(irasas2)


# print(biudzetas)

# for x in biudzetas:
#     if isinstance(x, PajamuIrasas):
#         print(x.suma)
#         print("Pajamos")
#     elif isinstance(x, IslaiduIrasas):
#         print(x.suma)
#         print("Islaidos")


class Bandom:
    def __init__(self):
        self._svarbus_raktas = "jahsdfklhasdbf27378rg23l"

    def padaryti_kazka_atvirai(self):
        print("as cia ")

    def _padaryti_kazka_privaciai(self):
        print("As esu slapukas")

    def parodyti_viska(self):
        self.padaryti_kazka_atvirai()
        self._padaryti_kazka_privaciai()

    def __str__(self):
        return "As"


# bandymas1 = Bandom()
# str(bandymas1)


#################################################
#               3 Uzduotis
#################################################


class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga


class Biudzetas:
    def __init__(self, irasai):
        self.irasai = irasai
        self.suma = 0

    def gauti_balansa(self):
        for irasas in self.irasai:
            if isinstance(irasas, PajamuIrasas):
                self.suma += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                self.suma -= irasas.suma
        return f"Jusu balansas yra: {self.suma}"


irasai = []
while True:
    print("iveskite iraso suma, kad iseitumete, iveskite q.")
    suma = input()
    if suma == "q":
        break
    # print("iveskite iraso tipa")
    # tipas = input() # islaidos/pajamos
    if suma < 0:
        print("iveskite atsksaitymo buda")
        atsiskaitymo_budas = input()
        print("iveskite preke")
        isigyta_preke_paslauga = input()
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        irasai.append(irasas)
    else:
        siuntejas = input()
        papildoma_informacija = input()
        irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        irasai.append(irasas)

biudzetas = Biudzetas(irasai)
print(biudzetas.gauti_balansa())
