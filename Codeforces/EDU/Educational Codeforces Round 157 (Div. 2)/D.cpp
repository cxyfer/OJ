#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N-1);
    for (int i = 0; i < N-1; i++) {
        cin >> A[i];
    }

    int t = A[0]; // B[1] ^ B[N]
    for (int i = 1; i < N-1; i++) {
        t ^= A[i];
    }

    vector<int> B(N);
    for (int i = 0; i < N-1; i++) { // 枚舉第一個數字
        unordered_map<int, int> cnt;
        B[0] = i;
        cnt[i] += 1;
        bool flag = true;
        for (int j = 1; j < N; j++) {
            B[j] = A[j-1] ^ B[j-1];
            if (B[j] >= N || B[j] < 0 || cnt[B[j]] > 0) {
                flag = false;
                break;
            }
            cnt[B[j]] += 1;
        }
        int res = B[0] ^ B[N-1];
        if (res != t) {
            flag = false;
        }
        if (flag) {
            for (int val : B) {
                cout << val << " ";
            }
            cout << endl;
            return 0;
        }
    }

    return 0;
}