import pymysql

HOST = 'localhost'
USER = 'root'
PASSWD = ''
DATABASE = 'firmaLivrare'

def creeaza_conexiune():
    try:
        conexiune = pymysql.connect(
            host=HOST,
            port=3306,
            user=USER,
            passwd=PASSWD,
            db=DATABASE,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Conexiunea la baza de date s-a realizat cu succes!")
        return conexiune
    except Exception as e:
        print("Eroare la conexiunea cu baza de date! -", e)
        return None

def creeaza_baza_de_date():
    try:
        conexiune = pymysql.connect(
            host=HOST,
            port=3306,
            user=USER,
            passwd=PASSWD,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conexiune.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
        conexiune.commit()
        cursor.close()
        conexiune.close()
        print(f"Baza de date {DATABASE} a fost creata (daca nu exista).")
    except Exception as e:
        print("Eroare la crearea bazei de date:", e)

def creeaza_tabela_comenzi():
    conexiune = creeaza_conexiune()
    if conexiune is None:
        return
    try:
        cursor = conexiune.cursor()
        cursor.execute(f"USE {DATABASE}")
        sql = """
        CREATE TABLE IF NOT EXISTS comenzi (
            id INT AUTO_INCREMENT PRIMARY KEY,
            adresa_livrare VARCHAR(255) NOT NULL,
            data_livrare DATE NOT NULL,
            status VARCHAR(50) NOT NULL
        )
        """
        cursor.execute(sql)
        conexiune.commit()
        print("Tabela 'comenzi' a fost creata / exista deja.")
    except Exception as e:
        print("Eroare la crearea tabelei:", e)
    finally:
        cursor.close()
        conexiune.close()

if __name__ == "__main__":
    creeaza_baza_de_date()
    creeaza_tabela_comenzi()