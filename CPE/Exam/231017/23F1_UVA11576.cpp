#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
	int t, n, m, ans;
	cin >> t;
	while (t--) {
        ans = 0;
		cin >> n >> m;
		vector<string> words(m);
		for (int i=0; i<m; i++){
			cin >> words[i];
		}
		ans = n * m;
		for (int i=0; i<m-1; i++){
			for (int j=0; j<n; j++){
                if (words[i].substr(j) == words[i+1].substr(0, n-j)){
                    ans -= n - j;
                    break;
                }
            }
		}
        cout << ans << endl;
	}
}