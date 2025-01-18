#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

class Manacher {
public:
    string s, t;
    vector<int> halfLen;
    int max_i;
    Manacher(string s) {
        this->s = s;
        t = "^";
        for (char ch : s) {
            t += "#";
            t += ch;
        }
        t += "#$";

        halfLen.resize(t.size() - 2, 0);
        halfLen[1] = 1;
        int boxM = 0, boxR = 0, hl = 1;
        max_i = 0;
        for (int i = 2; i < halfLen.size(); i++) {
            hl = 1;
            if (i < boxR) {
                hl = min(halfLen[boxM * 2 - i], boxR - i);
            }
            while (t[i - hl] == t[i + hl]) {
                hl++;
                boxM = i;
                boxR = i + hl;
            }
            halfLen[i] = hl;
            if (hl > halfLen[max_i]) {
                max_i = i;
            }
        }
    }

    // 判斷 [l, r) 是否為回文字串
    bool isPalindrome(int l, int r) {
        return halfLen[l + r + 1] > r - l;
    }

    // 獲取最長回文子字串的長度
    int getMaxPalindromeLength() {
        return halfLen[max_i] - 1;
    }

    // 獲取最長回文子字串
    string getMaxPalindrome() {
        int hl = halfLen[max_i];
        return s.substr((max_i - hl) / 2, hl - 1);
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    cin >> s;
    Manacher manacher(s);
    cout << manacher.getMaxPalindrome() << endl;
    return 0;
}