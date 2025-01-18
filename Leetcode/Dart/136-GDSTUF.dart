class Solution {
  int singleNumber(List<int> nums) {
    // XOR
    // 1. 0 ^ x = x
    // 2. x ^ x = 0
    // 3. XOR is commutative and associative
    int ans = 0 ;
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