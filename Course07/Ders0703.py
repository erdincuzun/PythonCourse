# 'Merhaba Deneme'

def kactane(s):
    d = {}
    for thes in s:
        if thes in d:
            d[thes] += 1
        else:
            d[thes] = 1
    return d
print(kactane('Merhaba Deneme')) 