import numpy

''' poprawna wersja, ale jest blad w odpowiedzi

n, m = map(int, input().split())

#print(numpy.eye(n, m, k = 0))
'''
n, m = map(int, input().split())

print(str(numpy.eye(n, m)).replace('1',' 1').replace('0',' 0'))
