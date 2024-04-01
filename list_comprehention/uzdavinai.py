import math

"""
Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6
"""


print('1 uzduotis')


def numbers_div_by_six(numbers):
    return [number for number in numbers if not number % 6]


a = list(range(1, 1001))
print(numbers_div_by_six(a))

'''
Raskite visus skaičius iš 1-1000, kuriuose yra 9.
'''


print('2 uzduotis')

numbers_with_9 = []
for num in range(1, 1001):
    num = str(num)
    if "9" in num:
        numbers_with_9.append(num)
print(numbers_with_9)

'''
Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e
'''

print('3 uzduotis')


def words_with_e(words):
    return [word for word in words if "e" in word]


e = ('Petras', 'Jonas', 'Antanas', 'Jane')
print(words_with_e(e))

'''
Naudodami tą patį string, kaip ir ankstesniame pratime: apskaičiuokite raidžių, kurios turi daugiau 
nei 5 simbolius, skaičių.
'''

print('4 uzduotis')


def words_more_5_simbols(words):
    return [word for word in words if len(word) > 5]


print(words_more_5_simbols(e))
print(len(words_more_5_simbols(e)))

'''
Parašykite programą, kuri patikrintų, ar duotas skaičius yra tobulasis kvadratas
'''

print('5 uzduotis')


numbe = int(input('ivesti sveika skaiciu:'))
root = int(math.sqrt(numbe))
if root*root == numbe:
    print(f'skaicius {numbe} yra tobulasis kvadratas')
else:
    print(f'skaicius {numbe} nera tobulasis kvadratas')
