class Solution {
  int distributeCandies(int n, int limit) {
    int ans = 0;
    limit = limit < n ? limit : n;
    for (int i=0; i< limit+1; i++){
      for (int j=0; j< limit+1; j++){
        int k = n - i - j;
        if (k >= 0 && k <= limit){
          ans += 1;
        }
      }
    }
    return ans;
  }
}