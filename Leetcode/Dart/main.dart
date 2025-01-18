class Solution {
  String findTheDifference(String s, String t) {
    int ans = 0;
    String ss = s + t ;
    for (int i = 0; i<ss.length; i++){
        ans ^= ss.codeUnitAt(i); // ASCII CODE
    }
    return String.fromCharCode(ans); // 
  }
}

