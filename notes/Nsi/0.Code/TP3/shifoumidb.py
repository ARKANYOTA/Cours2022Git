import sqlite3

def main():
    conn = sqlite3.connect('baseDonneesJeu.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Joueurs(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, pseudo TEXT, nbCiseaux INT, nbPierre INT, nbFeuille INT, nbParties INT, nbVictoires INT, ratioVictoire INT)")
    conn.commit()
    pseudo_joueur = input("Pseudo: ")
    
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
