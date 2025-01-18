#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int f(string s1, string s2){
    int n1 = s1.size(), n2 = s2.size();
    int st = 0, j = 0;
    while ((st + j) < n1 && j < n2){
        if (!(s1[st + j] == '2' && s2[j] == '2')){
            j++;
        }else{
            st++;
            j = 0;
        }
    }
    return n1 + n2 - j;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s1, s2;
    while (cin >> s1 >> s2){
        cout << min(f(s1, s2), f(s2, s1)) << endl;
    }
    return 0;
}