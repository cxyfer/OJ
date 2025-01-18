from bisect import bisect_left

m, n = map(int, input().split())

schools = list(map(int, input().split()))
students = list(map(int, input().split()))
schools.sort()

ans = 0
for student in students:
    idx = bisect_left(schools, student)

    if idx == 0:
        ans += schools[0] - student
    elif idx == m:
        ans += student - schools[-1]
    else:
        ans += min(schools[idx] - student, student - schools[idx - 1])
print(ans)
