import dbConnection
import datetime

def meniu_modifica_comanda():
    print("===============================")
    print("Modificare inregistrare in baza de date:")
    print("===============================")

    try:
        id_comanda = int(input("Introduceti ID-ul comenzii pe care doriti sa o modificati: ").strip())
    except ValueError:
        print("ID invalid! Trebuie sa fie un numar intreg.")
        input("Apasati Enter pentru a continua.")
        return

    query_select = "SELECT * FROM comenzi WHERE id = %s"

    try:
        db = dbConnection.creeaza_conexiune()
        if db is None:
            print("Nu s-a putut realiza conexiunea la baza de date.")
            return
        cursor = db.cursor()
        cursor.execute(query_select, (id_comanda,))
        rezultat = cursor.fetchone()
        if rezultat is None:
            print(f"Comanda cu ID {id_comanda} nu a fost gasita.")
            cursor.close()
            db.close()
            input("Apasati Enter pentru a continua.")
            return

        print("===============================")
        print("Comanda care va fi modificata:")
        print("===============================")
        print(f"1 - ID:\t\t\t{rezultat['id']}")
        print(f"2 - Adresa livrare:\t{rezultat['adresa_livrare']}")
        print(f"3 - Data livrare:\t{rezultat['data_livrare']}")
        print(f"4 - Status:\t\t{rezultat['status']}")
        print("===============================")

        opt = input("Introduceti numarul campului pe care doriti sa-l modificati si apasati Enter: ").strip()

        camp_modificat = ""
        noua_valoare = None

        if opt == "1":
            print("ID-ul este unic si nu poate fi modificat.")
            input("Apasati Enter pentru a continua.")
            return
        elif opt == "2":
            camp_modificat = "adresa_livrare"
            noua_valoare = input("Introduceti noua adresa de livrare: ").strip()
        elif opt == "3":
            camp_modificat = "data_livrare"
            while True:
                data_str = input("Introduceti noua data de livrare (YYYY-MM-DD): ").strip()
                try:
                    data_obj = datetime.datetime.strptime(data_str, "%Y-%m-%d").date()
                    noua_valoare = data_obj
                    break
                except ValueError:
                    print("Format invalid pentru data. Va rugam sa introduceti data in formatul YYYY-MM-DD.")
        elif opt == "4":
            camp_modificat = "status"
            print("Status posibil:")
            print("1 - In procesare")
            print("2 - Livrata")
            print("3 - Anulata")
            status_opt = input("Selectati noul status (1/2/3): ").strip()
            if status_opt == "1":
                noua_valoare = "In procesare"
            elif status_opt == "2":
                noua_valoare = "Livrata"
            elif status_opt == "3":
                noua_valoare = "Anulata"
            else:
                print("Optiune invalida pentru status!")
                input("Apasati Enter pentru a continua.")
                return
        else:
            print("Optiune invalida!")
            input("Apasati Enter pentru a continua.")
            return

        query_update = f"UPDATE comenzi SET {camp_modificat} = %s WHERE id = %s"
        cursor.execute(query_update, (noua_valoare, id_comanda))
        db.commit()

        # Afisare noua valoare
        cursor.execute(query_select, (id_comanda,))
        rezultat_modificat = cursor.fetchone()

        print("===============================")
        print("Inregistrare modificata:")
        print("===============================")
        print(f"1 - ID:\t\t\t{rezultat_modificat['id']}")
        print(f"2 - Adresa livrare:\t{rezultat_modificat['adresa_livrare']}")
        print(f"3 - Data livrare:\t{rezultat_modificat['data_livrare']}")
        print(f"4 - Status:\t\t{rezultat_modificat['status']}")
        print("===============================")

        cursor.close()
        db.close()
        input("Apasati Enter pentru a continua.")

    except Exception as e:
        print("Eroare la modificarea inregistrarii:", e)
        input("Apasati Enter pentru a continua.")