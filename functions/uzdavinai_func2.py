"""
1. Yra sugeneruojami random pagalba 4 skaiciai (nuo 0000 iki 9999).
2. Tada paprasoma konsoleje suvesti kiek bandymų spėti turime. (Tarkim vartotojas suves 3 kartus)
3. Vartotojo prasoma meginsti atspeti skaiciu (pvz vartotojas speja 0123).
4. Sistema skaiciuoja kiek skaiciu yra karvių, ir kiek yra bulių. Karve yra toks skaicius, kuris yra teisingas, bet stovi ne savo vietoje, bulius – ir teisingas, ir teisingoje vietoje. Jei visi buliai – zaidimo pabaiga.
5. Jei skaicius neatspetas per nustatyta bandymu skaiciu – zaidimas pralostas.



"""

'''
Parašykite funkciją, kuri paima du list'us ir prie pirmojo list pirmojo elemento prideda antrojo listpirmąjį elementą,
antrojo sąrašo antrąjį elementą, antrojo sąrašo antrąjį elementą ir antrojo sąrašo antrąjį elementą. pirmąjį sąrašą su
antruoju antrojo sąrašo elementu ir t. t., ir t. t. Grąžinkite True, jei visi elementų deriniai sudaro tą patį skaičių.
Priešingu atveju grąžinama False. Pavyzdys:
'''


def same_numbers(a: list, b: list)-> bool:
    if len(a) == len(b):
        for i in range((len(a)-1)):
            if a[i]+b[i] != a[i+1]+b[i+1]:
                return False
        return True
    return False


a = [1, 2, 3,]
b = [4, 3, 2, 1]
print(same_numbers(a, b))

'''
Tarp lyginių ir nelyginių skaičių vyksta didelis karas. Šiame kare jau žuvo daug skaičių, todėl tavo užduotis - 
jį nutraukti. Jūs turite nustatyti, kurios grupės sumos didesnės: lyginių ar nelyginių. Laimi didesnė grupė.

Sukurkite funkciją, kuri paimtų sveikųjų skaičių sąrašą, atskirai suskaičiuotų lyginių ir nelyginių skaičių sumas,
 tada grąžintų lyginių ir nelyginių skaičių sumų skirtumą skaičių.
'''


def palyginti_lyg_ir_nelyg_sumas(numb: list) -> float:
    lyg_sum = 0
    nelyg_sum = 0
    for i in numb:
        if i % 2 == 0:
            lyg_sum += i
        else:
            nelyg_sum += i
    skirt = lyg_sum - nelyg_sum
    return skirt


numb = [2, 8, 7, 5]
skirt = palyginti_lyg_ir_nelyg_sumas(numb)
print(numb)
print(skirt)

'''
Jums duotas bigramų masyvas ir žodžių masyvas. Parašykite funkciją, kuri grąžintų True, jei iš šio masyvo galima rasti
kiekvieną bigramą bent vieną kartą žodžių masyve.
'''


def can_find(bigr: list, words: list) -> bool:
    all_words = ' '.join(words)
    for i in bigr:
        if i not in all_words:
            return False
    return True


bigr = ["at", "be", "th", "au"]
words = ["beautiful", "the", "hat"]
print(can_find(bigr, words))

'''
Sukurkite funkciją, kuri priima eilučių sąrašą ir grąžina naują sąrašą, kuriame yra tik tos eilutės, 
kurios prasideda balsiu. Naudokite lambda funkcijas, kad įgyvendintumėte logiką, tikrinančią, 
ar eilutė prasideda balsiu.
'''
line_list = ['Hello! Welcome to \n', 'This file is for testing purposes.\n', 'Good Luck!\n', 'I see']
vowelletters = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
good_list = []
for i in range(len(line_list)):
    for vowel in vowelletters:
        if vowel == line_list[i][0]:
            good_list.append(line_list[i])
print(good_list)
