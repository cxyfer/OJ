#include <stdio.h>

int FN(int n){
    if(n <= 3)
        return n;
    return FN(n-1)*FN(n-2)*FN(n-3);
}

int main(){
    printf("%d", FN(5) >> 3 << 3);
    return 0;
}