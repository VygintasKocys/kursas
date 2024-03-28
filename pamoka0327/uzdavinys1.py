'''
Sukurkite kintamuosius, kuriuose reprezentuotų vartotojo vardą ir slaptažodį. Pradėkite begalinį ciklą, leidžiantį įvesti vartotojo vardą ir slaptažodį. Jei duomenys teisingi, sustabdykite begalinį ciklą ir išspausdinkite pasisveikinimo pranešimą
'''
name = "Vygis"
password = "Kocys"
while True:
    user_input = input("Enter name: ")
    user_input2= input("Enter password: ")
    if name == user_input and password == user_input2:
        print("teisingas atsakymas")
        break
