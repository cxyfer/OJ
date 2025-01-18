class Solution {
  int addDigits(int num) {
    while (num >= 10) {
        int tmp = 0;
        while (num > 0) {
            tmp += num % 10;
            num = num ~/ 10; // 整除
        }
        num = tmp;
    }
    return num;
  }
}

void main(){
  Solution solution = new Solution();
  print(solution.addDigits(38)); // 2
  print(solution.addDigits(0)); // 0
}