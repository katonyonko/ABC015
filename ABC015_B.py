import io
import sys

_INPUT = """\
6
4
0 1 3 8
5
1 4 9 10 15
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  print((sum(A)-1)//(N-A.count(0))+1)