if __name__ == '__main__':
    grades = []

    def find_second_smallest(sorted_array):
        smallest_score = sorted_array[0][1]
        for _, score in sorted_array:
            if score > smallest_score:
                return score

    
    for i in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])

    grades.sort(key = lambda x: x[1])
    second_best_score = find_second_smallest(grades) 
    winners = [x[0] for x in grades if x[1] == second_best_score]
    winners.sort(key = lambda x: x[0])

    print(*winners, sep='\n')
