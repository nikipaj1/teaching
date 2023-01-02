#!/Users/nikitapajanok/Development/Teaching/teaching/kartojimas/env/bin/python
from pymysql.err import MySQLError

def dalyba_is_nulio():
    dalinys = 7
    daliklis = 0

    if daliklis == 0:
        print("Dalyba is nulio negalima")
    else:
        print(dalinys / daliklis)
    print("Programa vykdoma toliau")
    i += 1

def dalyba_is_nulio_su_except():
    try:
        skaicius = int(input("Iveskite skaiciu: "))
        skaicius1 = int(input("Iveskite antra skaiciu: "))
        print(skaicius / skaicius1)
        open("text.txt")
    except ValueError:
        print("Ivedete klaidinga skaiciu")
    except ZeroDivisionError:
        print("Dalyba is nulio negalima.")
    except FileNotFoundError:
        print("Failas nerastas")


def finally_pavyzdys():
    try:
        print(7 / 0)
    except ZeroDivisionError:
        print("Dalyba is nulio negalima")
    finally:
        print("Todel ivykdysime daugyba: ")
        print(7 * 7)
    print("programa vykdoma toliau")


# def upsert_to_database():
#     database_connection, cursor = None, None
#     try:
#         database_connection = get_database_connection()
#         cursor = get_database_cursor(database_connection)

#         cursor.execute(query)
#         database_connection.commit()
#     except DatabaseError:
#         database_connection.rollback()
    

#     finally:
#         if cursor:
#             cursor.close()
#         if database_connection:
#             database_connection.close()
    

def use_exception_in_input():
    while True:
        try:
            x= int(input("Iveskite skaiciu: "))
            break
        except ValueError:
            print("Ivedete ne skaiciu. Bandykite dar karta.")




def ivesti_nauja_skaiciu():
    try:
        skaicius = int(input("iveskite skaiciu: "))
    except ValueError:
        print("Ivestas klaidingas skaicius")

if __name__ == "__main__":
    # 7 / 0
    # dalyba_is_nulio()
    # dalyba_is_nulio_su_except()
    # ivesti_nauja_skaiciu()
    # dalyba_is_nulio_su_except()
    # finally_pavyzdys()
    use_exception_in_input()