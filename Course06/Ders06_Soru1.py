# girdi: l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# m : 2, n : 3, baştan ve sondan kaç elemanı seçeceğimizi belirler
# çıktı: [8, 9, 0, 3, 4, 5, 6, 7, 1, 2]

def liste_degistir(l, m=2, n=2):
    if m + n > len(l):
        return l
    return l[-n:] + l[m:-n] + l[:m]


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(liste_degistir(l, 2, 3))
print(liste_degistir(l, 1, 2))
print(liste_degistir(l, 1, 5))
print(liste_degistir(m = 2, n = 3, l = l))
print(liste_degistir(l))
print(liste_degistir(l, n = 4))