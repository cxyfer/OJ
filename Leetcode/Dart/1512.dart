import 'dart:collection';

class Solution {
  int numIdenticalPairs(List<int> nums) {
    int ans = 0;
    // Map<int, int> cnt = Map();
    Map<int, int> cnt = HashMap();
    for (int num in nums) {
      ans += cnt[num] ?? 0;
      cnt[num] = (cnt[num] ?? 0) + 1;
    }
    return ans;
  }
}

void main(){
  Solution sol = new Solution();
  print(sol.numIdenticalPairs([1,2,3,1,1,3])); // 4
  print(sol.numIdenticalPairs([1,1,1,1])); // 6
}