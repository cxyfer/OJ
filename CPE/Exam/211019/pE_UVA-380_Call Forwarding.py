from collections import defaultdict
from bisect import bisect_right

t = int(input())
print(f"CALL FORWARDING OUTPUT")
for kase in range(1, t + 1):
    print(f"SYSTEM {kase}")
    # Add rules
    rules = defaultdict(list)
    while True:
        line = input().strip()
        if line == "0000":
            break
        src, st, d, target = map(int, line.split())
        rules[src].append((st, d, target))
    # Forward calls
    visited = set()
    def forward(at_time, src):
        if not rules[src]:
            return src
        if src in visited:
            return 9999
        visited.add(src)
        # 好像沒必要用二分搜尋
        for st, d, target in rules[src]:
            if st <= at_time <= st + d:
                return forward(at_time, target)
        # idx = bisect_right(rules[src], (at_time, float("inf"), float("inf"))) - 1
        # st, d, target = rules[src][idx]
        # if st <= at_time <= st + d:
        #     return forward(at_time, target)
        return src
    # Process calls
    while True:
        line = input().strip()
        if line == "9000":
            break
        call_time, src = map(int, line.split())
        visited.clear()
        print(f"AT {call_time:04d} CALL TO {src:04d} RINGS {forward(call_time, src):04d}")
print(f"END OF OUTPUT")