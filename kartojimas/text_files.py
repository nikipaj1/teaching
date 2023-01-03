#!/Users/nikitapajanok/Development/Teaching/teaching/kartojimas/env/bin/python
import os
import datetime

if __name__ == "__main__":
    # # write file
    # with open("failas.txt", "w", encoding="utf-8") as failas:
    #     failas.write("Labas!!!!! ĄĘČĖĮŠĮĖĘČęėįėęč")

    # write file without context manager
    # failas = open("failas.txt", "w")
    # failas.write("Labas!!!!")
    # failas.close()

    # geriau visada nuskaityti failus su context manageriu
    # WITH

    # nuskaityti teksta is failo
    # with open("failas.txt", "r") as failas:
    #     print(failas.read())

    # Irasyti ir nuskaityti faila vienu metu
    # with open("failas.txt", "r+") as failas:
    #     print(failas.read())
    #     failas.write("\nHello, World!")

    # with open("failas.txt", "r", encoding="utf-8") as failas:
    #     print(failas.read())


    # Kaip prideti, o ne perrasyti teksta (problema)
    # with open('failas.txt', 'w') as f:
    #     f.write("Cia yra pirmas sakinys \n")
    # with open('failas.txt', 'w') as f:
    #     f.write("Cia yra antras sakinys \n")

    # sprendimas
    # with open('failas.txt', 'w') as f:
    #     f.write("Cia yra pirmas sakinys \n")
    # with open('failas.txt', 'a') as f:
    #     f.write("Cia yra antras sakinys \n")

    # kaip perrasyti teksta
    # with open("failas.txt", "w") as f:
    #     f.write("Test")
    #     f.seek(0)
    #     f.write("BEA")


    # kaip skaityti po viena eilute
    # with open("failas.txt", "r", newline="\r\n") as f:
    #     # print(f.readline())
    #     # print(f.readline())
    #     # print(f.readline())
    #     while 1:
    #         newln = f.readline()
    #         if newln != "":
    #             print(newln)
    #         else:
    #             break

    # # with open("failas.txt", "r") as f:
    # #     print(f.readlines())

    # with open("failas.txt", "r") as failas:
    #     for idx, eilute in enumerate(failas):
    #         print(eilute, end="")


    # nuskaityti ribota kieki eiluciu
    # with open("failas.txt", "r") as f:
    #     print(f.read(100))

    # darbas su dviem failais
    # with open("failas.txt", "r") as failas_1:
    #     with open("failo_kopija.txt", "w") as failas_2:
    #         for eilute in failas_1:
    #             failas_2.write(eilute)


    with open("360_F_468808843_7xj0voXr6Sa33pPsonayRz03C6QkWcvD.jpeg", "rb") as failas:
        with open("img_kopija.jpeg", "wb") as failo_kopija:
            for eilute in failas:
                failo_kopija.write(eilute)