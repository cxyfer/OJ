"""
    假設初速度為0，否則算不出來
    從v-t圖可以得在t秒內的位移為v*t/2，而在2t秒內的位移為v*t*2
"""
while True:
    try:
        v, t = map(int, input().split())
    except EOFError:
        break
    print(v * t * 2)