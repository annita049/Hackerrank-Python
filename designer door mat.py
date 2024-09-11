if __name__ == '__main__':
    n, m = map(int,input().split())
    s = ".|."

    for i in range(n//2):
        print(((2*i+1)*s).center(m,'-'))

    print("WELCOME".center(m,'-'))

    for i in range(n//2):
        print(((2*(n//2-i)-1)*s).center(m,'-'))

'''


    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

            '''

