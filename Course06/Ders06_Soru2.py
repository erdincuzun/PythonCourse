# girdi: [5, 4, 3, 2, 1]
# 8 ekle, sondakini sil
# çıktı: [8, 5, 4, 3, 2]
# kuyruk 

def kuyruk_ekle(l, eklenen):
    l.pop()
    l.insert(0, eklenen)
    return l

l = [5, 4, 3, 2, 1]
print(kuyruk_ekle(l, 8))