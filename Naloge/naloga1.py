#definiramo spremenljivke
zacetna = int(input('Vnesi zacetno vrednost: '))
st_ponovitev = int(input('Vnesi stevilo ponovitev: '))
st = int(0)
sestevek = int(0)

#dodamo zacetno vrednost v sesetevek
sestevek = zacetna

#z zanko vnesemo nove tocke
while (st_ponovitev > 0):
    st = int(input('Vnesi stevilo tock: '))
    sestevek = sestevek + st
    st_ponovitev -= 1

#izpisemo rezultat
print(sestevek)