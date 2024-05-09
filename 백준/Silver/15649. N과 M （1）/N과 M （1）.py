# 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열

n, m = map(int, input().split())

import itertools

n_list = list(range(1, n+1))

for i in itertools.permutations(n_list, m):
    my_str = ' '.join(map(str, i))
    print(my_str)
    