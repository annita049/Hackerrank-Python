if __name__ == '__main__':
    lis = []
    N = int(input())

    for _ in range(N):
        cmd, *t = input().split()
        y = list(map(int, t))

        if cmd =="insert":
            lis.insert(y[0],y[1])
        elif cmd == "append":
            lis.append(y[0])
        elif cmd == "remove":
            lis.remove(y[0])
        elif cmd == "pop":
            lis.pop()
        elif cmd == "sort":
            lis.sort()                                     
        elif cmd == "reverse":
            lis.reverse()
        else:
            print(lis)


'''
insert 0 5
print
append 9
append 17
sort
insert 2 6
pop
remove 6
reverse
print
pop
'''