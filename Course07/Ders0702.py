def enfazlagecen(s):
    enfazla = 0
    ch = ''
    for theC in list(set(s)):
        if s.count(theC) > enfazla:
            enfazla = s.count(theC)
            ch = theC
    return ch, enfazla

print(enfazlagecen('Merhaba Deneme'))
    