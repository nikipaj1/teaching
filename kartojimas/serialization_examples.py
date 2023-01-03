#!/Users/nikitapajanok/Development/Teaching/teaching/kartojimas/env/bin/python
import pickle

a = 1024

# with open("a.pkl", "wb") as pickle_out:
#     pickle.dump(a, pickle_out)


# with open("a.pkl", "rb") as pickle_in:
#     naujas_a = pickle.load(pickle_in)

# print(naujas_a)




# zodynas = {1:"Pirmas", 2:"Antras", 3:"Trečias"}
# with open("zodynas.pkl", "wb") as f:
#     pickle.dump(zodynas, f)

# with open("zodynas.pkl", "rb") as f:
#     naujas_zodynas = pickle.load(f)

# print(naujas_zodynas)


a = 10
b = 7
c = 3

with open("abc.pkl", "wb") as pickle_out:
    pickle.dump(a, pickle_out)
    pickle.dump(b, pickle_out)
    pickle.dump(c, pickle_out)

with open("abc.pkl", "rb") as pickle_in:

    while True:
        try:
            # naujas_a = pickle.load(pickle_in)
            # naujas_b = pickle.load(pickle_in)
            # naujas_c = pickle.load(pickle_in)
            # naujas_d = pickle.load(pickle_in)
            print(pickle.load(pickle_in))
        except EOFError:
            print("baigesi")
            break

# print(a)
# print(b)
# print(c)


# # pavyzdys su vardu sarasu
# while True:
#     try:
#         veiksmas = int(input("Pasirinkite veiksma: 1 - perziureti, 2 - irasyti, 3 - iseiti\n\n"))
        
#         if veiksmas == 1:
#             try:
#                 with open("zmones.pkl", "rb") as failas:
#                     print(pickle.load(failas))
#             except:
#                 print("Nera tokio failo")
#                 with open("zmones.pkl", "wb") as failas:
#                     zmones = []
#                     pickle.dump(zmones, failas)
        
#         if veiksmas == 2:
#             with open("zmones.pkl", "rb") as failas:
#                 zmones = pickle.load(failas)
#                 vardas = input("Iveskite nauja varda: ")
#                 with open("zmones.pkl", "wb") as failas:
#                     zmones.append(vardas)
#                     pickle.dump(zmones, failas)
#         if veiksmas == 3:
#             print("Programa baitgta. Viso gero.")
#             break
#     except ValueError:
#         print("Ivedete neteisinga skaiciu")