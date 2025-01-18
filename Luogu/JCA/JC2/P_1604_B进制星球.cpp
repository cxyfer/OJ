#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int B;
int DLEN = 4;
int BASE = pow(10.0, DLEN);

class BigInt {
    vector<int> v;
    int sign;
    int ln;
public:
    BigInt() : sign(1), ln(1) { v.resize(1, 0); }
    BigInt(string s) {
        // Handle empty string
        if (s.empty()) {
            ln = 1;
            v.resize(1);
            v[0] = 0;
            sign = 1;
            return;
        }
        
        // Handle negative sign
        sign = (s[0] == '-') ? -1 : 1;
        if (s[0] == '-') s = s.substr(1);
        
        // Remove leading zeros
        int j = 0;
        while (j < s.length() && s[j] == '0') j++;
        s = j == s.length() ? "0" : s.substr(j);
        
        // Handle zero case
        if (s == "0") {
            ln = 1;
            v.resize(1);
            v[0] = 0;
            return;
        }

        ln = (s.length() + DLEN - 1) / DLEN;
        v.resize(ln);
        
        int pos = 0;
        for (int i = s.length() - 1; i >= 0; i -= DLEN) {
            int temp = 0;
            for (int j = max(0, i - DLEN + 1); j <= i; j++) {
                temp = temp * B + char_to_digit(s[j]);
            }
            v[pos++] = temp;
        }
    }
    BigInt operator+(const BigInt& other) const {
        // Initialize result
        BigInt res;
        res.sign = sign;  // Same sign as operands
        res.ln = max(ln, other.ln) + 1;  // +1 for possible carry
        res.v.resize(res.ln);
        
        // Add corresponding digits
        int carry = 0;
        for (int i = 0; i < res.ln - 1; i++) {
            int sum = carry;
            if (i < ln) sum += v[i];
            if (i < other.ln) sum += other.v[i];
            
            if (sum >= BASE) {
                carry = 1;
                sum -= BASE;
            } else {
                carry = 0;
            }
            res.v[i] = sum;
        }
        
        // Handle final carry
        res.v[res.ln - 1] = carry;
        
        // Remove leading zeros
        while (res.ln > 1 && res.v[res.ln - 1] == 0) {
            res.ln--;
        }
        res.v.resize(res.ln);
        
        return res;
    }

    friend ostream& operator<<(ostream& out, const BigInt& num) {
        if (num.sign == -1) out << '-';
        
        // Handle zero case
        if (num.ln == 1 && num.v[0] == 0) {
            out << "0";
            return out;
        }
        
        // Print first group
        string first = to_base(num.v[num.ln - 1]);
        out << first;
        
        // Print remaining groups with proper padding
        for (int i = num.ln - 2; i >= 0; i--) {
            string group = to_base(num.v[i]);
            // Pad with zeros to maintain DLEN digits in B base
            while (group.length() < DLEN) group = "0" + group;
            out << group;
        }
        return out;
    }

    friend istream& operator>>(istream& in, BigInt& num) {
        string s;
        in >> s;
        num = BigInt(s);  // Use the string constructor we already have
        return in;
    }

    BigInt abs() const {
        BigInt res = *this;
        res.sign = 1;
        return res;
    }

private:
    // Helper function to compare absolute values
    static bool abs_less(const BigInt& a, const BigInt& b) {
        if (a.ln != b.ln) return a.ln < b.ln;
        for (int i = a.ln - 1; i >= 0; i--) {
            if (a.v[i] != b.v[i]) {
                return a.v[i] < b.v[i];
            }
        }
        return false;
    }

    // Convert character to digit value
    static int char_to_digit(char c) {
        if (isdigit(c)) return c - '0';
        if (isupper(c)) return c - 'A' + 10;
        if (islower(c)) return c - 'a' + 10;
        return 0;
    }

    // Convert digit value to character
    static char digit_to_char(int d) {
        if (d < 10) return '0' + d;
        return 'A' + (d - 10);
    }

    static string to_base(int n) {
        if (n == 0) return "0";
        string res;
        while (n > 0) {
            res = digit_to_char(n % B) + res;
            n /= B;
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    cin >> B;
    BASE = pow(double(B), DLEN);

    BigInt a, b;
    cin >> a >> b;
    cout << a + b << endl;
}