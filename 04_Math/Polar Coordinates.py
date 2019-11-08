import cmath

z = complex(input())

#print("%f\n%f" % (abs(z), cmath.phase(z)))
#print("{}\n{}".format(abs(z), cmath.phase(z)))
print(abs(z), cmath.phase(z), sep='\n')
