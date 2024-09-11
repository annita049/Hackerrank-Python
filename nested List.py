if __name__ == '__main__':
    student = []
    score = []
    for _ in range(int(input())):
        name = input()
        sc = float(input())
        score.append(sc)
        student.append([name,sc])

    score = sorted(set(score))
    second_lowest = score[1]
    
    target_students = [st[0] for st in student if st[1]== second_lowest]


    for x in target_students:
        print(x)

'''
4
kona
80.6
ador
77.8
apu
80.6
ruby
92.3
'''
