def merge_the_tools(string, k):
    output_list = []
    n = len(string)
#    split_var = int(n / k)
    string_splited = [string[i:i+k] for i in range(0, n, k)]
    for u in string_splited:
        temp_list = []
        [temp_list.append(element) for element in u if element not in temp_list]
        output_list.append("".join(temp_list))

    print(*output_list, sep='\n')


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)