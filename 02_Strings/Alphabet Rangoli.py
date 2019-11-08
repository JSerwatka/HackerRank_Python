def print_rangoli(size):
    string = ""
    line_size = size + (size-1) * 3
    line_array = []

    for i in range(size-1, -1, -1):
        if i == (size-1):
            string += chr(ord('a') + i)
        else:
            string += "-" + chr(ord('a') + i)
        line_array.append(string + string[-2::-1])
        print((line_array[size-i-1]).center(line_size, '-'))

    print(*[line_array[i].center(line_size, '-') for i in range(size-2, -1, -1)], sep='\n')


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)