"""
    tags: CPE49
    absolute value
"""
while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    print(b - a if a < b else a - b)