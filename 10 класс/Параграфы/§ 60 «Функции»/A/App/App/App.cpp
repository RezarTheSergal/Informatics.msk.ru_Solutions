#include <iostream>

using namespace std;

int GetMinNimber(int a, int b);

int main()
{
	int first_num, second_num, third_num;
	cin >> first_num >> second_num >> third_num;
	cout << GetMinNimber(first_num, GetMinNimber(second_num, third_num));
}

int GetMinNimber(int a, int b)
{
	return(a < b ? a : b);
}