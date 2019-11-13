import numpy

n, m = map(int, input().split())
my_array = numpy.zeros((n, m), dtype = int)
        
for i in range(n):
    split_list = list(map(int, input().split()))
    for j in range(m):  
        my_array[i][j] = split_list[j]

print(numpy.max(numpy.min(my_array, axis = 1)))
