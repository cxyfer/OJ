#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<string> tasks(m);
    for (auto &task : tasks) cin >> task;
    for (int i = 0; i < n; ++i) {
        string name, s, t;
        cin >> name;
        for (int j = 0; j < m; ++j) {
            cin >> s;
            t = name + ".zip/" + name + "/" + tasks[j] + "/" + tasks[j] + ".cpp";
            cout << (s == t ? "Fusu is happy!" : "Fusu is angry!") << endl;
        }
    }
    return 0;
}