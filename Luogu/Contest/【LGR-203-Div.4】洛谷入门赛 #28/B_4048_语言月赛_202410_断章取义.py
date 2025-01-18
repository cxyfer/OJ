T = int(input())
s = input()

# st = []
# cnt = 0
# for ch in s:
#     if ch == 't' and len(st) >= 2 and st[-1] == 'o' and st[-2] == 'n':
#         st.pop()
#         st.pop()
#         cnt += 1
#     else:
#         st.append(ch)

# print(''.join(st))
# print(cnt)

cnt = 0
while 'not' in s:
    s = s.replace('not', '')
    cnt += 1

print(s)
print(cnt)
