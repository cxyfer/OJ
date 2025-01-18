#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e5 + 10;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
#define endl "\n";

int main(){
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr); 
	LL T, x, y;
	cin >> T;
	for (int t=1; t<=T; t++){
		cin >> x >> y;
		cout << "Case " << t << ": " << x << "+" << y << "=" << x + y << endl;
	}
	return 0;
}