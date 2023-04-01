#include <iostream>

using namespace std;

int count_of_numbers(int number);

int main()
{
	int num;
	cin >> num;

	cout << count_of_numbers(num);

}

int count_of_numbers(int number)
{
	if (number == 0)
		return 1;


	int count = 0;
	while (number > 0)
	{
		number /= 10;
		count++;
	}

	return count;
}