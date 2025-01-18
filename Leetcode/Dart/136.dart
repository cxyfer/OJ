class Solution {
  int singleNumber(List<int> nums) {
    int ans = 0;
    for (int num in nums){
      ans ^= num;
    }
    return ans;
  }
}

void main(){
  Solution sol = new Solution();
  print(sol.singleNumber([2,2,1]));
}