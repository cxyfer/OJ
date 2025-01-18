#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	while (cin >> n){
		vector<int> nums(n);
		for (auto &x: nums) cin >> x;
		vector<int> cnt(n);
        for (int i = 0; i < n; ++i) cnt[i] = 0;
        bool flag = true;
        for (int i = 0; i < n - 1; ++i) {
            int d = abs(nums[i] - nums[i + 1]);
            if (d < 1 || d >= n || cnt[d-1] > 0) {
                flag = false;
                break;
            }
            cnt[d-1] += 1;
        }
        cout << (flag ? "Jolly" : "Not jolly") << endl;
	}
}
