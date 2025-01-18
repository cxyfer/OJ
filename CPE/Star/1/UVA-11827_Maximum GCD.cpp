#include <bits/stdc++.h>
using namespace std;
const int N = 105;
#define endl '\n'

vector<int> nums(N);

int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    cin.ignore(1024, '\n');
    while (t--) {
        string line;
        getline(cin, line);
        stringstream ss(line);
        int n = 0;
        while (ss >> nums[n]) n++;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                ans = max(ans, gcd(nums[i], nums[j]));
            }
        }
        cout << ans << endl;
    }
    return 0;
}