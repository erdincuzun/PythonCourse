# bir metinde üç farklı pazantezin kullanımında kaynaklı hata olup olmadığını bulan kod.
# girdi: '[(3 - 2)+(3 * 2)] * { 3 }'
# çıktı: True / False, Açıklama eklenebilir (Hata varsa hangi tip hata)
# stack uygulaması

def parantezkontrol(metin):
    par = {'(': ')', '[': ']', '{': '}'}
    s = []
    for thel in metin:
        if thel in '[({':
            s.append(thel)
        elif thel in '])}':
            if len(s) > 0:
                x = s.pop()
            else:
                return False, "Stack boş"
            if thel != par[x]:
                return False, "Parantez uyum hatası"

    if len(s) > 0:
        return False, "Fazla parantez"
    
    return True, ":)"

l = '[(3 - 2)+(3 * 2)] * { 3 }'

check, hata = parantezkontrol(l)

print(check, hata)
