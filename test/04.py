# def sortList(list):
#     sortedList = []
#     while True:
#         if list:
#             for num in list:
#                 if num == max(list):
#                     sortedList.append(num)
#                     list.remove(num)

#         else:
#             return sortedList
                
# print(sortList([3, 6, 2, 7, 9, 1]))

def sortList(list):
    resultList = []
    while list:
        num = max(list)
        resultList.append(num)
        list.remove(num)
    
    return resultList

print(sortList([3, 6, 2, 7, 9, 1]))