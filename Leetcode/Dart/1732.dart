class Solution {
  int largestAltitude(List<int> gain) {
    int ans = 0;
    int pre = 0;
    for (int g in gain){
      pre = pre + g;
      ans = pre > ans ? pre : ans;
    }
    return ans;
  }
}