#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;

bool isVowel(char ch) {
    return ch == 'a' || ch == 'e';
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        vector<string> ans;
        int n; cin >> n;
        string s; cin >> s;
        int i = 0;
        while (i < n){
            if ((i+3) >= n) {
                ans.push_back(s.substr(i, n-i));
                break;
            }
            if (isVowel(s[i+1]) && !isVowel(s[i+2]) && !isVowel(s[i+3])) { // CVCC
                ans.push_back(s.substr(i, 3));
                i += 3;
            } else {
                ans.push_back(s.substr(i, 2));
                i += 2;
            }
        }
        for (int i = 0; i < ans.size(); ++i) {
            cout << ans[i] << ".\n"[i+1==ans.size()]; 
        }
    }
    return 0;
}

/*
".\n"[i+1==ans.size()] 這部分的程式碼是一個條件運算子，它會根據條件 i+1==ans.size() 的結果來選擇輸出哪個字符。如果 i+1 等於 ans.size()（也就是說，當前元素是陣列的最後一個元素），則條件為真，選擇的字符是 '\n'（換行符）。否則，條件為假，選擇的字符是 '.'。
所以，這段程式碼的效果是：對於 ans 陣列的每個元素，如果它不是最後一個元素，則在其後面添加一個點 '.'；如果它是最後一個元素，則在其後面添加一個換行符 '\n'。
*/