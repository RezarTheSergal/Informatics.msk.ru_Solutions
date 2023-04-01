#include <iostream>


using namespace std;

int main()
{
	float Number;
	cin >> Number;

	float SaveNum;

	Number *= Number;
	SaveNum = Number;
	Number *= Number;
	Number *= Number;
	Number *= SaveNum;

	cout.setf(ios::fixed);
	cout.precision(3);
	cout << Number << endl;

	return 0;
}
