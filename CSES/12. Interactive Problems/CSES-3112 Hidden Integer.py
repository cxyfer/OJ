"""

"""
def query(y: int) -> bool:
    print(f'? {y}', flush=True)
    return input() == "YES"

def answer(x: int) -> None:
    print(f'! {x}', flush=True)
    return

def solve():
    left, right = 1, int(1e9)
    while left <= right:
        mid = (left + right) // 2
        if query(mid):
            left = mid + 1
        else:
            right = mid - 1
    answer(left)

if __name__ == "__main__":
    solve()