T = int(input())
bool_array = []

for _ in range(T):
    _ = int(input())
    A_elements = list(map(int, input().split()))
    _ = int(input())
    B_elements = list(map(int, input().split()))
    
    bool_array.append(all(item in B_elements for item in A_elements))

print(*bool_array, sep='\n')