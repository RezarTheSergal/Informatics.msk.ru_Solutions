#include <iostream>

using namespace std;

string DrawALine(int length);

int main()
{
    int length = 0;

    cin >> length;
    cout << DrawALine(length);
    return 0;
}

string DrawALine(int length)
{
    string line = "";

    for (size_t i = 0; i < length; i++)
    {
        for (size_t i = 0; i < length; i++)
        {
            line += "*";
        }

        line += "\n";
    }
    return line;
}