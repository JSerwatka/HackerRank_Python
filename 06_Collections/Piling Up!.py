from collections import deque

def can_be_piled(numbers):
    queue = deque(numbers)
    curr_cube = queue.popleft() if queue[0] >= queue[-1] else queue.pop()

    while len(queue) > 0:
        if queue[0] >= queue[-1] and curr_cube >= queue[0]:
            curr_cube = queue.popleft()
        elif queue[0] < queue[-1]  and curr_cube >= queue[-1]:
            curr_cube = queue.pop()
        else:
            return False
    return True

for _ in range(int(input())):
    _ = input()
    numbers = map(int, input().split())
    
    print("Yes" if can_be_piled(numbers) else "No")