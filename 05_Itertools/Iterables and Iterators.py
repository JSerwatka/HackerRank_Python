from itertools import combinations

_ = int(input())
letter_list = list(input().split())
K = int(input())

tuples_list = list(combinations(letter_list, K))
correct_tuples_list = list([x for x in tuples_list if "a" in x])

print("{0:.3f}".format(len(correct_tuples_list)/len(tuples_list)))

'''moje pierwsze rozwiązanie

total_tuples = 0
correct_tuples = 0

for letter_tuple in combinations(letter_list, K):
    total_tuples += 1
    if 'a' in letter_tuple:
        correct_tuples += 1
print("{0:.3f}".format(correct_tuples/total_tuples))
'''
