if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # listU = [[i,j for i in range(3)] for j in range(3)]
    Biglist = []
    list = []


    ''''
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k==n: continue
                list.append([i,j,k])   # insert elements i,j,k as a list
    
    print(list)
    '''

    list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!= n]

    print(list)