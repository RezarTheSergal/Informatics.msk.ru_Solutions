#define _USE_MATH_DEFINES
#include <iostream>
#include <math.h>


using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");

	int Radius;
	cin >> Radius;

	cout.setf(ios::fixed);
	cout.precision(3);
	cout << M_PI * pow(Radius, 2) << endl;
	cout << 2 * M_PI * Radius << endl;

	return 0;
}