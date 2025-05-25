import dbConnection
import datetime

def adauga_comanda(adresa_livrare, data_livrare, status):
    sql_insert = "INSERT INTO comenzi (adresa_livrare, data_livrare, status) VALUES (%s, %s, %s)"
    try:
        db = dbConnection.creeaza_conexiune()
        if db is None:
            print("Nu s-a putut realiza conexiunea la baza de date.")
            return
        cursor = db.cursor()
        try:
            cursor.execute(sql_insert, (adresa_livrare, data_livrare, status))
            db.commit()
            print("Comanda a fost adaugata cu succes!")
        except Exception as e:
            print("Eroare la executarea interogarii:", e)
        finally:
            cursor.close()
            db.close()
    except Exception as e:
        print("Eroare la adaugarea in baza de date:", e)

def meniu_adauga_comanda():
    print("===============================")
    print("Adauga o comanda noua in baza de date:")
    print("===============================")

    adresa = input("Introduceti adresa de livrare: ").strip()

    # Cerem data livrarii si validam formatul
    while True:
        data_str = input("Introduceti data livrarii (YYYY-MM-DD): ").strip()
        try:
            data_livrare = datetime.datetime.strptime(data_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Format invalid pentru data. Va rugam sa introduceti data in formatul YYYY-MM-DD.")

    # Status presetat cu optiuni
    print("Status comanda:")
    print("1 - In procesare")
    print("2 - Livrata")
    print("3 - Anulata")
    status_opt = input("Selectati statusul (1/2/3): ").strip()

    if status_opt == "1":
        status = "In procesare"
    elif status_opt == "2":
        status = "Livrata"
    elif status_opt == "3":
        status = "Anulata"
    else:
        print("Optiune invalida pentru status!")
        input("Apasati Enter pentru a reveni la meniu.")
        return

    adauga_comanda(adresa, data_livrare, status)
    input("Apasati Enter pentru a continua...")