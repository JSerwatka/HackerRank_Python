if __name__ == '__main__':
    N = int(input())
    array = []

    for _ in range(N):
        command = input().split()
        if command[0] == "print":
            print(array)
        else:
            eval("array.{0}{1}".format(command[0], tuple(map(int, command[1:]))))
