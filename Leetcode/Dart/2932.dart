import 'dart:math';

class Solution {
  int maximumStrongPairXor(List<int> nums) {
    int n = nums.length;
    int ans = 0;
    for (int i=0; i<n; i++){
      for (int j=i+1; j<n; j++){
        int x = nums[i];
        int y = nums[j];
        if ( (x-y).abs() <= min(x,y) ){
          ans = max(ans, x^y);
        }
      }
    }
    return ans;
  }
}