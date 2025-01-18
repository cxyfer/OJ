#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
	int k, n, m, x, y;
	while (cin >> k && k) {
		cin >> n >> m;
		while (k--) {
			cin >> x >> y;
			if (x == n || y == m) cout << "divisa" << endl;
			else if (x > n && y > m) cout << "NE" << endl;
			else if (x > n && y < m) cout << "SE" << endl;
			else if (x < n && y > m) cout << "NO" << endl;
			else cout << "SO" << endl;
		}
		
	}
	return 0;
}