import numpy

n, m = map(int, input().split())

a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(numpy.add(a, b), numpy.subtract(a, b), numpy.multiply(a, b), numpy.floor_divide(a, b), numpy.mod(a, b), numpy.power(a, b), sep='\n')
