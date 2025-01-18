class Solution {
  List<int> plusOne(List<int> digits) {
    digits.insert(0, 0); // 避免進位
    int n = digits.length;
    int last = n - 1; // 最後一個數字的 index
    digits[last] += 1;
    while (digits[last] >= 10) {
      digits[last] -= 10;
      last -= 1;
      digits[last] += 1;
    }
    return digits[0] == 0 ? digits.sublist(1) : digits;
  }
}

void main(){
  Solution solution = new Solution();
  print(solution.plusOne([1,2,3])); // [1,2,4]
  print(solution.plusOne([4,3,2,1])); // [4,3,2,2]
  print(solution.plusOne([0])); // [1]
  print(solution.plusOne([9])); // [1,0]
}