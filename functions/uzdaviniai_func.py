"""
Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.
"""

'''
Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.
'''


def add_string(values: list, end_string: str = 'string') -> list:
    return [f'{i}{end_string}' for i in values]


values = ['per', 3, "jj"]
end_string = "sting"
a = add_string(values, end_string)
print(a)

"""
Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą
"""


def add_min_dev_mult(value1: int, value2: int) -> tuple:
    return (value1 + value2, value1 - value2, value1 / value2, value1 * value2)


value1 = 8
value2 = 3
b = add_min_dev_mult(value1, value2)
print(f'suma {b[0]}, skirtumas {b[1]}, dalyba {b[2]}, sandauga {b[3]}')

'''
Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.
'''


def words_with_unique_simb(sentence: str,) -> list:
    words = sentence.split()
    good_words = []
    for word in words:
        for letter in word:
            if word.count(letter) > 1:
                break
        else:
            good_words.append(word)
    return good_words


sentence = 'gg jjfda asdt wdst'
a = words_with_unique_simb(sentence)
print(a)

'''
Parašykite programą, apibrėžiančią funkciją extract_email_addresses(), kuri priima tekstą kaip įvestį 
ir iš teksto ištraukia visus el. pašto adresus.
'''


def extract_email_addresses(my_text: str) -> list:
    my_text = my_text.split()
    return [word for word in my_text if '@' in word and '.' in word]


my_text = 'as noriu issiusti laiskus siems adresams vygis@danbalt.lt ir vygis.kocys@gmail.com'
print(extract_email_addresses(my_text))
