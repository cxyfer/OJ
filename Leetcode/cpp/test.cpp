#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;
#define endl '\n'

int main() {
    unsigned short a = 65535;
    unsigned short b = 65535;
    unsigned short c = 65535;
    unsigned short ans1 = a * b / c;
    unsigned short ans2 = a * a / a;
    unsigned short ans3 = 65535 * 65535 / 65535;
    cout << ans1 << endl; // result: 65534
    cout << ans2 << endl; // result: 65534
    cout << ans3 << endl; // result: 65534
    cout << 65535 * 65535 / 65535 << endl; // result: 65534

    // unsigned short ans = (LL) a * b / c;
    // cout << ans << endl; // 65535
    // unsigned short d = a*b; // 以 32 位有號數計算後，將結果轉為 16 位無號數
    // unsigned short e = a*b/c;


    // cout << d << endl;
    // string d_str1 = bitset<16>(a*b).to_string(); // 0000000000000001
    // string d_str2 = bitset<32>(a*b).to_string(); // 11111111111111100000000000000001
    // string d_str3 = bitset<32>(65535*65535).to_string(); // 11111111111111100000000000000001
    // cout << d_str1 << endl << d_str2 << endl << d_str3 << endl;

    // LL d2 = (LL) a*b;
    // LL d3 = 0b11111111111111100000000000000001;
    // cout << d2 << endl; // 4294836225
    // cout << d3 << endl; // 4294836225
    // cout << a * b << endl; // -131071 (在 32 位下以有號數表示會 overflow)
    // cout << 65535*65535 << endl; // -131071 (overflow)
    // cout << (LL) 65535*65535 << endl; // 4294836225 (correct)

    // cout << e << endl; // 65534 
    // string e_str1 = bitset<16>(a*b/c).to_string(); // 1111111111111110
    // string e_str2 = bitset<32>(a*b/c).to_string(); // 11111111111111111111111111111110
    // string e_str3 = bitset<32>(65535*65535/65535).to_string(); // 11111111111111111111111111111110
    // cout << e_str1 << endl << e_str2 << endl << e_str3 << endl;
    // string e_str4 = bitset<64>(65535*65535/65535).to_string(); 
    // cout << e_str4 << endl; //

    // cout << -131071 / 65535 << endl; // -2 
    // string f_str1 = bitset<16>(-2).to_string(); 
    // string f_str2 = bitset<32>(-2).to_string(); 
    // cout << f_str1 << endl << f_str2 << endl;
    // return 0;
}