#!/Users/nikitapajanok/Development/Teaching/teaching/kartojimas/env/bin/python
from datetime import timezone
import datetime
import time
import locale
# from tqdm import tqdm

def today():
    print(datetime.datetime.today())

def today_date():
    print(datetime.date.today())

def now_time():
    print(datetime.datetime.today().time())

def laikas_is_ivesties(metai, menuo, diena, valanda, minute, sekunde):
    x = datetime.datetime(metai, menuo, diena, valanda, minute, sekunde)
    print(x)
    print(x.strftime("%A, %d. %B %Y %I:%M%p"))

def laikas_su_lietuviskumu(metai, menuo, diena, valanda, minute, sekunde):
    locale.setlocale(locale.LC_TIME, 'lt_LT.UTF-8')
    x = datetime.datetime(metai, menuo, diena, valanda, minute, sekunde)
    print(x.strftime("%A, %d. %B %Y %H:%M"))


def datu_skirtumas():
    now = datetime.datetime.now()
    nepriklausomybes_diena = datetime.datetime(1990, 3, 11)
    skirtumas = now - nepriklausomybes_diena
    print(skirtumas.days)


def example():
    utcnow = datetime.datetime.now(timezone.utc)
    print(utcnow)


def datetime_ivedimas():
    ivesta_data = input("Iveskite data: ")
    data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
    skirtumas = (datetime.datetime.now() - data)
    print(skirtumas.days * 24)


def kodo_trukme():
    pradzia = datetime.datetime.now()

    for x in tqdm(range(1_000_000)):
        # print("Labas")
        time.sleep(0.0001)
    
    pabaiga = datetime.datetime.now()
    print(f"Programa uztruko {(pabaiga - pradzia).total_seconds()}")
    print(type(pradzia), type(pabaiga))
    print(type((pabaiga - pradzia)))

def kodo_pauze():
    print("Labas")
    time.sleep(2)
    print("Ate")

if __name__ == "__main__":

    # today()
    # today_date()
    # now_time()
    # laikas_is_ivesties(2023, 1, 2, 18, 27, 37)
    # laikas_su_lietuviskumu(2023, 1, 2, 18, 27, 37)
    # datu_skirtumas()
    # example()
    # datetime_ivedimas()

    # now = datetime.datetime.now()
    # print(now.year)
    # print(now.month)
    # print(now.weekday())
    # print(now.day)
    # print(now.hour)
    # print(now.minute)
    # print(now.second)
    # print(now.microsecond)


    kodo_trukme()
    # kodo_pauze()