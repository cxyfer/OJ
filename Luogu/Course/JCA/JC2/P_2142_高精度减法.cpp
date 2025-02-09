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
        n = n >= 0 ? n : -n;
        
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

    BigInt operator*(const BigInt& other) const {
        if ((ln == 1 && v[0] == 0) || (other.ln == 1 && other.v[0] == 0)) {
            return BigInt(0);
        }
        
        BigInt res;
        res.sign = sign * other.sign;
        res.ln = ln + other.ln;
        res.v.resize(res.ln, 0);
        
        for (int i = 0; i < ln; i++) {
            if (v[i] == 0) continue;  // Skip if multiplier is 0
            long long carry = 0;
            for (int j = 0; j < other.ln; j++) {
                long long cur = res.v[i + j] + (long long)v[i] * other.v[j] + carry;
                res.v[i + j] = cur % BASE;
                carry = cur / BASE;
            }
            if (carry) res.v[i + other.ln] = carry;
        }
        
        while (res.ln > 1 && res.v[res.ln - 1] == 0) res.ln--;
        res.v.resize(res.ln);
        return res;
    }

    BigInt operator/(const BigInt& divisor) const {
        if (divisor.ln == 1 && divisor.v[0] == 0) {
            throw runtime_error("Division by zero");
        }
        if (abs_less(*this, divisor)) return BigInt(0);
        if (divisor.ln == 1 && divisor.v[0] == 1) {
            BigInt res = *this;
            res.sign *= divisor.sign;
            return res;
        }

        // Optimize: Use binary search to speed up division
        BigInt res;
        res.sign = sign * divisor.sign;
        res.v.resize(ln);
        res.ln = ln;
        
        BigInt current;
        current.sign = 1;
        BigInt divisor_abs = divisor;
        divisor_abs.sign = 1;

        for (int i = ln - 1; i >= 0; i--) {
            // Shift left and add new digit
            current.v.insert(current.v.begin(), v[i]);
            current.ln = current.v.size();
            
            // Binary search to find the quotient for the current position
            int left = 0, right = BASE - 1;
            int quotient = 0;
            
            while (left <= right) {
                int mid = (left + right) >> 1;
                BigInt temp = divisor_abs * BigInt(mid);
                
                if (temp <= current) {
                    quotient = mid;
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            
            res.v[i] = quotient;
            current = current - (divisor_abs * BigInt(quotient));
        }

        // Remove leading zeros
        while (res.ln > 1 && res.v[res.ln - 1] == 0) {
            res.ln--;
        }
        res.v.resize(res.ln);
        return res;
    }

    BigInt operator%(const BigInt& divisor) const {
        if (divisor.ln == 1 && divisor.v[0] == 0) {
            throw runtime_error("Division by zero");
        }
        if (abs_less(*this, divisor)) return *this;
        if (divisor.ln == 1 && divisor.v[0] == 1) {
            return BigInt(0);
        }

        // Optimize: Use division result to calculate remainder
        BigInt quotient = *this / divisor;
        return *this - (quotient * divisor);
    }

    BigInt operator^(const int& n) const {
        // Handle special cases
        if (n < 0) {
            throw runtime_error("Negative exponent not supported");
        }
        if (n == 0) {
            return BigInt(1);
        }
        if (n == 1) {
            return *this;
        }
        if (ln == 1 && v[0] == 0) {  // 0^n = 0
            return BigInt(0);
        }
        if (ln == 1 && v[0] == 1) {  // 1^n = 1
            return BigInt(1);
        }
        
        // Initialize result as 1
        BigInt res(1);
        BigInt base(*this);
        int exp = n;
        
        // Fast power algorithm
        while (exp > 0) {
            if (exp & 1) {  // If current exponent bit is 1
                res = res * base;
            }
            base = base * base;  // Square the base
            exp >>= 1;  // Move to next bit
        }
        
        // Handle sign
        if (sign == -1 && (n & 1)) {  // Negative base and odd exponent
            res.sign = -1;
        } else {
            res.sign = 1;
        }
        
        return res;
    }

    bool operator>(const BigInt& other) const {
        if (sign != other.sign) {
            return sign > other.sign;
        }
        if (sign == 1) {
            return !abs_less(*this, other) && !(*this == other);
        } else {
            return abs_less(*this, other);
        }
    }

    bool operator<(const BigInt& other) const {
        if (sign != other.sign) {
            return sign < other.sign;
        }
        if (sign == 1) {
            return abs_less(*this, other);
        } else {
            return !abs_less(*this, other) && !(*this == other);
        }
    }

    bool operator==(const BigInt& other) const {
        if (sign != other.sign || ln != other.ln) {
            return false;
        }
        for (int i = 0; i < ln; i++) {
            if (v[i] != other.v[i]) {
                return false;
            }
        }
        return true;
    }

    bool operator!=(const BigInt& other) const {
        return !(*this == other);
    }

    bool operator>=(const BigInt& other) const {
        return *this > other || *this == other;
    }

    bool operator<=(const BigInt& other) const {
        return *this < other || *this == other;
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
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    BigInt a, b;
    cin >> a >> b;
    cout << a - b << endl;
    return 0;
}