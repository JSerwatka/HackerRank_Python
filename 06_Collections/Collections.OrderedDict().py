from collections import OrderedDict

N = int(input())
ordered_dictionary = OrderedDict()


for _ in range(N):
    items_array = list(input().split())
    if " ".join(items_array[:-1]) in ordered_dictionary:
        ordered_dictionary[" ".join(items_array[:-1])] += int(items_array[-1])
    else:
       ordered_dictionary[" ".join(items_array[:-1])] = int(items_array[-1])

for key, values in ordered_dictionary.items():
    print(key, values)
    