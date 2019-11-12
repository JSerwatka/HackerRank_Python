def wrapper(f):
    def fun(l):
        f("+91 {} {}".format(c[-10:-5], c[-5:]) for c in l)
    return fun

'''
        for i in l:
            if len(i) == 10:
                print("+91 %s %s" % (i[0:5], i[5:]))
            else:
                if i[0] == "0":
                    print("+91 %s %s" % (i[1:6], i[6:]))
                elif i[0:2] == "91":
                    print("+%s %s %s" % (i[0:2], i[2:7], i[7:]))
                else:
                    print("%s %s %s" % (i[0:3], i[3:8], i[8:]))'''

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
