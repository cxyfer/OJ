import 'dart:math';

class Solution {
  int sumCounts(List<int> nums) {
    int n = nums.length;
    int ans = 0;
    for (int l = 1; l < n + 1; l++) { // 枚舉長度
      for (int i = 0; i <= n - l; i++) { // 枚舉起始位置
        var set = Set<int>.from(nums.sublist(i, i + l));
        // ans += set.length * set.length;
        ans += pow(set.length, 2).toInt();
      }
    }
    return ans;
  }
}

class Solution2 {
  int sumCounts(List<int> nums) {
    int n = nums.length;
    int ans = 0;
    for (int i=0; i<n; i++){
      for (int j=i; j<n; j++){
        var set = Set<int>.from(nums.sublist(i, j+1));
        // ans += set.length * set.length;
        ans += pow(set.length, 2).toInt();
      }
    }
    return ans;
  }
}

// int sumCounts(List<int> nums) {
//   int n = nums.length;
//   int ans = 0;
//   for (int l = 1; l <= n; l++) {
//     for (int i = 0; i <= n - l; i++) {
//       ans += Set<int>.from(nums.sublist(i, i + l)).length.pow(2);
//     }
//   }
//   return ans;
// }