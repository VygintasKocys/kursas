import math
"""
 Parasyti funckija, kuri priimtu du vairabe – lista kartotini. Grazinti turi lista, kuriame buvo listai su
 kartotiniu nariu skaiciumis. Pvz.
Data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Kartotinis = 3
Grazina [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
def return_slice(numbers: list, number: int):
    value = math.ceil(len(numbers)/number)
    result = []
    for i in range(value):
        first_index, second_index = i * number, i * number + number
        result.append(numbers[first_index:second_index])
    print(result)

return_slice([1,2,3,4,5,6,7,8,9,10],4)








# data={1:'vienas', d2:'du', 3:'trys', 4:'keturi'}
# needed_keys = [1,2]
# deleting_keys = [3]
#
# result_n ={}
#
# def calculate_dic(data:dict, needed_key:list, deleting_key):
#     for key in data:
#     if key in needed_keys:
#         result_n[key] = data[needed_key]
#         if key in deleting_key:
#             del new_data[key]
#
#     return result_n, new_data