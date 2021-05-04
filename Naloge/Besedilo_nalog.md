Uvodne naloge
Hej!

Veseli nas, da se nam boš letos pridružil(a) na Poletnem taboru računalništva. Z ekipo mentorjev se že pripravljamo na tabor in komaj čakamo avgust, ko bomo čas preživeli z vami in vas naučili kaj novega. Še pred tem pa smo zate pripravili nekaj zanimivih računalniških izzivov. Namen teh nalog je, da te na podlagi tvojih rešitev uvrstimo v eno od treh skupin na letošnjem taboru.

Brez skrbi, če še ne znaš programirati in ne poznaš nobenega programskega jezika. V tem primeru lahko z običajnimi besedami opišeš, kako bi se lotil(a) posamezne naloge. Za lažji začetek smo vzeli eno izmed lanskih nalog za primer in jo za lažjo predstavo kaj pričakujemo od vas, rešili na več načinov.

Če že programiraš, bomo tvoje kode zelo veseli. Zaželeno je, da jo objaviš na GitHub in nam na naloge@ptr.si pošlješ povezavo do repozitorija s tvojimi rešitvami. Če ti je Git povsem neznan, lahko kodo stisneš v arhiv in ga pošlješ na isti naslov (naloge@ptr.si).

Datoteke z izvorno ali psevdokodo naj bodo ustrezno poimenovane in sicer nalogaX, kjer je X zaporedna številka naloge (npr. naloga1.py).

Za reševanje spodnjih nalog imaš na voljo 14 dni. In ja, čas pošiljanja povabila k reševanju smo si zabeležili. Če v tem času tvoje kode ne prejmemo, boš samodejno uvrščen(a) v skupino začetnikov. V primeru dodatnih vprašanj sem na voljo na tadej.zlak@ptr.si.

Lepo te pozdravljamo Tadej, Andraž, David, Jaka, Matic in še nekdo, ki ga(jo) boš spoznal(a) na taboru.

0. naloga: Primer naloge, rešene na različne načine
Arne se je zaljubil. Vendar ni prepričan ali je ljubezen obojestranska. Zato poišče marjetico in trga cvetne liste: “Ljubi”, “Ne ljubi”, “Ljubi”, “Ne ljubi”… Pomagaj mu napisati računalniški program, ki sprejme število listkov na marjetici in odgovori z “Ljubi” ali “Ne ljubi”. Vedno začnemo šteti z “Ljubi”.

Primer 1:

Vhod: 12
Izhod: "Ne ljubi"
Primer 2:

Vhod: 15
Izhod: "Ljubi"
Rešitev naloge
Nalogo smo najprej rešili v psevevdokodi, nato še v programskih jezikih Python in Javascript. Psevodkoda je način zapisa oziroma predstavitve algoritma na človeku čim bolj razumljiv način. Ni treba, da se držiš spodnjih primerov, saj sprejmemo vse zapise, ki jih razumemo.

Rešitev v psevdokodi
Osnovna ideja psevdokode je, da korake postopka opišemo z besedami in probleme razbijemo na čim manjše koščke. Najbolje je, če so stavki kratki npr. število povečamo za 1. Enak korak lahko zapišemo tudi bolj matematično kot število = število + 1 ali število += 1. Kar je za znakom #, računalnik preskoči in besedilo za znakom imenujemo komentar.

# Preberi število listov in shrani v spremenljivko steviloListov
steviloListov = preberiSteviloListov()
ljubi = 'Ljubi' # Začnemo z ljubi, zapomnimo si to vrednost v spremenljivki "ljubi"

# Ponavljaj je zanka, ki računalniku naroči, nekaj počne
# dokler pogoj ne velja.
ponavljaj dokler je steviloListov večje od 0 # dokler ima marjetica liste
    # Vse kar je zamaknenjo (tipka Tab na tipkovnici), sodi v zanko
    # Ko zaključi (pogoj ne drži več), skoči ven
    steviloListov = steviloListov - 1 # odtrgamo en list
    če ljubi == 'Ljubi' # Če res ljubi
        ljubi = 'Ne ljubi' # Potem ne ljubi več
    sicer # Če zgornji pogoj ne velja, bo šel računalnik v sicer
        ljubi = 'Ljubi'

