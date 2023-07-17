from random import choices
from typing import Set

count = int(input())
list_nums = choices(range(1, count * 2), k=count)

print(list_nums)

res_list = set()
for i in list_nums:
    if list_nums.count(i) > 1:
        res_list.add(i)

print(res_list)