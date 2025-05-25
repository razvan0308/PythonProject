import os
import dbConnection

def cauta_comenzi(camp_cautare, text_cautare):
    query_select = f"SELECT * FROM comenzi WHERE {camp_cautare} = %s"
    try:
        db = dbConnection.creeaza_conexiune()
        if db is None:
            print("Nu s-a putut realiza conexiunea la baza de date.")
            return
        cursor = db.cursor()
        cursor.execute(query_select, (text_cautare,))
        rezultate = cursor.fetchall()
        cursor.close()
        db.close()
    except Exception as e:
        print("Eroare la conexiunea cu baza de date:", e)
        input("Apasati 'Enter' pentru a continua.")
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    print("===============================")
    print("Cautare comenzi in baza de date:")
    print("===============================")
    if not rezultate:
        print("Nu a fost gasita nicio inregistrare!")
        print("===============================")
    else:
        for entry in rezultate:
            print(f"ID:\t\t\t{entry['id']}")
            print(f"Adresa livrare:\t{entry['adresa_livrare']}")
            print(f"Data livrare:\t{entry['data_livrare']}")
            print(f"Status:\t\t{entry['status']}")
            print("===============================")
    input("\n\nApasați 'Enter' pentru a continua: ")

def meniu_cauta_comenzi():
    print("""
    ===============================
    Alegeti criteriul de cautare:
    1 - Dupa ID
    2 - Dupa adresa de livrare
    3 - Dupa data livrarii
    4 - Dupa status
    """)
    opt = input("Introduceti optiunea si apasați 'Enter': ").strip()

    camp_cautare = ""
    text_cautare = None

    if opt == "1":
        camp_cautare = "id"
        try:
            text_cautare = int(input("Introduceti ID-ul comenzii: ").strip())
        except ValueError:
            print("ID-ul trebuie sa fie un numar intreg!")
            input("Apasati 'Enter' pentru a reveni la meniu.")
            return
    elif opt == "2":
        camp_cautare = "adresa_livrare"
        text_cautare = input("Introduceti adresa de livrare: ").strip()
    elif opt == "3":
        camp_cautare = "data_livrare"
        text_cautare = input("Introduceti data livrarii (YYYY-MM-DD): ").strip()
    elif opt == "4":
        camp_cautare = "status"
        print("""
        Introduceti statusul:
        1 - In procesare
        2 - Livrata
        3 - Anulata
        """)
        optiune_status = input("\t").strip()
        if optiune_status == "1":
            text_cautare = "In procesare"
        elif optiune_status == "2":
            text_cautare = "Livrata"
        elif optiune_status == "3":
            text_cautare = "Anulata"
        else:
            print("Optiune invalida!")
            input("Apasati 'Enter' pentru a reveni la meniu.")
            return
    else:
        print("Ati introdus date greșite!")
        input("Apasati 'Enter' pentru a reveni la meniu.")
        return

    cauta_comenzi(camp_cautare, text_cautare)