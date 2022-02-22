#!/usr/bin/env python
# ┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04  ┃
# ┃ Creation: 08/09/2021                        ┃
# ┃ Mise a jour: 11/09/2021 22:36               ┃
# ┃ Fichier: 1.1.carlisi_nolan_progF1.py        ┃
# ┃ Exercice fiche 1                            ┃
# ┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

def transpose():
    """Create a transposed of table"""
def Exo1():
    txt = input("Votre texte : ")
    n = int(input("Votre entier : "))
    print("Le texte saisiest : " + txt)
    print("Il contient " + str(len(txt)) + " charactères")
    print("L'entier saisi est " + str(n) + " et son carré est " + str(n ** 2))


def Exo2():
    name = input("Nom : ")
    first = input("Prénom : ")
    age = input("Age : ")
    out = name + " " + first + " " + age + " ans"
    print(out)


def Exo3():
    a = int(input("Saisir la valeur d'un entier a : "))
    b = int(input("Saisir la valeur d'un entier b : "))
    s, p, r, e = a + b, a * b, a % b, a ** b
    print(f"La somme de {a} par {b} vaut {s}")
    print(f"Le produit de {a} par {b} vaut {p}")
    print(f"Le rest de la division euclidienne de {a} par {b} vaut {r}")
    print(f"{a} pruissance {b} vaut {e}")


def Exo4():
    naissance = int(input("Année de naissance : "))
    annee = int(input("Donner une année : "))
    print(f"En {annee} tu auras {annee - naissance} ans.")


def Exo5():
    txt = input("le texte : ")
    if len(txt) < 2:
        raise Exception("le texte est trop court")
    n = int(input("nombre d'étoiles : "))
    print(txt[:2] + "*" * n + txt[-2:])


def Exo6():
    j = int(input("jour : "))
    if not (1 <= j and j <= 31):
        raise Exception("Mauvais jour")
    m = int(input("mois : "))
    if not 1 <= m and m <= 12:
        raise Exception("Mauvais mois")
    a = int(input("année : "))
    if not (len(str(a)) == 4 and 1900 <= a and a <= 2100):
        raise Exception("Mauvaise année")
    print(f"{j}{m}{a}{(j + m + a) % 97}")


def Exo7():
    j = int(input("jour : "))
    if not (1 <= j and j <= 31):
        raise Exception("Mauvais jour")
    m = int(input("mois : "))
    if not 1 <= m and m <= 12:
        raise Exception("Mauvais mois")
    a = int(input("année : "))
    if not (len(str(a)) == 4 and 1900 <= a and a <= 2100):
        raise Exception("Mauvaise année")

    date = str(j) + "/" + str(m) + "/" + str(a)
    print(date)


def Exo8():
    j = int(input("jour : "))
    if not (1 <= j and j <= 31):
        raise Exception("Mauvais jour")
    m = int(input("mois : "))
    if not 1 <= m and m <= 12:
        raise Exception("Mauvais mois")
    a = int(input("année : "))
    if not (len(str(a)) == 4 and 1900 <= a and a <= 2100):
        raise Exception("Mauvaise année")
    if j < 10:
        j = "0" + str(j)
    if m < 10:
        m = "0" + str(m)
    date = str(j) + "/" + str(m) + "/" + str(a)
    print(date)


def Exo9():
    date = input("Saisir une date au format jj/mm/aaaa : ")
    # Supprimer tout les / sans .replace ou autre functions
    new_date = ""
    for i in date:
        if i != "/":
            new_date += i
    print("le nommbre N s'écrit : " + new_date)
    int_new_date = int(new_date)
    print("le nommbre N vaut : " + str(int_new_date))
    cle = int_new_date % 97
    print("La clé est : " + str(cle))
    code = str(new_date) + str(cle)
    print("le code est : " + code)


def Exo10():
    code = input("Votre code secret : ")
    print(str(int(code[:8]) % 97) == code[8:])


def lire_an():
    for i in range(5, -1, -1):
        a = int(input("Année : "))
        if 1900 <= a and a <= 2100:
            return a
        else:
            print(f"Mauvaise année non valide, elle doit être comprise en 1900 et 2100 inclus, plus que {i} essais")
    raise Exception("Mauvaise Année")


def lire_mois():
    for i in range(5, -1, -1):
        a = int(input("Mois : "))
        if 1 <= a and a <= 12:
            return a
        else:
            print(f"Mauvais mois non valide, elle doit être comprise en 1 et 12 inclus, plus que {i} essais")
    raise Exception("Mauvais Mois")


def lire_jour(a, m):
    # Il sont deja dans les ecats 
    for i in range(5, -1, -1):
        j = int(input("Jour : "))
        if m == 2:  # Février
            # Verifier les années bixestile 
            if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
                max_day = 29
            else:
                max_day = 28
        else:
            if m in [1, 3, 5, 8, 10, 12]:
                max_day = 31
            else:
                max_day = 30
        if 1 <= j and j <= max_day:
            return j
        else:
            print(f"Mauvais jour non valide, elle doit être comprise en 1 et  inclus, plus que {i} essais")
    raise Exception("Mauvais Jour")


def Exo11():
    a = lire_an()
    m = lire_mois()
    j = lire_jour(a, m)
    return (a, m, j)


def Espacement(n):
    print("=================")
    print(f"Exo {n}\n")


if __name__ == "__main__":
    Espacement(1)
    Exo1()
    Espacement(2)
    Exo2()
    Espacement(3)
    Exo3()
    Espacement(4)
    Exo4()
    Espacement(5)
    Exo5()
    Espacement(6)
    Exo6()
    Espacement(7)
    Exo7()
    Espacement(8)
    Exo8()
    Espacement(9)
    Exo9()
    Espacement(10)
    Exo10()
    Espacement(11)
    print(f"Date (aaaa, mm, jj): {Exo11()}")
