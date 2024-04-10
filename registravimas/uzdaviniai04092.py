"""
Sukurkite paprastą programą, kuri registruotų (logs) visus įvesties duomenis iš terminalo. Konfigūracijose turi
 būti rodomi visi papildomi duomenys (laikas, data, lygis ir t. t.).
"""
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.debug('This is Debug Message')
logging.info('This is an info message')

# def caltula (a:int, b:int):
#     return a + b
# logging.info('suskaiciavo')
#
# caltula(5,4)

"""
Parašykite funkciją, kuri perkeltų visus vieno tipo elementus į list galą
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
"""
def move_to_end(numbers:list, number: int):
    logging.info(f'ivestys{numbers} ir {number}')
    qnt = numbers.count(number)
    new_list1=[]
    new_list2=[]
    for c in range(0, qnt):
        new_list1.append(number)
    for i in numbers:
        if i != number:
            new_list2.append(i)
    new_list =  new_list2 + new_list1
    logging.info(f'rezultatas{new_list}')
    return new_list


new_list = move_to_end([1,2,4,1,6,9,1,0], 1)
print(new_list)

"""
Sukurkite 3 funkcijas, kurios yra susijusios viena su kita (viena iškviečiama kitoje), ir išbandykite visus
 logging sunkumo lygius pagal savo projektą.
"""

def suma(a, b)
    return(a + b)


def sand (x, function):
    return(x * function)

