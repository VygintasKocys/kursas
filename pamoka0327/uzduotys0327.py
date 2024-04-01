# [‚namas‘, ‚namelis‘, ‚nameliukas‘] -> „nam“
"""
Yra duotas listas, jame yra žodžiai. Parašyti algortimą, kuris atrinktų patį ilgiausią besikartojančių žodžių fragmenta. Pvz, jei listas:

[‚namas‘, ‚namelis‘, ‚nameliukas‘] -> „nam“

[morkytė, molas, morka] - > mo

[namas, balkonas, mama] - > „“ tuscias stringas.
"""

a = ['namas', 'namelis', 'nameliukas']
a1, a2, a3 = a
b = []
for i in range(10):
    if a1[i] == a2[i] == a3[i]:
        b.append(a1[i])
    else:
        break
c=''.join(b)
print(c)