"""
Sukurkite Calculator klasę su pagrindinėmis funkcijomis: sudėti, dalyti, dauginti, atimti ir t. t.. Inicijuokite
klasę ir parodykite keletą skaičiavimų

"""
print('1 uzdavinys')


class Calculator:
    def __init__(self, number1: int, number2: int):
        self.number1 = number1
        self.number2 = number2

    def suma(self):
        return f'{self.number1} + {self.number2} = {self.number1 + self.number2}'

    def skirtumas(self):
        return f'{self.number1} - {self.number2} = {self.number1 - self.number2}'


a = 9
b = 7
calculator = Calculator(a, b)
print(calculator.suma())
print(calculator.skirtumas())

"""
Darbuotojo klasėje sukurkite egzempliorių atributus fullname (vardas, pavardė) ir email (el. paštas). 
Turint asmens vardą ir pavardę:
Vardą ir pavardę suformuokite paprasčiausiai sujungdami vardą ir pavardę, atskiriamus tarpeliu.
Elektroninį paštą suformuokite sujungdami vardą ir pavardę, tarp jų įterpdami simbolį . 
Pabaigoje įrašydami @company.com. Įsitikinkite, kad visas el. laiškas būtų** rašomas mažosiomis raidėmis**.
"""
print('2 uzdavinys')


class Emploee:
    def __init__(self, name, lname):
        self.name = name
        self.lname = lname

    def fullname(self):
        return f'{self.name} {self.lname}'

    def email(self):
        return f'{self.name}.{self.lname}@company.com'


emploee = Emploee("Jonas", "Petraitis")

print(emploee.fullname())
print(emploee.email().lower())

"""
Sukurkite knygos klasę Book, kuri turi du atributus:
name
author
ir du metodus:
Metodas, pavadintas .get_title(), kuris grąžina: "Pavadinimas: " + egzemplioriaus pavadinimas.
Metodas .get_autor(), kuris grąžina: "Autorius: " + egzempliorius autorius.
ir instancuokite šią klasę sukurdami 3 naujas knygas:

- Pride and Prejudice - Jane Austen (PP)
- Hamletas - Viljamas Šekspyras (H)
- Karas ir taika - Levas Tolstojus (WP)
Naujų egzempliorių pavadinimai turėtų būti atitinkamai PP, H ir WP. Pavyzdžiui, jei, naudodamas šią knygų klasę, 
instancuočiau šią knygą:


- Haris Poteris - J. K. Rowling (HP)
"""
print('3 uzdavinys')


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def get_title(self):
        return f"Pavadinimas: {self.name}"

    def get_autor(self):
        return f"Autorius: {self.author}"

    def sarasas(self):
        print(f'{self.name} \n{self.author} \n{self.get_title()} \n{self.get_title()}')


PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamletas", "Viljamas Sekspyras")
WP = Book("Karas ir taika", "Levas Tolstojus")
PP.sarasas()

"""
Apie šalį galima sakyti, kad ji yra didelė, jei ji yra:
Didelė gyventojų skaičiumi.
Didelė pagal plotą.
Šalies klasę papildykite taip, kad joje būtų atributas is_big. Nustatykite jį į True, jei tenkinamas kuris nors 
iš šių kriterijų:
Gyventojų skaičius yra didesnis nei 20 mln.
Plotas didesnis nei 3 mln. km².
Taip pat sukurkite metodą, kuris palygintų šalies gyventojų tankį su kitos šalies objektu. Grąžinkite 
tokio formato eilutę:

{country} has a {smaller / larger} population density than {other_country}
"""
print('4 uzdavinys')


class Country:
    def __init__(self, name, inhabitants, area):
        self.name = name
        self.inhabitants = inhabitants
        self.area = area
        if self.inhabitants > 2000000 or self.area > 3000000:
            self.is_big = True
        else:
            self.is_big = False
        self.dencity = inhabitants / area

    def compare_pd(self, country):
        if country.dencity > self.dencity:
            a = 'larger'
        else:
            a = 'smaller'
        return f'{country.name} has a {a} population density than {self.name}'


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big)
print(andorra.is_big)

print(andorra.compare_pd(australia))
print(f'Australija {australia.dencity}')
print(f'Andora {andorra.dencity}')







