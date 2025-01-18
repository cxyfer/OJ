#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int N, M;
bool cmp(int a, int b) {
    if (a % M != b % M) return a % M < b % M; // 1. 餘數由小到大
    if (a & 1 ^ b & 1) return a & 1; // 2. 奇數在前偶數在後
    return a & 1 ? a > b : a < b; // 3. 奇數由大到小偶數由小到大
    // if (a & 1 && b & 1) return a > b; // 3a. 都是奇數，由大到小
    // else if (!(a & 1) && !(b & 1)) return a < b; // 3b. 都是偶數，由小到大
    // else return a & 1; // 2. 奇數在前偶數在後
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    while (cin >> N >> M && (N || M)) {
        vector<int> nums(N);
        for (auto &x: nums) cin >> x;
        sort(nums.begin(), nums.end(), cmp);
        cout << N << " " << M << endl;
        for (auto &x: nums) cout << x << endl;  
    }
    cout << "0 0" << endl;
    return 0;
}