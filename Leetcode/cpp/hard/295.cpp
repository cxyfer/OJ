/*
 * @lc app=leetcode.cn id=295 lang=cpp
 *
 * [295] 数据流的中位数
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class MedianFinder {
 public:
  // max heap，保存 <= median 的數字
  priority_queue<int> l;
  // min heap，保存 > median 的數字
  priority_queue<int, vector<int>, greater<int>> r;

  MedianFinder() {}

  void addNum(int num) {
    // 若當前數量為偶數，則應該將新數字加入到左邊
    if (l.size() == r.size()) {
      // 如果新數字比右邊的最小值還要大，則把右邊的最小值加入到左邊、把新數字加入到右邊
      if (!r.empty() && num > r.top()) {
        l.push(r.top()); r.pop();
        r.push(num);
      } else {
        l.push(num);
      }
      // 若當前數量為奇數，則應該將新數字加入到右邊
    } else {
      // 如果新數字比左邊的最大值還要小，則把左邊的最大值加入到右邊、把新數字加入到左邊
      if (num < l.top()) {
        r.push(l.top()); l.pop();
        l.push(num);
      } else {
        r.push(num);
      }
    }
  }

  double findMedian() {
    return l.size() == r.size() ? l.top() + (r.top() - l.top()) / 2.0 : l.top();
  }
};
// @lc code=end
