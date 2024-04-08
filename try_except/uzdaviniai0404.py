"""
Sukurkite bent 5 skirtingas funkcijas ir pabandykite apdoroti bent 5 integruotas "Python" išimtis
"""


def devide(x: int, y: int) -> float:
    try:
        z = x / y
        print(z)
        return z
    except ZeroDivisionError:
        print("devision by zero")


c = devide(6, 0)
print(c)

lambda_sum = lambda x, y: x + y
lambda_mult = lambda x, y: x * y
lambda_min = lambda x, y: x - y
lambda_div = lambda x, y: x / y


def count_numbers(a: int, b: int, function):
    try:
        return function(a, b)
    except TypeError:
        print('wrong type')
    except NameError:
        print('wrong name')
    except SyntaxError:
        print('wrong syntax')


print(count_numbers((2, 5), 7, lambda_sum))


def count_numbers1(a: int, b: int, function):
    try:
        print(x)
        return function(a, b)
    except NameError:
        print('wrong name')


print(count_numbers1(4, 8, lambda_min))


def count_numbers2(d):
    try:
        a = int(input('ivesti skaiciu a'))
        b = int(input('ivesti skaiciu b'))
        c = a - b + d
        print(c)
    except ValueError:
        print('wrong value')


count_numbers2(9)

"""
Python kalboje, dalijant iš nulio, gauname ZeroDivisionError. Jūsų užduotis - sukurti funkciją, kuri:

Kaip argumentus priima du skaičius.

Mėgina padalyti pirmąjį skaičių iš antrojo.

Jei antrasis skaičius yra nulis, ji turėtų sugauti ZeroDivisionError ir grąžinti pasirinktinį klaidos pranešimą.

Jei dalijimas sėkmingas, turėtų būti grąžinamas rezultatas.

Nepriklausomai nuo to, ar dalijimas pavyko, ar ne, turėtų būti išspausdintas pranešimas "Attempted division". 
Jei įvesties duomenys nėra skaičiai, pateikiamas TypeError pranešimas. Funkcija pagauna šią TypeError ir
grąžina pasirinktinį klaidos pranešimą.
"""


def two_numbers_devision():
    try:
        a = int(input('Iveskite pirma skaiciu '))
        b = int(input('Iveskite antra skaiciu '))
        return a / b

    except ZeroDivisionError:
        print("division by zero")
    except ValueError:
        print('ivesti ne skaiciai')
    finally:
        print("Attempted devision")


print(two_numbers_devision())

"""
Sukurkite mini "Python" programą, kuri įvestų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą. 
Tvarkykite visas galimas klaidas.
"""


def calc(function):
    try:
        x = int(input('Iveskite pirma skaiciu x '))
        if not type(x) is int:
            raise ValueError("Galima ivesti tik skaicius")
        y = int(input('Iveskite anta skaiciu y '))
        return function(x, y)
    except ZeroDivisionError:
        print("Dalyba is nulio negalima")
    except ValueError:
        print('Neteisingai ivestas skaicius')
    except NameError:
        print('Neteisingas junkcijos pavadinimas')
    finally:
        print('Atlikti skaiciavimai')


print(f'x / y = {calc(lambda_div)}')
print(f'x + y = {calc(lambda_sum)}')
print(f'x -y = {calc(lambda_min)}')
print(f'x * y = {calc(lambda_mult)}')
