#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int caseNum = 0; caseNum < t; caseNum++) {
        int n;
        cin >> n;

        vector<int> nums(n);
        for (int i = 0; i < n; i++) {
            cin >> nums[i];
        }

        unordered_map<int, int> cnt;
        for (int num : nums) {
            // 質因數分解
            int prime = 2;
            while (num > 1) {
                if (num % prime == 0) {
                    num /= prime;
                    cnt[prime]++;
                } else {
                    prime++;
                }
            }
        }

        string ans = "YES";
        for (const auto& kvp : cnt) {
            if (kvp.second % n != 0) {
                ans = "NO";
                break;
            }
        }

        cout << ans << endl;
    }

    return 0;
}