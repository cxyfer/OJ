/*
    DP：LIS (Longest Increasing Subsequence)
    每種積木的數量不限，且每種積木有六種擺放方式，
    故可以將所有積木的六種擺放方式排序後，求 LIS
    令 dp[i] 表示以第 i 個積木為最後一個積木(最下面)時的最大高度
    tags: DP, LIS, 紫書, CPE-171219, CPE-211019, CPE-221018
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Block {
    int x, y, z;
    Block(int x, int y, int z) : x(x), y(y), z(z) {}
    bool operator<(const Block &b) const {
        return x < b.x || (x == b.x && y < b.y);
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, kase = 1;
    while (cin >> n && n) {
        vector<Block> blocks;
        for (int i = 0, x, y, z; i < n; i++) {
            cin >> x >> y >> z;
            blocks.push_back(Block(x, y, z));
            blocks.push_back(Block(x, z, y));
            blocks.push_back(Block(y, x, z));
            blocks.push_back(Block(y, z, x));
            blocks.push_back(Block(z, x, y));
            blocks.push_back(Block(z, y, x));
        }
        sort(blocks.begin(), blocks.end());
        int ans = 0;
        vector<int> dp(6 * n);
        for (int i = 0; i < 6 * n; i++) {
            dp[i] = blocks[i].z;
            for (int j = 0; j < i; j++) {
                if (blocks[i].x > blocks[j].x && blocks[i].y > blocks[j].y) {
                    dp[i] = max(dp[i], dp[j] + blocks[i].z);
                }
            }
            ans = max(ans, dp[i]);
        }
        cout << "Case " << kase++ << ": maximum height = " << ans << endl;
    }
    return 0;
}