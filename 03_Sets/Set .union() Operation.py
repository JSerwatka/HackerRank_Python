_ = int(input())
en_set = set(input().split()) #mozna tez zmapowac na int, ale po co
_ = int(input())
fr_set = set(input().split())

print(len(en_set.union(fr_set)))
#print(len(en_set | fr_set))