izpiši vrednost ljubi # v ljubi smo si zapomnili, kje smo ostali
Zgornji pristop je najbolj naiven. Kaj če ime marjetica 984.631.354.687.354 listov? Trajalo bo lep čas, da odšteva po 1 navzdol proti 0. Z nekaj matematike problem postane sila preprost in hiter. Le preverimo, ali je število sodo ali liho, torej ostanek pri deljenju z 2.

steviloListov = preberiSteviloListo()

# lahko tudi, če je število liho, če 
če je ostanek steviloListov pri deljenju z 2 enako 1
    izpiši "Ljubi"
sicer
    izpiši "Ne ljubi"
Rešitev v jeziku Python
Najprej koda naivnega pristopa:

stListov = int(input("Vnesi št. marjetic: "))
ljubi = True

for i in range(stListov)
    ljubi = not ljubi

print(ljubi)
Nato še rešitev hitrejšega pristopa:

stListov = int(input("Vnesi št. marjetic: "))

if stListov % 2 == 1:
    print("Ljubi")
else
    print("Ne ljubi")
Rešitev v jeziku Javascript
Najprej koda naivnega pristopa:

stListov = parseInt(readline());
let ljubi = true;

while(stListov > 0) {
    stListov -= 1;
    ljubi != ljubi;
}
    
console.log("Ljubi", ljubi)
Nato še rešitev hitrejšega pristopa:

stListov = parseInt(readline())

if (stListov % 2 == 1)
    console.log("Ljubi")
else
    console.log("Ne ljubi")
1. naloga: Diamantna liga
Žiga v prostem času igra računalniške igre in se pogosto hvali o svojih dosežkih. V najljubši igri je uvrščen v tako imenovano diamantno skupino igralcev, za katero potrebuje vsaj 3200 točk, ki se spreminjajo glede na uspešnost v vsaki odigrani igri. Pogosto se hvali, koliko časa je zdržal v diamantni skupini. Ker je odigral že veliko iger, potrebuje tvojo pomoč, da mu pomagaš izračunati, koliko zaporednih iger se je držal nad vključno 3200 točkami.

Za tvoj algoritem je Žiga pripravil podatke o začetnih točkah in seznam o spremembah v številu točk, po vsaki odigrani igri. Na podlagi teh podatkov mu povej največje število zaporednih iger, pri katerih je bil nad vključno 3200 točkami.

Primer vhoda:

3200  // Začetne točke
10    // Število odigranih iger
20    // Sledijo spremembe točk po vsaki odigrani igri
10
-35
20
15
-10
-20
20
-30
-10
Izhod:

5
2. naloga: Zvezdice in kvadratki
Dobri programerji smo velikokrat tudi umetniki in radi ustvarjamo slike s pomočjo znakov, ki jih lahko uporabljamo v ukazni vrstici.

Napiši program, ki prebere število n in z uporabo * izriše kvadratek višine n.

Primer vhoda:

5
Izhod:

*****
*****
*****
*****
*****
3. naloga: Faktorizacija
V kriptografiji so zelo pomembna praštevila. To so števila, deljiva le z 1 in sama s sabo. Zaradi te lastnosti so zelo uporabna pri asimetrični kriptografiji RSA. Vsa ostala števila, ki jih imenujemo sestavljena števila, lahko izrazimo kot produkt praštevil (npr. 6 = 2 * 3, 12 = 2 * 2 * 3, …). Faktorizacija števila večjega od 1 (n > 1) je operacija, ki vsako število razbije na produkt praštevil iz katerih je sestavljen.

Napiši program, ki prebere poljubno celo število (n > 1) ter izpiše zmnožek praštevil, ki ga sestavljajo. Ker faktorizacija velja za težak problem (zato je trenutno tudi RSA varen mehanizem za kriptiranje in podpisovanje) se ne obremenjuj s prevelikimi števili, vendar pazi, da bo tvoj program kar se da hiter.

Primer vhoda:

25
Izhod:

25 = 5*5
Še en primer vhoda:

129360
Izhod:

