import 'dart:math';

class Solution {
  int findMinimumOperations(String s1, String s2, String s3) {
    int x=s1.length, y=s2.length, z=s3.length;
    int n = min(x, min(y,z));
    int lcp = 0; // Longest Common Prefix
    for(int i=0; i<n; i++){
      if (s1[i] != s2[i] || s2[i] != s3[i]){
        break;
      }
      lcp += 1;
    }
    return lcp == 0 ? -1 : x+y+z-3*lcp;
  }
}