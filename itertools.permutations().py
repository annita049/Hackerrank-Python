import itertools as it

line = input().split()
string = line[0]
n = int(line[1])


string = ''.join(sorted(string))
ans = it.permutations(string, n)

for x in ans:
    print(''.join(x))


# hackerrank
# aacehkknrr)
# aa, ac, ae, ah, ak, ak, ...