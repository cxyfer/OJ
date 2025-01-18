#include <bits/stdc++.h>
using namespace std;

int main(){
    string week[7] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
    int month[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	int n, fd ;
	cin >> n;
	fd = (0-4-31-28-31) % 7 + 7; //4.4 is Mon(0), use to cal 2010/12/31

	while(n--){
		int mm, dd;
		cin >> mm >> dd;

		int w = fd;
		for(int i = 1; i < mm; i++)
			w += month[i-1];
		w = (w + dd) % 7;
		cout << week[w] << endl;
	}
	return 0;
}
