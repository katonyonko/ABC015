import io
import sys

_INPUT = """\
6
isuruu
isleapyear
ttttiiiimmmmeeee
time
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A=input()
  B=input()
  if len(A)>len(B): print(A)
  else: print(B)