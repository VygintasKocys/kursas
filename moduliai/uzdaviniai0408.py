"""
Reikia parašyti funckiją, kuri turėtų du variable – vienas yra listas, kitas – iš kokio skaičiaus reikia
kad dalintusi. Reikia grazinti visus skaicius kurie dalinasi is duoto skaiciaus.
"""

# good_list=[]
# def dev_func(my_list: list, dev: int)-> list:
#     good_list = []
#     for i in my_list:
#         if i % dev == 0:
#             good_list.append(i)
#     return good_list
#
#
# print(dev_func([5,6,9,6],3))

"""
Parašyti funciją, į kurią padavus skaičių atspausdintų tokia tvarka kaip parodyta žemiau. Funkcija 
turi priimti 2 variable – nuo kurio iki kurio skaiciaus.: 
1 
22 
333 
4444 
55555 
Pvz jei nuo 3 iki 5, spausdina: 
333 

4444 

55555 
"""

# def skaiciai(a, b):
#     for i in range(a,b):
#         skaiciai1=[]
#         for j in range(1,i):
#             i=str(i)
#             skaiciai1.append(i)
#             skaiciai2 = "".join(skaiciai1)
#         print(skaiciai2)
#
# skaiciai(3, 6)

"""
Exercise 11: Write a Program to extract each digit from an integer in the reverse order. 

For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits. 
"""

# def apversti(a:int):
#     a = str(a)
#     apvert = []
#     for i in range(1,len(a)+1):
#         apvert.append(a[-i])
#     apv = "".join(apvert)
#     return apv
#
# a = 9876
# print(a, apversti(a))

"""
Print multiplication table from 1 to 10
"""

# for i in range(1,11):
#     date = []
#     for j in range(1,11):
#         date.append(str(j*i))
#     print(" ".join(date))

"""
Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk) 
* * * * *   
* * * *   
* * *   
* *   
* 
"""

# def eglute(a):
#     for i in range(a,0,-1):
#         print('*' * i)
#
# eglute(6)
