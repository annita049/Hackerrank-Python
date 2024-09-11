if __name__ == '__main__':

    student = {}
    n = int(input())
    for _ in range(n):
        name, *score = input().split()   # name, scores are two lists
        records = list(map(float,score))
        student[name] = records
    query = input()
    total = sum(student[query])
    print(f"{total/3:.2f}")


'''
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
'''
