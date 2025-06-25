/*
 * @lc app=leetcode.cn id=2040 lang=cpp
 * @lcpr version=30204
 *
 * [2040] 两个有序数组的第 K 小乘积
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
// class Solution1:
//     def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
//         n, m = len(nums1), len(nums2)
//         i0 = bisect_left(nums1, 0)
//         j0 = bisect_left(nums2, 0)
//         def check(mx):
//             cnt = 0
//             # 右下區（從左上往右下遞增）
//             j = m - 1
//             for i in range(i0, n):
//                 while j >= j0 and nums1[i] * nums2[j] > mx:
//                     j -= 1
//                 cnt += j - j0 + 1
//             # 左上區（從右下往左上遞增）
//             j = 0
//             for i in range(i0 - 1, -1, -1):
//                 while j < j0 and nums1[i] * nums2[j] > mx:
//                     j += 1
//                 cnt += j0 - j
//             # 右上區（從右上往左下遞增）
//             j = j0
//             for i in range(0, i0):
//                 while j < m and nums1[i] * nums2[j] > mx:
//                     j += 1
//                 cnt += m - j
//             # 左下區（從左下往右上遞增）
//             j = j0 - 1
//             for i in range(n - 1, i0 - 1, -1):
//                 while j >= 0 and nums1[i] * nums2[j] > mx:
//                     j -= 1
//                 cnt += j + 1
//             return cnt >= k
        
//         corners = [nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1]]
//         left, right = min(corners), max(corners)
//         while left <= right:
//             mid = (left + right) // 2
//             if check(mid):
//                 right = mid - 1
//             else:
//                 left = mid + 1
//         return left
class Solution1 {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        int n = nums1.size(), m = nums2.size();
        int i0 = lower_bound(nums1.begin(), nums1.end(), 0) - nums1.begin();
        int j0 = lower_bound(nums2.begin(), nums2.end(), 0) - nums2.begin();
        auto check = [&](long long mx) {
            long long cnt = 0;
            // 右下區
            for (int i = i0, j = m - 1; i < n; ++i) {
                while (j >= j0 && 1LL * nums1[i] * nums2[j] > mx) --j;
                cnt += j - j0 + 1;
            }
            // 左上區
            for (int i = i0 - 1, j = 0; i >= 0; --i) {
                while (j < j0 && 1LL * nums1[i] * nums2[j] > mx) ++j;
                cnt += j0 - j;
            }
            // 右上區
            for (int i = 0, j = j0; i < i0; ++i) {
                while (j < m && 1LL * nums1[i] * nums2[j] > mx) ++j;
                cnt += m - j;
            }
            // 左下區
            for (int i = n - 1, j = j0 - 1; i >= i0; --i) {
                while (j >= 0 && 1LL * nums1[i] * nums2[j] > mx) --j;
                cnt += j + 1;
            }
            return cnt >= k;
        };
        vector<long long> corners = {1LL * nums1[0] * nums2[0], 1LL * nums1[0] * nums2.back(), 1LL * nums1.back() * nums2[0], 1LL * nums1.back() * nums2.back()};
        long long left = *min_element(corners.begin(), corners.end());
        long long right = *max_element(corners.begin(), corners.end());
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            if (check(mid)) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};

class Solution2 {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        auto it1 = lower_bound(nums1.begin(), nums1.end(), 0);
        auto it2 = lower_bound(nums2.begin(), nums2.end(), 0);
        vector<int> neg1(nums1.begin(), it1), pos1(it1, nums1.end());
        vector<int> neg2(nums2.begin(), it2), pos2(it2, nums2.end());
        long long below0 = 1LL * neg1.size() * pos2.size() + 1LL * pos1.size() * neg2.size();
        auto cal = [&](vector<int> arr1, vector<int> arr2, long long mx, bool rev1 = false, bool rev2 = false) -> long long {
            long long cnt = 0;
            int j = arr2.size() - 1;
            if (rev1) reverse(arr1.begin(), arr1.end());
            if (rev2) reverse(arr2.begin(), arr2.end());
            for (int &x : arr1) {
                while (j >= 0 && 1LL * x * arr2[j] > mx) --j;
                cnt += j + 1;
            }
            return cnt;
        };
        auto check = [&](long long mx) {
            long long cnt = 0;
            if (mx >= 0) return below0 + cal(neg1, neg2, mx, true, true) + cal(pos1, pos2, mx) >= k;
            else return cal(pos1, neg2, mx, true, false) + cal(neg1, pos2, mx, false, true) >= k;
        };
        vector<long long> corners = {1LL * nums1[0] * nums2[0], 1LL * nums1[0] * nums2.back(), 1LL * nums1.back() * nums2[0], 1LL * nums1.back() * nums2.back()};
        long long left = *min_element(corners.begin(), corners.end());
        long long right = *max_element(corners.begin(), corners.end());
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            if (check(mid)) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

/*
// @lcpr case=start
// [2,5]\n[3,4]\n2\n
// @lcpr case=end

// @lcpr case=start
// [-4,-2,0,3]\n[2,4]\n6\n
// @lcpr case=end

// @lcpr case=start
// [-2,-1,0,1,2]\n[-3,-1,2,4,5]\n3\n
// @lcpr case=end

 */

