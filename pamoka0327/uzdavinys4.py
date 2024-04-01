'''
Sukurkite PIN kodo nulaužimo programą. Tarkime, PIN kodą sudaro 4 atsitiktiniai skaitmenys. Reikšmę galite saugoti kintamajame. Tada sukurkite ciklą, einantį per visas galimas kombinacijas, kol rasite tą, kurią įvedėte.
'''

pinas = '0983'
for i in range(1,9999):
    i=str(i)
    i=i.zfill(4)
    if i == pinas:
        print(f'pinas {i}')

