"""
    Stack
"""
import sys
input = sys.stdin.readline
def print(val):
    sys.stdout.write(str(val) + '\n')

n = int(input())
st = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "Sleep":
        st.append(cmd[1])
    elif cmd[0] == "Kick":
        if st:
            st.pop()
    else:
        if st:
            print(st[-1])
        else:
            print("Not in a dream")