def hanoi(n,d,a,t):
    if n == 1:
        print(d,'-->',a)
    else:
        hanoi(n-1,d,t,a)
        print(d,'-->',a)
        hanoi(n-1,t,a,d)


# hanoi(45, 'D', 'A', 'T')

def fusion(tab1, tab2):
    tab3 = []
    i, j, k = 0, 0, 0
    while i < len(tab1) and j < len(tab2):
        if tab1[i] < tab2[j]:
            tab3.append(tab1[i])
            i += 1
        else:
            tab3.append(tab2[j])
            j += 1
        k += 1

    return tab3


def tri_fusion(tab):
    if len(tab) <= 1:
        return tab
    else:
        tab1 = tri_fusion(tab[:len(tab)//2])
        tab2 = tri_fusion(tab[len(tab)//2:])
        return fusion(tab1, tab2)

print(fusion('ABCDEFGHIJKLMNOPQRSTUVWXYZ','ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
print(tri_fusion([1,3,4,4,3,0]))


