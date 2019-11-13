import numpy

n, m = map(int, input().split())

my_array = numpy.zeros((n, m), dtype = int)

for i in range(n):
    split_array = list(map(int, input().split()))
    for j in range(m):
        my_array[i][j] = split_array[j]

print(numpy.prod(numpy.sum(my_array, axis = 0))) 
