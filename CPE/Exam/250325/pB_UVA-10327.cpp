/*
UVA-10327 Flip Sort
https://vjudge.net/problem/UVA-10327
僅透過交換相鄰元素來排序的次數為逆序對數量，可以用 Bubble Sort 的原理理解。
由於 N <= 1000，可以直接暴力法求解，時間複雜度為 O(N^2)。

進階作法是在 Merge Sort 的過程中維護逆序對數量，或使用 BIT 維護，時間複雜度為 O(N log N)。
注意雖然樣例都是 1~N 的排列，但題目沒有保證，因此用 BIT 的話需要先離散化。
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve(int N) {
    vector<int> A(N);
    for (auto &x : A) cin >> x;

    // int ans = 0;
    // for (int i = 0; i < N; i++)
    //     for (int j = i + 1; j < N; j++)
    //         if (A[i] > A[j]) ans++;

    // 離散化
    auto B = A;
    sort(B.begin(), B.end());
    B.erase(unique(B.begin(), B.end()), B.end());
    unordered_map<int, int> mp;
    for (int i = 0; i < B.size(); i++) mp[B[i]] = i + 1;
    for (auto &x : A) x = mp[x];

    // BIT
    vector<int> tree(N + 1);
    function<void(int, int)> update = [&](int k, int x) {
        while (k < N + 1) {
            tree[k] += x;
            k += (k & -k);
        }
    };
    function<int(int)> query = [&](int k) {
        int res = 0;
        while (k > 0) {
            res += tree[k];
            k -= (k & -k);
        }
        return res;
    };

    int ans = 0;
    for (int i = 0; i < N; i++) {
        ans += i - query(A[i]);
        update(A[i], 1);
    }

    cout << "Minimum exchange operations : " << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int N;
    while (cin >> N) solve(N);
    return 0;
}