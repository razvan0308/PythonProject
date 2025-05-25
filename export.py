import os
import csv
import dbConnection

def exporta_comenzi_csv():
    query_select = "SELECT * FROM comenzi"
    try:
        db = dbConnection.creeaza_conexiune()
        cursor = db.cursor()
        cursor.execute(query_select)
        rezultate = cursor.fetchall()
        cursor.close()
        db.close()
    except Exception as e:
        print("Eroare la conexiunea cu baza de date:", e)
        input("Apasa 'Enter' pentru a reveni la meniu.")
        return

    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===============================")
        print("Export tabel 'comenzi' in format CSV")
        print("===============================")
        filename = input("Introduceti numele fisierului (fara extensia .csv): ").strip()
        if not filename:
            print("Numele fisierului nu poate fi gol.")
            input("Apasa 'Enter' pentru a reveni la meniu.")
            return
        filename = filename + ".csv"

        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Scrie antetele
            writer.writerow(["ID", "Adresa Livrare", "Data Livrare", "Status"])
            # Scrie datele
            for row in rezultate:
                # Daca folosesti cursor cu dict, fiecare row e dict, deci:
                writer.writerow([row['id'], row['adresa_livrare'], row['data_livrare'], row['status']])

        print(f"Fisierul {filename} a fost exportat cu succes!")
        input("Apasa 'Enter' pentru a continua.")
    except Exception as e:
        print("Eroare la scrierea fisierului:", e)
        input("Apasa 'Enter' pentru a reveni la meniu.")