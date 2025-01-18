buffer = []
def cin():
    global buffer
    if len(buffer) == 0:
        buffer = input().split()
    res = buffer[0]
    buffer = buffer[1:]
    return res

t = int(input())

while True:
    try:
        n = int(input())
    except EOFError:
        break
