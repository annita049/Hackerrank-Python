if __name__ == '__main__':  

    N = int(input())
    x = tuple (map(int, input().split()))
    print(hash(x))