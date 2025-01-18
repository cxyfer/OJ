#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
	int t, n, cnt[10];
	cin >> t;
	while (t--) {
		cin >> n;
		if (n <= 1) {
			cout << n << endl;
			continue;
		}
		memset(cnt, 0, sizeof(cnt)); 
		for (int p = 9; p > 1; p--) { // 因數分解
			while (n % p == 0) {
				cnt[p]++;
				n /= p;
			}
		}
		if (n != 1) { // 有大於10的因數
			cout << -1 << endl;
		} else {
			string ans = "";
			for (int p = 2; p < 10; p++) {
				while (cnt[p] --) {
					cout << p;
				}
			}
			cout << endl;
		}
	}
	return 0;
}