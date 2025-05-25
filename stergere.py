import os
import dbConnection

def sterge_comanda():
    try:
        id_stergere = int(input("Introduceti ID-ul comenzii pe care doriti sa o stergeti: ").strip())
    except ValueError:
        print("ID invalid! Trebuie sa fie un numar intreg.")
        input("Apasati 'Enter' pentru a continua.")
        return

    db = dbConnection.creeaza_conexiune()
    if db is None:
        print("Nu s-a putut realiza conexiunea la baza de date.")
        input("Apasati 'Enter' pentru a continua.")
        return

    try:
        cursor = db.cursor()
        query_select = "SELECT * FROM comenzi WHERE id = %s"
        cursor.execute(query_select, (id_stergere,))
        rezultat = cursor.fetchone()

        if rezultat is None:
            print("Nu exista nicio comanda cu acest ID.")
            cursor.close()
            db.close()
            input("Apasati 'Enter' pentru a continua.")
            return

        print("===============================")
        print("Informatii despre comanda care va fi stearsa:")
        print("===============================")
        print(f"ID:\t\t\t{rezultat['id']}")
        print(f"Adresa livrare:\t\t{rezultat['adresa_livrare']}")
        print(f"Data livrare:\t\t{rezultat['data_livrare']}")
        print(f"Status:\t\t\t{rezultat['status']}")
        print("===============================")
        opt = input("Sunteti sigur ca doriti sa stergeti comanda? (D/d = da, orice altceva = nu): ").strip().lower()
        if opt == 'd':
            query_delete = "DELETE FROM comenzi WHERE id = %s"
            cursor.execute(query_delete, (id_stergere,))
            db.commit()
            print("Inregistrarea a fost stearsa cu succes!")
        else:
            print("Inregistrarea NU a fost stearsa!")
        cursor.close()
        db.close()
        input("Apasati 'Enter' pentru a continua.")
    except Exception as e:
        print(f"Eroare la accesarea/stergerea inregistrarii din baza de date: {e} (tip: {type(e)})")
        input("Apasati 'Enter' pentru a continua.")

def meniu_sterge_comanda():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===============================")
    print("Sterge inregistrare")
    print("===============================")
    sterge_comanda()