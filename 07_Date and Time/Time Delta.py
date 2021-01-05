import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_obj = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2_obj = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    time_difference = abs((t1_obj - t2_obj).total_seconds())

    return f"{time_difference:.0f}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
