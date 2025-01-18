import 'dart:math';

class Solution {
  int minCostClimbingStairs(List<int> cost) {
    int n = cost.length;
    List<int> dp = List<int>.filled(n+1, 0);
    // You can either start from the step with index 0, or the step with index 1.
    for (int i=2; i<n+1; i++){
      dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1]);
    }
    return dp[n];
  }
}