129360 = 2*2*2*2*3*5*7*7*11
Dodatna naloga
Za dodatne točke lahko dopolniš zgornji program tako, da bo zmnožek izpisan v obliki potenc, kot je tudi v matematiki najbolj pogosto.

Primer vhoda:

129360
Izhod:

129360 = 2^4*3*5*7^2*11
4. naloga: Arhitekti piramid
Vsi poznamo antične Egipčane, Keopsovo piramido in zgodbe o vesoljskih sprejemnikih. Čudež starodavne arhitekture, a vendar je bilo včasih vse preprosteje. Le zložiti so morali težko kamne enega na drugega.

Dandanes, sploh na poletnem taboru računalništva, so stvari velikokrat obrnjene na glavo. Tudi piramide zato ni več tako preprosto postaviti, kljub žerjavom. Novodobni arhitekti morajo zato pred gradnjo vedeti, s katere strani bo največji pritisk na temeljno skalo (najnižjo).

Vsak kamen ima nad seboj dva druga kamna. Sila vedno pride s težjega. Napiši program, ki izračuna silo na temeljni kamen. Sila je največji seštevek, ki ga lahko dobiš, če seštevaš vrednosti pri prehodu od spodnjega ogljišča navzgor. Za lažjo predstavo je dodan primer.

Izračun sile:

4 6 8 8 3 8
       \
 8 3 4 7 6
       /
  3 4 9 6
     /
   2 6 5
      \
    3 5
     /
     8

8 + 7 + 9 + 6 + 5 + 8 = 43
Primer vhoda:

3 2 3 4 5
4 5 6 6
3 5 6
5 6
8
Izhod:

31
Dodatna naloga
Če je le mogoče, ne hrani celotne piramide v pomnilniku.

5. naloga: Sporočilo, ljubezensko?
S simpatijo si se zbližal pri pouku računalništva, kjer sta skupaj raziskovala področje internetne komunikacije in razlike med TCP in UDP komunikacijo. Mesec kasneje ti simpatija pošlje s pridobljenim znanjem sporočilo preko programa, ki ga napiše sama.

Sporočilo dobiš več paketih. Logično saj je veliko in je razbito za lažji prenos. Hitro jih sestaviš skupaj, a ti ni nič jasno, saj je le slika brez smisla. Ne upaš si reči, da sporočila nisi prejel. Še enkrat pregledaš vse in vidiš, da je bilo poslano preko UDP-ja.

Ah, za UDP že ptički čivkajo, da je sporočilo lahko prejeto večkrat ali pa se na poti izgubi in je za vedno pozabljeno. Tudi vrstni red ni zagotovljen. No vsak očitno ne ve, verjetno je bila med poukom kriva kakšna motnja.

Duplikate odstraniš in upaš, da kaj ne manjka. Identificiraš tudi prvi paketek s podatki o velikosti slike in ga izločiš, da ne bo povzročal težav.

Naloga
Zdaj moraš koščke le sestaviti skupaj. Vse skupaj je ena računalniška sestavljanka, pri teh se pa robovi sosednjih koščkov prekrivajo.

V datoteki 05-2-input.txt so prejeti koščki slike. Končna slika veš, da je velika 76x76 znakov in vsak košček 6x6.

Sestavi skupaj sliko in ugotovi, kaj je na njej. Vsi koščki so pravilno obrnjeni in noben ne manjka. Rešitev je le ena. Morda kdaj dobiš še kakšno takšno sporočilo, zato naj bo rešitev splošna.

Primer vhoda:

Zaradi lažje berljivosti je spodaj podan primer za sliko 7x7 in koščki velikosti 3x3.

-MM
MMV
#'O

O`O
'L-
\_/

#'\
##'
-##

/-#
`##
##'

MM'
VMX
O'#

#'O
#`'
#'\

MVM
VMV
O`O

\_/
'U`
###

O'#
--#
/-#
Izhod:

-MMVMM'
MMVMVMX
#'O`O'#
#`'L--#
#'\_/-#
##'U`##
-#####'
Dodatna naloga
Pri prenosu sporočila je prišlo do šuma, slika ima zaradi tega anomalije. Te so v sliki vidne kot ' (apostrof) in ` (tick). Odstrani še šum in ga zamenjaj s presledki.
