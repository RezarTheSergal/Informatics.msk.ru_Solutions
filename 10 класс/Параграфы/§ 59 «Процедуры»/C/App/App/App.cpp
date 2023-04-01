#include <iostream>

using namespace std;

void All_Digits(int number);

int main()
{
    int num = 0;

    cin >> num;
    All_Digits(num);
    return 0;
}

void All_Digits(int number)
{
    while (number > 0)
    {
        cout << number % 10 << endl;
        number /= 10;
    }

}