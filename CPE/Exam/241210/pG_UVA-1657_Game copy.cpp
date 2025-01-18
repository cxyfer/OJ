#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    int n, m;
    while (cin >> n >> m) {
        vector<pair<int, int>> v;
        map<int, int> Msum, Mprod;

        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                v.emplace_back(i, j);
                Msum[i + j]++;
                Mprod[i * j]++;
            }
        }

        vector<bool> ck(v.size(), false);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < v.size(); j++) {
                if (ck[j]) continue;

                int sum = v[j].first + v[j].second;
                int prod = v[j].first * v[j].second;

                if (i % 2 == 0) {
                    if (Msum[sum] <= 1) {
                        ck[j] = true;
                        Msum[sum]--;
                        Mprod[prod]--;
                    }
                } else {
                    if (Mprod[prod] <= 1) {
                        ck[j] = true;
                        Mprod[prod]--;
                        Msum[sum]--;
                    }
                }
            }
        }

        vector<pair<int, int>> ans;

        if (m % 2 == 0) {
            for (int i = 0; i < v.size(); i++) {
                if (ck[i]) continue;
                int sum = v[i].first + v[i].second;
                if (Msum[sum] == 1) {
                    ans.push_back(v[i]);
                }
            }
        } else {
            for (int i = 0; i < v.size(); i++) {
                if (ck[i]) continue;
                int prod = v[i].first * v[i].second;
                if (Mprod[prod] == 1) {
                    ans.push_back(v[i]);
                }
            }
        }

        cout << ans.size() << endl;
        for (auto &p : ans) {
            cout << p.first << " " << p.second << endl;
        }
    }

    return 0;
}
