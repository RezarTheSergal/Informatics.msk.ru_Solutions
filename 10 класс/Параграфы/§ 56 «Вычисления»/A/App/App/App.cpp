#include <iostream>

using namespace std;

int main()
{
	int FirstNum, SecondNum, ThirdNum;

	cin >> FirstNum >> SecondNum >> ThirdNum;

	int Sum = FirstNum + SecondNum + ThirdNum;

	cout << FirstNum << "+" << SecondNum << "+" << ThirdNum << "=" << Sum << endl;
	cout << FirstNum << "*" << SecondNum << "*" << ThirdNum << "=" << FirstNum * SecondNum * ThirdNum << endl;
	cout << "(" << FirstNum << "+" << SecondNum << "+" << ThirdNum << ")/3" << "=";

	cout.setf(ios::fixed);
	cout.precision(3);
	cout << (double)Sum / 3 << endl;

	return 0;
}