#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int FirstPerson, SecondPerson, ThirdPerson;

	cin >> FirstPerson >> SecondPerson >> ThirdPerson;

	if (FirstPerson == SecondPerson && SecondPerson == ThirdPerson)
	{
		cout << 0;
		return 0;
	}
	else if (FirstPerson == SecondPerson && ThirdPerson < FirstPerson)
	{
		cout << "A B";
		return 0;
	}
	else if (FirstPerson == ThirdPerson && SecondPerson < FirstPerson)
	{
		cout << "A C";
		return 0;
	}
	else if (SecondPerson == ThirdPerson && ThirdPerson > FirstPerson)
	{
		cout << "B C";
		return 0;
	}

	if (FirstPerson > SecondPerson)
	{
		if (FirstPerson > ThirdPerson)
		{
			cout << "A";
			return 0;
		}
		else
		{
			cout << "C";
			return 0;
		}
	}
	else if (FirstPerson > ThirdPerson)
	{
		if (FirstPerson > SecondPerson)
		{
			cout << "A";
			return 0;
		}
		else
		{
			cout << "B";
			return 0;
		}
	}
	else
	{
		if (ThirdPerson > SecondPerson)
		{
			cout << "C";
			return 0;
		}
		else
		{
			cout << "B";
			return 0;
		}
	}
}