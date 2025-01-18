from math import gcd

n = int(input())

courses = []
for _ in range(n):
    _p = int(input())
    _id = sorted(list(map(int, input().split())))
    _sc = list(map(int, input().split()))
    _w = list(map(int, input().split()))

    courses.append((_p, _id, _sc, _w))

student_id = int(input())

tot = cnt = 0
for p, id, sc, w in courses:
    if student_id not in id:
        continue
    stu_sc = sc[id.index(student_id)]
    rk = sorted(sc, reverse=True).index(stu_sc)
    tot += w[rk]
    cnt += 1

if tot % cnt == 0:
    print(tot // cnt)
else:
    q, r = divmod(tot, cnt)
    g = gcd(r, cnt)
    print(f'{q}+{r // g}/{cnt // g}')