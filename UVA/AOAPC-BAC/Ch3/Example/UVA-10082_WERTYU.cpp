/*
    字串索引
    tags: string, 紫書-Ch3, CPE-160322
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./";
    string s;
    while (getline(cin, s)) {
        for (char ch: s){
            if (ch == ' ') cout << " ";
            else cout << keyboard[keyboard.find(ch) - 1];
        }
        cout << endl;
    }
    return 0;
}