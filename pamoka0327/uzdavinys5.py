no_array = input('iveskite skaiciu seka, skaicius atskirti tarpu:')
no_array1 = no_array.split()
listas=[]
for i in no_array1:
    listas.append(int(i))
print(listas)
print(f'vidurkis{sum(listas)/len(listas)}')



