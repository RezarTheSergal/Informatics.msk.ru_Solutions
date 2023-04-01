#include <cmath>
#include <iostream>

using namespace std;

void All_Digits(int number);
void Divisions(int number);

int main()
{
    int num = 0;

    cin >> num;
    Divisions(num);
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

void Divisions(int number)
{
    for (size_t i = 1; i <= number; i++)
    {
        if (((double)number / (double)i) == (double)(number / i))
        {
            // cout << ((double)number / (double)i) << " / " << (double)number / i << endl;
            cout << i << " ";
        }
    }
}