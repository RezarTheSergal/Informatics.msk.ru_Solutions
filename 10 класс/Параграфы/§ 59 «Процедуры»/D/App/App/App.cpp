#include <cmath>
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
    if (number == 0)
    {
        cout << 0;
        return;
    }
    int temp = number;
    int power = 0;

    while (temp > 0)
    {
        power += 1;
        temp /= 10;
    }

    while (number > 0 && power > 0)
    {
        cout << number / (int)pow(10, power - 1) % 10 << endl;
        power--;
    }

}