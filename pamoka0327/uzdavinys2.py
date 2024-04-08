"""
Leiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.
"""
suma = 0
vidurkis = 0
skaiciai = []
for i in range(10):
    skaicius=int(input('iveskite skaiciu'))
    skaiciai.append(skaicius)
    print(skaiciai)
suma=sum(skaiciai)
print(suma)
vidurkis