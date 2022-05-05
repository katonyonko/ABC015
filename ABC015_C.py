import io
import sys

_INPUT = """\
6
3 4
1 3 5 17
2 4 2 3
1 3 2 9
5 3
89 62 15
44 36 17
4 24 24
25 98 99
66 33 57
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
    from itertools import product
    N,K=map(int,input().split())
    T=[list(map(int,input().split())) for _ in range(N)]
    ans='Nothing'
    for k in product(*[list(range(K)) for _ in range(N)]):
      tmp=0
      for i in range(N):
        tmp^=T[i][k[i]]
      if tmp==0: ans='Found'
    print(ans)