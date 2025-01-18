#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve1() {
    int n; cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    sort(nums.begin(), nums.end());
    int ans = 1;
    for (int i = 1; i < n; i++) {
        if (nums[i] != nums[i - 1]) ans++;
    }
    cout << ans << endl;
}

void solve2() {
    int n, x; 
    cin >> n;
    set<int> nums;
    for (int i = 0; i < n; i++) {
        cin >> x;
        nums.insert(x);
    }
    cout << nums.size() << endl;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    // solve1();
    solve2();
    return 0;
}