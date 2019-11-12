cube = lambda x: # complete the lambda function 

def fibonacci(n):
    fib_array = []
    a, b = 0, 1
    
    for i in range(n):
        fib_array.append(a)
        a, b = b, a+b
    
    return fib_array

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    