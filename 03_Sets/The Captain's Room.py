'''
K = int(input())
rooms_list = list(map(int, input().split()))
rooms_set = set(rooms_list)
'''

'''moje - za duzo obliczen, timout przy duzej liczbie danych
def captain_room(K, rooms_list, rooms_set):
    for _ in range(K):
        for element in rooms_set:
            try:
                rooms_list.remove(element)
            except ValueError:
                return(element)

print(captain_room(K, rooms_list, rooms_set))
'''

''' krotsze rozwiazanie, ale dalej duzo obliczen
print(((sum(rooms_set) * K) - sum(rooms_list)) // (K - 1))
'''
#najlepsze - najszybsze
nom = int(input())
members = list(map(int, input().split()))
rooms = set()   # Contains all the rooms.
room_more_mem = set()   # Contains only the rooms with families.

for m in members:
    if m not in rooms:
        rooms.add(m)
    else:
        room_more_mem.add(m)

print(rooms.difference(room_more_mem).pop())