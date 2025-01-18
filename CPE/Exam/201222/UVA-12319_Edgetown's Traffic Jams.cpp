#include <bits/stdc++.h>
using namespace std;
const int N = 105;
const int INF = 0x3f3f3f3f;
#define endl '\n'

void floyd_warshall(vector<vector<int>> &g) {
    int n = g.size();
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            if (g[i][k] == INF) continue;
            for (int j = 0; j < n; j++) {
                if (g[k][j] == INF) continue;
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, u, v, A, B;
    string line;
    while (cin >> n && n) {
        vector<vector<int>> g1(n, vector<int>(n, INF));
        vector<vector<int>> g2(n, vector<int>(n, INF));
        for (int i = 0; i < n; i++) g1[i][i] = 0, g2[i][i] = 0;
        cin.ignore();

        for (int i = 0; i < n; i++) {
            getline(cin, line);
            stringstream ss(line);
            ss >> u;
            u--;
            while (ss >> v) {
                v--;
                g1[u][v] = 1;
            }
        }

        for (int i = 0; i < n; i++) {
            getline(cin, line);
            stringstream ss(line);
            ss >> u;
            u--;
            while (ss >> v) {
                v--;
                g2[u][v] = 1;
            }
        }

        cin >> A >> B;

        floyd_warshall(g1);
        floyd_warshall(g2);

        bool flag = true;
        for (int i = 0; i < n && flag; i++) {
            for (int j = 0; j < n && flag; j++) {
                if (g2[i][j] > g1[i][j] * A + B) {
                    flag = false;
                }
            }
        }
        cout << (flag ? "Yes" : "No") << endl;
    }
    return 0;
}