#include <iostream>
#include <iomanip>

using namespace std;

int GetMinNimber(int a, int b);
int GetMaxNimber(int a, int b);

int main()
{
	int first_num, second_num, third_num, forth_num, fifth_num, sum;
	cin >> first_num >> second_num >> third_num >> forth_num >> fifth_num;

	sum = first_num + second_num + third_num + forth_num + fifth_num;

	int min_num = GetMinNimber(first_num, GetMinNimber(second_num, GetMinNimber(third_num, GetMinNimber(forth_num, fifth_num))));
	sum -= min_num;

	int max_num = GetMaxNimber(first_num, GetMaxNimber(second_num, GetMaxNimber(third_num, GetMaxNimber(forth_num, fifth_num))));
	sum -= max_num;

	cout << min_num << " " << max_num << endl;


	cout << fixed << setprecision(2) << (double)sum / 3;
}

int GetMinNimber(int a, int b)
{
	return(a < b ? a : b);
}

int GetMaxNimber(int a, int b)
{
	return(a < b ? b : a);
}