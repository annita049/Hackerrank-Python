def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    j= size-1
    for i in range(size):
        ka = '-'.join(alpha[j+i:j:-1])
        kb = '-'.join(alpha[j:j+i+1])
        if(i==0): string = kb
        else: string = ka +'-'+ kb
        print(string.center(4*size-3,'-'))
        j-=1

    j= size-1
    for i in range(size-1):
        ka = '-'.join(alpha[i+j:i:-1])
        kb = '-'.join(alpha[i+2:i+j+1])
        string = ka +'-'+ kb
        print(string.center(4*size-3,'-'))
        j-=1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)