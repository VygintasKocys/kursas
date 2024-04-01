"""
Sugeneruokite dict iš 10 skaitmenų (keys): 1,2,3...10. Kiekvienam key turėtų būti priskirta atsitiktinio sveikojo skaičiaus vertė nuo 1 iki 100.
"""
import random
my_dictio = {}

for i in range(1,11):
    my_dictio[i] = random.randint(1,100)
print(my_dictio)