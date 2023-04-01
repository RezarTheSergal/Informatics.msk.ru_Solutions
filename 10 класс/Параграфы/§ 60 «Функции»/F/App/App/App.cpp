#include <iostream>

using namespace std;

void reverse_number(int number);

int main()
{
	int num;
	cin >> num;
	reverse_number(num);

}

void reverse_number(int number)
{
	cout << number % 10;
	number /= 10;

	if (number > 0)
	{
		reverse_number(number);
	}
	else
	{
		return;
	}

}