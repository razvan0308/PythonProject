import os
import adaugare
import cautare
import modificare
import stergere
import export


def meniu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    ================================
    1 - Adauga comanda livrare
    2 - Cauta comenzi
    3 - Modifica comanda
    4 - Sterge comanda
    5 - Exporta comenzi in CSV
    6 - Iesire
    ================================
    """)
    opt = input("Introduceti optiunea si apasati Enter: ")
    return opt
# as
def main():
    opt = ""
    while opt != "6":
        opt = meniu()
        if opt == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            adaugare.meniu_adauga_comanda()
        elif opt == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            cautare.meniu_cauta_comenzi()
        elif opt == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            modificare.meniu_modifica_comanda()
        elif opt == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            stergere.sterge_comanda()
        elif opt == "5":
            export.exporta_comenzi_csv()
        elif opt == "6":
            print("La revedere!")
        else:
            print("Optiune invalida. Incercati din nou.")

if __name__ == "__main__":
    main()