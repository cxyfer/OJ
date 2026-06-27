#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
#define endl '\n'

void solve() {
    int n, typ;
    cin >> n >> typ;

    vector<int> nums(n), tot(n);
    for (int& x : nums) {
        cin >> x;
        ++tot[x];
    }

    i64 ans = 0;
    int B = sqrt(n) + 1;

    // 枚舉出現次數 > B 的元素
    for (int target = 0; target < n; ++target) {
        if (tot[target] <= B) {
            continue;
        }
        // 3739. Count Subarrays With Majority Element II 的 O(n) 作法
        vector<int> cnt(2 * n + 1);
        int s = n;
        cnt[s] = 1;
        i64 lt = 0;
        for (int x : nums) {
            if (x == target) {
                lt += cnt[s];
                ++s;
            } else {
                lt -= cnt[s - 1];
                --s;
            }
            ans += lt;
            ++cnt[s];
        }
    }

    // 出現次數為 B 的元素最多只能是長度為 2B-1 區間的多數元素
    // 因此可以直接枚舉長度 < 2B 的區間，並維護出現次數最多的元素
    // unordered_map<int, int> cnt;  // TLE
    vector<int> cnt(n);
    for (int l = 0; l < n; ++l) {
        vector<int> touched;  // 紀錄被修改過的元素，方便以 O(B) 清空
        int bestCnt = 0, bestVal = -1;
        for (int r = l; r < min(n, l + 2 * B - 1); ++r) {
            int x = nums[r];
            if (cnt[x] == 0) {
                touched.push_back(x);
            }
            ++cnt[x];

            if (cnt[x] > bestCnt) {
                bestCnt = cnt[x];
                bestVal = x;
            }

            int len = r - l + 1;
            if (bestCnt * 2 > len && tot[bestVal] <= B) {
                ++ans;
            }
        }
        // 清空被修改過的元素
        for (int x : touched) {
            cnt[x] = 0;
        }
    }

    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}