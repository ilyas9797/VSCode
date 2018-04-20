#include <iostream>
using namespace std;

static int c = 0;

int foo(int n) {
    if (n <= 0)
        return 1;
    c += 2;
    return foo((n * 2) / 3) + foo(n - 2);
}

int main() {
    c++;
    foo(3);
    cout << c << endl;
    return 0;
}