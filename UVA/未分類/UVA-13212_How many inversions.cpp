#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

LL merge_sort(vector<int>& A, int left, int right) {
    if (left >= right) {
        return 0;
    }

    // 遞迴分割陣列
    int mid = (left + right) / 2;
    LL cnt = merge_sort(A, left, mid) + merge_sort(A, mid + 1, right);

    // 合併兩個已排序的子陣列
    int i = left, j = mid + 1;
    vector<int> tmp;
    while (i <= mid && j <= right) {
        if (A[i] <= A[j]) {
            tmp.push_back(A[i++]);
        } else {
            tmp.push_back(A[j++]);
            cnt += mid - i + 1; // 此時 (A[i], A[j]), (A[i+1], A[j]), ..., (A[mid], A[j]) 都是逆序對
        }
    }
    while (i <= mid)
        tmp.push_back(A[i++]);
    while (j <= right)
        tmp.push_back(A[j++]);
    
    // 將 tmp 的值複製回 A
    for (int i = left; i <= right; ++i)
        A[i] = tmp[i - left];
    return cnt;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    while (cin >> n && n) {
        vector<int> A(n);
        for (int i = 0; i < n; ++i) {
            cin >> A[i];
        }
        cout << merge_sort(A, 0, n - 1) << endl;
    }
    return 0;
}