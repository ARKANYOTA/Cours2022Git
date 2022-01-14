
A = {
    5: {"fg":3   , "fd" : 2   },
    1: {"fg": None, "fd" : 7   },
    7: {"fg": None, "fd" : None},
    2: {"fg": 4   , "fd" : 8   },
    8: {"fg": None, "fd" : None},
    3: {"fg": 1   , "fd" : None},
    4: {"fg": None, "fd" : None}
}

print(A)

def first_elt(A):
    return A.keys()[0]

def taille(A, elt):
    if elt is None:
        return 0
    return 1+taille(A[elt]["fg"]) + taille(A[elt]["fd"])
def hauteur(A, elt):
    if A[elt]["fg"] is None or A[elt]["fd"] is None:
        if A[elt]["fg"] is None and A[elt]["fd"] is None:
            return 0
        if A[elt]["fg"] is None:
            return 1 + hauteur(A, A[elt]["fd"])
        if A[elt]["fd"] is None:
            return 1 + hauteur(A, A[elt]["fg"])
    return 1 + max(hauteur(A, A[elt]["fg"]), hauteur(A, A[elt]["fd"]))

def prefix(A, elt):
    if elt is None:
        return []
    return [elt] + prefix(A, A[elt]["fg"]) + prefix(A, A[elt]["fd"])

def suffixe(A, elt):
    if elt is None:
        return []
    return  suffixe(A, A[elt]["fg"]) + suffixe(A, A[elt]["fd"]) + [elt]
def infixe(A, elt):
    if elt is None:
        return []
    return  infixe(A, A[elt]["fg"]) + [elt] + infixe(A, A[elt]["fd"]) 

def largeur(A, elt):
    liste_finale = []
    f = []
    f.append(elt)
    while len(f)!=0:
        n = f[0]
        f = f[1:]
        liste_finale.append(n)
        if A[n]["fg"] is not None:
            f.append(A[n]["fg"])
        if A[n]["fd"] is not None:
            f.append(A[n]["fd"])
    return  liste_finale

print(hauteur(A, 5))
print(prefix(A, 5))
print(suffixe(A, 5))
print(infixe(A, 5))
print(largeur(A, 5))
