#include <bits/stdc++.h>
using namespace std;
const int N = 105;
#define endl '\n'

char mp[N][N], tmp[N][N];

int main() {
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
	int t, r, c, n;
	cin >> t;
	int DIR[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
	while (t--) {
		cin >> r >> c >> n;
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				cin >> mp[i][j];
			}
		}
		while (n--) { // each day
			for (int i = 0; i < r; ++i) { // copy
				for (int j = 0; j < c; ++j) {
					tmp[i][j] = mp[i][j];
				}
			}
			for (int i = 0; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					for (int k = 0; k < 4; ++k) {
						int x = i + DIR[k][0], y = j + DIR[k][1];
						if (x < 0 || x >= r || y < 0 || y >= c) continue; // out of range
						if (mp[x][y] == 'R' && mp[i][j] == 'S') tmp[i][j] = 'R';
						if (mp[x][y] == 'S' && mp[i][j] == 'P') tmp[i][j] = 'S';
						if (mp[x][y] == 'P' && mp[i][j] == 'R') tmp[i][j] = 'P';
					}
				}
			}
			for (int i = 0; i < r; ++i) { // update
				for (int j = 0; j < c; ++j) {
					mp[i][j] = tmp[i][j];
				}
			}
		}
		for (int i = 0; i < r; ++i) { // output
			for (int j = 0; j < c; ++j) {
				cout << mp[i][j];
			}
			cout << endl;
		}
		if (t) cout << endl;
	}
	return 0;
}