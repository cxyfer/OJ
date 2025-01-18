/*
 * @lc app=leetcode.cn id=762 lang=cpp
 *
 * [762] 二进制表示中质数个计算置位
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int N = 20;

int bit_count(int n) {
    int cnt = 0;
    while (n) {
        n &= n - 1; // 消除最低位的 1
        cnt++;
    }
    return cnt;
}
class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        // return solve1(left, right);
        // return solve2(left, right);
        return solve3(left, right);
    }
    int solve1(int left, int right) {
        auto is_prime = [](int n) {
            if (n < 2 || n % 2 == 0 && n != 2) return false; // 先判斷是否為2的倍數
            for (int i = 3; i <= sqrt(n); i += 2) { // // 之後只判斷是否為奇數的倍數
                if (n % i == 0) return false;
            }
            return true;
        };
        int ans = 0;
        for (int i = left; i <= right; i++) {
            if (is_prime(bit_count(i))) ans++;
        }
        return ans;
    }
    int solve2(int left, int right) {
        bool is_prime[N];
        memset(is_prime, true, sizeof(is_prime));
        is_prime[0] = is_prime[1] = false;
        for (int i = 2; i * i < N; i++) { // 埃氏篩法
            if (is_prime[i]) {
                for (int j = i * i; j < N; j += i) {
                    is_prime[j] = false;
                }
            }
        }
        int ans = 0;
        for (int i = left; i <= right; i++) {
            if (is_prime[bit_count(i)]) ans++;
        }
        return ans;
    }
    int solve3(int left, int right) { // 範圍內的質數只有 2,3,5,7,11,13,17,19
        int ans = 0;
        for (int i = left; i <= right; i++) {
            if ((1 << bit_count(i)) & 0b10100010100010101100) ans++;
        }
        return ans;
    }
};
// @lc code=end

