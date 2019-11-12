from collections import namedtuple

N, student_array, Student = int(input()), [], namedtuple('Student', input())

for i in range(N):
    student_array.append(Student(*input().split()))

print(sum(list(map(int, [student_array[x].MARKS for x in range(N)]))) / N)
