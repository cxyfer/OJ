/*
 * @lc app=leetcode.cn id=567 lang=cpp
 *
 * [567] 字符串的排列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        if (m > n) return false;
        unordered_map<char, int> cnt;
        for (char ch : s1) cnt[ch]++;
        int left = 0, need = cnt.size(), have = 0;
        for (int right = 0; right < n; right++) {
            char ch = s2[right];
            if (cnt.find(ch) != cnt.end()) {
                cnt[ch]--;
                if (cnt[ch] == 0) have++;
            }
            while (right - left + 1 > m) {
                char lc = s2[left];
                if (cnt.find(lc) != cnt.end()) {
                    cnt[lc]++;
                    if (cnt[lc] == 1) have--;
                }
                left++;
            }
            if (have == need) return true;
        }
        return false;
    }
};

class Solution2 {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        if (m > n) return false;
        vector<int> cnt(26); // 每個字元還需要的數量
        for (char ch : s1) cnt[ch - 'a']++;
        int left = 0;
        for (int right = 0; right < n; right++) {
            int idx = s2[right] - 'a';
            cnt[idx]--;
            while (cnt[idx] < 0) { // 這個字元的數量太多了
                cnt[s2[left] - 'a']++;
                left++;
            }
            if (right - left + 1 == m) return true; // 窗口大小等於 s1 的長度
        }
        return false;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end