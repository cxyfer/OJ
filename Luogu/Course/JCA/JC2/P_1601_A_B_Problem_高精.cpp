#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

const int DLEN = 4;
const int BASE = pow(10.0, DLEN);

class BigInt {
    vector<int> v;
    int sign;
    int ln;
public:
    BigInt() : sign(1), ln(1) { v.resize(1, 0); }
    BigInt(int n) {
        // Handle negative numbers
        sign = n >= 0 ? 1 : -1;
        n = abs(n);
        
        // Handle zero case
        if (n == 0) {
            ln = 1;
            v.resize(1);
            v[0] = 0;
            return;
        }
        
        // Convert to string first for easier processing
        string s = to_string(n);
        ln = (s.length() + DLEN - 1) / DLEN;
        v.resize(ln);
        
        // Process digits in groups of DLEN
        int pos = 0;
        for (int i = s.length() - 1; i >= 0; i -= DLEN) {
            int temp = 0;
            for (int j = max(0, i - DLEN + 1); j <= i; j++) {
                temp = temp * 10 + (s[j] - '0');
            }
            v[pos++] = temp;
        }
    }
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
        while (s[j] == '0') j++;
        s = s.substr(j);
        if (s.empty()) s = "0";  // if all zeros
        
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
                temp = temp * 10 + (s[j] - '0');
            }
            v[pos++] = temp;
        }
    }
    BigInt operator+(const BigInt& other) const {
        // If signs are different, convert to subtraction
        if (sign != other.sign) {
            BigInt temp = other;
            temp.sign = -temp.sign;
            return *this - temp;
        }
        
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
    BigInt operator-(const BigInt& other) const {
        // If signs are different, convert to addition
        if (sign != other.sign) {
            BigInt temp = other;
            temp.sign = -temp.sign;
            return *this + temp;
        }
        
        // Compare absolute values
        bool swapped = false;
        const BigInt *a = this;
        const BigInt *b = &other;
        
        if (abs_less(*this, other)) {
            swap(a, b);
            swapped = true;
        }
        
        // Initialize result
        BigInt res;
        res.sign = swapped ? -sign : sign;
        res.ln = a->ln;
        res.v.resize(res.ln);
        
        // Subtract corresponding digits
        int borrow = 0;
        for (int i = 0; i < res.ln; i++) {
            int diff = a->v[i] - borrow;
            if (i < b->ln) diff -= b->v[i];
            
            if (diff < 0) {
                diff += BASE;  // Changed from 10000 to BASE
                borrow = 1;
            } else {
                borrow = 0;
            }
            res.v[i] = diff;
        }
        
        // Remove leading zeros
        while (res.ln > 1 && res.v[res.ln - 1] == 0) {
            res.ln--;
        }
        res.v.resize(res.ln);
        
        // Handle zero case
        if (res.ln == 1 && res.v[0] == 0) {
            res.sign = 1;
        }
        
        return res;
    }

    friend ostream& operator<<(ostream& out, const BigInt& num) {
        if (num.sign == -1) out << '-';
        
        // Print first group without leading zeros
        out << num.v[num.ln - 1];
        
        // Print remaining groups with leading zeros
        for (int i = num.ln - 2; i >= 0; i--) {
            out << setfill('0') << setw(DLEN) << num.v[i];
        }
        return out;
    }

    friend istream& operator>>(istream& in, BigInt& num) {
        string s;
        in >> s;
        num = BigInt(s);  // Use the string constructor we already have
        return in;
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
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    BigInt a, b;
    cin >> a >> b;
    cout << a + b << endl;  // 輸出 A + B 的結果
    return 0;
}