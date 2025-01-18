#include <bits/stdc++.h>
using namespace std;

int main() {
    int kase = 1;
    string s, lang;
    while (cin >> s && s != "#") {
        if (s == "HELLO") lang = "ENGLISH";
        else if (s == "HOLA") lang = "SPANISH";
        else if (s == "HALLO") lang = "GERMAN";
        else if (s == "BONJOUR") lang = "FRENCH";
        else if (s == "CIAO") lang = "ITALIAN";
        else if (s == "ZDRAVSTVUJTE") lang = "RUSSIAN";
        else lang = "UNKNOWN";
        cout << "Case " << kase++ << ": " << lang << endl;
    }
    return 0;
}