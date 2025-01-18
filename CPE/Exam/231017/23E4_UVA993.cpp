#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;
#define endl '\n'

int main() {
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
	int t; LL n;
	cin >> t;
	while (t--) {
		cin >> n;
		if (n == 0) {
			cout << 0 << endl;
			continue;
		}
		int cnt[10] = {0};
		for (int i = 9; i > 1; --i) {
			while (n % i == 0) {
				cnt[i]++;
				n /= i;
			}
		}
		if (n != 1) cout << -1 << endl;
		else {
			string ans = "";
			for (int i = 2; i < 10; ++i) {
				ans += string(cnt[i], i + '0');
			}
			cout << (ans.empty() ? "1" : ans) << endl;
		}
	}
	return 0;
}