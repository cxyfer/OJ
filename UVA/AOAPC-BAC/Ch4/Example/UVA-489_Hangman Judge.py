while True:
    round = int(input())
    if round == -1:
        break
    s = input()
    g = input()

    visited = [0] * 26 # 0: not in s, 1: in s, 2: in s and g
    cnt = 0
    wrong = 0
    for ch in s:
        idx = ord(ch) - ord('a')
        if not visited[idx]:
            cnt += 1
            visited[idx] = 1
    for ch in g:
        idx = ord(ch) - ord('a')
        if visited[idx] == 1:
            visited[idx] = 2
            cnt -= 1
            if cnt == 0:
                break
        elif visited[idx] == 0:
            wrong += 1
            visited[idx] = -1
            if wrong >= 7:
                break
    print('Round', round)
    if wrong >= 7:
        print('You lose.')
    elif cnt == 0:
        print('You win.')
    else:
        print('You chickened out.')
# while True:
#     round = int(input())
#     if round == -1:
#         break
#     s = input()
#     g = input()

#     st = set(s)
#     wrong = 0
#     for ch in g:
#         if ch in st:
#             st.remove(ch)
#             if not st:
#                 break
#         else:
#             wrong += 1
#             if wrong >= 7:
#                 break
#     print('Round', round)
#     if wrong >= 7:
#         print('You lose.')
#     elif not st:
#         print('You win.')
#     else:
#         print('You chickened out.')