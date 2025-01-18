#include <bits/stdc++.h>
using namespace std;
const int N = 9;
#define endl '\n'

int main() {
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
	int x, coef[N];
	while (cin >> x) {
		coef[0] = x;
		for (int i = 1; i < N; i++) cin >> coef[i];
		// 先特判是不是全為 0 ，如果是的話直接輸出 0
		bool all_zero = true;
		for (int i = 0; i < N; i++) {
			if (coef[i]) {
				all_zero = false;
				break;
			}
		}
		if (all_zero) {
			cout << 0 << endl;
			continue;
		}
		// 輸出多項式
		bool flag = false; // 第一項前面不用加 + 或 - ，所以 flag = false
		for (int i = 0; i < N; i++) {
			if (!coef[i]) {
				continue;
			}
			if (flag) { // 不是第一項
				cout << (coef[i] > 0 ? " + " : " - ");
			} else { // 是第一項
				if (coef[i] < 0) {
					cout << "-";
				}
				flag = true;
			}
			int x = abs(coef[i]); // 係數部分
			int m = N - 1 - i; // 次方
			if (x != 1 || m == 0) { // 係數部分不是 1 或是次方是 0 的話才輸出係數部分
				cout << x;
			}
			if (m > 1) { // 次方大於 1 才輸出次方
				cout << "x^" << m;
			} else if (m == 1) {
				cout << "x";
			}
		}
		cout << endl;
		
	}
	return 0;
}