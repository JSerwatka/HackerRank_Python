import numpy

# 1
'''
in_array = list(map(int, input().split()))
np_array = numpy.array(in_array)

print(numpy.reshape(np_array, (3, 3)))
'''

# 2
in_array = numpy.array(list(map(int, input().split())))
in_array.shape = (3, 3)

print(in_array)
