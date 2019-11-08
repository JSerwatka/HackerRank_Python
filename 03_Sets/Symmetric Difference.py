m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

print(*sorted(m_set ^ n_set), sep='\n')