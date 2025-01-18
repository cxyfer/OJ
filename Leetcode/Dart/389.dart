class Solution {
  String findTheDifference(String s, String t) {
    int ans = 0;
    String c = s + t;
    for (int i=0; i<c.length; i++){
      ans ^= c.codeUnitAt(i);
    }
    return String.fromCharCode(ans);
  }
}