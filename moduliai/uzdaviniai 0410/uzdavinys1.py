"""Exercise 1:	Write a Python program to find the most common elements and their counts in a specified text.
Original string: lkseropewdssafsdfafkpwe
Most common three characters of the said string:
[('s', 4), ('e', 3), ('f', 3)]

"""

a="lkseropewdssafsdfafkpwe"
good_list=[]
raides = []
dazniausias1=0
dazniausias2=0

for i in a:
    b=a.count(i)
    if b > dazniausias1-1:
        dazniausias1 +=1
    if i not in raides:
        raides.append(i)
        good_list.append((i,b))
print(good_list)

"""
Exercise 2: Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
"""
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

def pirmas_list(pirmas, antras):
    return pirmas[1::2] + antras[::2]

"""

Exercise 3: Create a Python set such that it shows the element from both lists in a pair
Given:

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
Expected Output:

Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)
"""

def pair(first_list:list, second_list:list)->set:
    return set(zip(first_list, second_list))

"""
Exercise 5: Get all values from the dictionary and add them to a list but don’t add duplicates
Given:
 

Expected Outcome:
 
[47, 52, 44, 53, 54]
"""
def get_values(speed:dict)->list:
    good_list=[]
    for i in speed.values():
        if i not in good_list:
            good_list.append(i)
    return (good_list)

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
s=get_values(speed)
print(s)

