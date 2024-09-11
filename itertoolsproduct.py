import itertools as it


A = map(int, input().split())
B = map (int, input().split())

cartesian_product = it.product(sorted(A),sorted(B))

for items in cartesian_product:
    print(items, end=' ')