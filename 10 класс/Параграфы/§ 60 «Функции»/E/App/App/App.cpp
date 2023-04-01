#include <iostream>

using namespace std;

int GetNOD(int a, int b);
int GetNOK(int a, int b);

int main()
{
	int first_num, second_num;
	cin >> first_num >> second_num;
	cout << GetNOK(first_num, second_num);

}

int GetNOD(int a, int b)
{
	if (a % b == 0)
		return b;
	if (b % a == 0)
		return a;
	if (a > b)
		return GetNOD(a % b, b);
	return GetNOD(a, b % a);
}

int GetNOK(int a, int b)
{
	return a / GetNOD(a, b) * b;
}