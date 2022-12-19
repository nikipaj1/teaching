from models import Projektas
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()


while 1:
    pasirinkimas = int(input("Pasirinkite veiksma: \n1 - Atvaizduoti projektus \n2 - sukurti projekta \n3 - pakeisti projekta \n4 - istrinti projekta\n"))

    if pasirinkimas == 1:
        projektai = session.query(Projektas).all()
        print('-' * 10)
        for projektas in projektai:
            print(projektas)
        print('-' * 10)

    if pasirinkimas == 2:
        name = input("Iveskite projekto pavadinima\n")
        price = float(input("Iveskite projekto kaina\n"))
        projektas = Projektas(name, price)
        session.add(projektas)
        session.commit()

    if pasirinkimas == 3:
        projektai = session.query(Projektas).all()
        print('-' * 10)
        for projektas in projektai:
            print(projektas)
        print('-' * 10)
        keiciamo_id = int(input("Pasirinkite norimo pakeisti projekto ID"))
        keiciamas_projektas = session.query(Projektas).get(keiciamo_id)
        pakeitimas = int(input("Ką norite pakeisti: 1 - pavadinimą, 2 - kainą"))
        if pakeitimas == 1:
            keiciamas_projektas.name = input("Įveskite projekto pavadinimą")
        if pakeitimas == 2:
            keiciamas_projektas.price = float(input("Įveskite projekto kainą"))
        
        session.commit()

    if pasirinkimas == 4:
        projektai = session.query(Projektas).all()
        print('-' * 10)
        for projektas in projektai:
            print(projektas)
        print('-' * 10)
        trinamo_id = int(input("Pasirinkite norimo ištrinti projekto ID"))
        trinamas_projektas = session.query(Projektas).get(trinamo_id)
        session.delete(trinamas_projektas)
        session.commit()