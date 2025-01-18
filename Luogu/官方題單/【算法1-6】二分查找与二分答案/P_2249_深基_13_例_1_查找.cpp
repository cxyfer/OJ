#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    while (m--) {
        int q;
        cin >> q;
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (A[mid] < q) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        cout << (left < n && A[left] == q ? left + 1 : -1) << " ";
    }
    return 0;
}