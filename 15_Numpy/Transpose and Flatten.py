import numpy

n, _ = map(int, input().split())

array = numpy.array([input().split() for _ in range(n)], int)

print(numpy.transpose(array), array.flatten(), sep='\n')