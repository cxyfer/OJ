/*
 * @lc app=leetcode.cn id=1089 lang=cpp
 * @lcpr version=30204
 *
 * [1089] 复写零
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n = arr.size();
        // i 為修改後最後一個元素在原始陣列中的位置，j 用來統計修改後的陣列長度
        int i = 0, j = 0;
        for (; i < n && j < n; i++)
            j += arr[i] == 0 ? 2 : 1;
        i--, j--;
        if (j == n) {  // 超過範圍，代表最後一個元素是0
            arr[j - 1] = 0;
            j -= 2;
            i--;
        }
        for (; i >= 0; i--) {
            arr[j--] = arr[i];
            if (arr[i] == 0) arr[j--] = 0;
        }
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> arr = {1, 0, 2, 3, 0, 4, 5, 0};
    sol.duplicateZeros(arr);
    for (int x : arr) cout << x << " ";
    cout << endl;
    arr = {1, 2, 3};
    sol.duplicateZeros(arr);
    for (int x : arr) cout << x << " ";
    cout << endl;
    return 0;
}

/*
// @lcpr case=start
// [1,0,2,3,0,4,5,0]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

 */

