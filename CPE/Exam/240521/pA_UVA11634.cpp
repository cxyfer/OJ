#include <bits/stdc++.h>
using namespace std;
const int N = 10000;
#define endl '\n'

bool visited[N];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    while (cin >> n && n) {
        int ans = 0;
        memset(visited, false, sizeof(visited));
        while (!visited[n]) {
            ans++;
            visited[n] = true;
            n = (n * n) / 100 % 10000;
        }
        cout << ans << endl;
    }
    return 0;
}