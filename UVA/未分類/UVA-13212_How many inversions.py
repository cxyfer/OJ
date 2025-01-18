while True:
    n = int(input().strip())
    if n == 0:
        break
    A = [int(input().strip()) for _ in range(n)]

    def merge_sort(left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        cnt = merge_sort(left, mid) + merge_sort(mid + 1, right)
        i, j = left, mid + 1
        tmp = []
        while i <= mid and j <= right:
            if A[i] <= A[j]:
                tmp.append(A[i])
                i += 1
            else:
                tmp.append(A[j])
                j += 1
                cnt += mid - i + 1
        while i <= mid:
            tmp.append(A[i])
            i += 1
        while j <= right:
            tmp.append(A[j])
            j += 1
        A[left:right + 1] = tmp
        return cnt

    print(merge_sort(0, n - 1))
