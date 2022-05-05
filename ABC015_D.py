import io
import sys

_INPUT = """\
6
10
3 2
4 20
3 40
6 100
10
5 4
9 10
3 7
3 1
2 6
4 5
22
5 3
5 40
8 50
3 60
4 70
6 80
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from copy import deepcopy
  W=int(input())
  N,K=map(int,input().split())
  S=[list(map(int,input().split())) for _ in range(N)]
  dp=[[0]*(K+1) for j in range(W+1)]
  for i in range(N):
    for j in reversed(range(W+1)):
      for k in reversed(range(K)):
        if j<W+1-S[i][0]:
          dp[j+S[i][0]][k+1]=max(dp[j+S[i][0]][k+1],dp[j][k]+S[i][1])
    
  print(dp[-1][-1])