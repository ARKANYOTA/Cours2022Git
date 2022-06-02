import sqlite3

data = [('Yphe', 'Yphe@compote.com', 0),
        ('Zirak', 'Zirak34@hibou.fr', 100),
        ('Tikal', 'twouini@music.fr', 50),
        ('Nyse', 'Niz@patate.com', 0)]


def main():
    conn = sqlite3.connect('baseDonnees.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Joueurs(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, pseudo TEXT, mail TEXT, score FLOAT)")
    zirac350 = (350, 'Zirak')
    cur.execute("UPDATE Joueurs SET score = ? WHERE pseudo = ?", zirac350)

    conn.commit()
    cur.close()
    conn.close()


def main_exo1():
    conn = sqlite3.connect('baseDonnees.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Joueurs(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, pseudo TEXT, mail TEXT, score FLOAT)")
    cur.executemany("INSERT INTO Joueurs (pseudo, mail, score) VALUES (?, ?, ?)", data)
    conn.commit()
    cur.close()
    conn.close()


def main_exo2():
    conn = sqlite3.connect('baseDonnees.db')
    cur = conn.cursor()
    modif = (9999, 'Yphe')
    cur.execute("UPDATE Joueurs SET score = ? WHERE pseudo = ?", modif)
    suppr = ('Yphe',)
    cur.execute("DELETE FROM Joueurs WHERE pseudo = ?", suppr)
    conn.commit()
    cur.close()
    conn.close()


def main_exo3():
    conn = sqlite3.connect('baseDonnees.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Joueurs")
    conn.commit()
    listeResultat = cur.fetchall()
    print(listeResultat)
    recherche = ('Zirak',)
    cur.execute("SELECT score FROM Joueurs WHERE pseudo = ?", recherche)
    conn.commit()
    listeResultat = cur.fetchall()
    print(listeResultat)
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
