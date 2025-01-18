#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, q, a, b;
    cin >> n >> q;
    vector<int> A(n), pos(n + 1);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
        pos[A[i]] = i;
    }

    int ans = 1;
    for (int x = 2; x <= n; x++) {
        if (pos[x - 1] > pos[x]) ans++;
    }

    while (q--) {
        cin >> a >> b;
        a--, b--;

        int x = A[a], y = A[b];
        if (x > y) swap(x, y);

        if (x - 1 > 0 && pos[x - 1] > pos[x]) ans--;
        if (x + 1 <= n && pos[x] > pos[x + 1]) ans--;
        if (y - 1 > 0 && y != x + 1 && pos[y - 1] > pos[y]) ans--;
        if (y + 1 <= n && pos[y] > pos[y + 1]) ans--;

        swap(A[a], A[b]);
        swap(pos[A[a]], pos[A[b]]);

        if (x - 1 > 0 && pos[x - 1] > pos[x]) ans++;
        if (x + 1 <= n && pos[x] > pos[x + 1]) ans++;
        if (y - 1 > 0 && y != x + 1 && pos[y - 1] > pos[y]) ans++;
        if (y + 1 <= n && pos[y] > pos[y + 1]) ans++;

        cout << ans << endl;
    }
    return 0;
}