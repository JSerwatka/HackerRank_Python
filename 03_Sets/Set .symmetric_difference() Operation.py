_, en_set = input(), set(input().split())
_, fr_set = input(), set(input().split())

print(len(en_set.symmetric_difference(fr_set)))
#print(len(en_set ^ fr_set))
