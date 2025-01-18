import 'dart:collection';

class Solution {
  List<int> twoSum(List<int> nums, int target) {
    int n = nums.length;
    // var tbl = Map<int, int>();
    var tbl = HashMap();
    for (int idx=0; idx<n; idx++){
      int num = nums[idx];
      if (tbl.containsKey(target-num)){
        // return [tbl[target-num]!, i]; // !: non-null assertion operator
        return [tbl[target-num], idx];
      }
      tbl[num] = idx;
    }
    return [];
  }
}
