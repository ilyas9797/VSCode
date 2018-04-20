#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

int main() {
    int k, m, d;
    cin >> k >> m >> d;
    int d0 = d;
    int i = 1;
    int s = m + k * ((0 < ((d - 1) % 5)) - (((d - 1) % 5) < 0)) * ((0 < ((d - 1) % 6)) - (((d - 1) % 6) < 0)) - i;
    while (s >= 0) {
        ++d;
        ++i;
        s = m + k * ((0 < ((d - 1) % 5)) - (((d - 1) % 5) < 0)) * ((0 < ((d - 1) % 6)) - (((d - 1) % 6) < 0)) - i;
    }
    cout << d - d0 << endl;
    return 0;
}