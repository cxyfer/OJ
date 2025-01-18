#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = INT_MAX;
        vector<int> st;
        for (int x : nums) {
            vector<int> st2;
            st2.push_back(x);
            for (int y : st) {
                if ((y & x) != st2.back()) {
                    st2.push_back(y & x);
                }
            }
            st = st2;
            for (int y : st) {
                ans = min(ans, abs(y - k));
            }
        }
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 4, 5};
    cout << sol.minimumDifference(nums, 3) << endl; // 1
    nums = {1, 2, 1, 2};
    cout << sol.minimumDifference(nums, 2) << endl; // 0
    nums = {1};
    cout << sol.minimumDifference(nums, 10) << endl; // 9
    nums = {5, 13, 90, 92, 49};
    cout << sol.minimumDifference(nums, 10) << endl; // 2
}