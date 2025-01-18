class Solution {
  String findTheDifference(String s, String t) {
    // Similar to 136. Single Number
    int ans = 0;
    String c = s + t;
    for (int i=0; i<c.length; i++){
      ans ^= c.codeUnitAt(i); // ASCII code 
    }
    return String.fromCharCode(ans);
  }
}