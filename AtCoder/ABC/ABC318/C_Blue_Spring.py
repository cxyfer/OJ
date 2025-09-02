N, D, P = map(int, input().split(" "))
costs = list(map(int, input().split(" ")))

max_pass = N//D # 最多可以買幾張月票

costs.sort(reverse=True)
S = sum(costs)
ans = S
pre = 0
# print(max_pass)
for i in range(max_pass+1):
    # print(costs[i*D:(i+1)*D])
    pre += sum(costs[i*D:(i+1)*D])
    ans = min(ans, S-pre+(i+1)*P)
    # print(ans, i, pre)
print(ans)
exit()


pass_cost = P/D
count = D

ans = 0
buy_cost = 0 # 保存可以買的成本
buy_days = 0 # 保存可以買的天數

for i, cost in enumerate(costs):
    if cost > pass_cost:
        buy_days += 1
        if buy_days == D: # 月票可以被用完，買一張月票
            ans += buy_cost
            buy_cost = 0
            buy_days = 0
        else:
            buy_cost += cost
            buy_days += 1
    else:
        ans += cost
    print(ans, buy_cost, buy_days)

print(ans)
if buy_days != 0:
    ans += max(P, buy_cost)
print(ans)