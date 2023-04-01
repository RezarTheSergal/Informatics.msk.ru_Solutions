using System;

namespace Informatics
{
	class Program
	{
		static int GetSumOfDivisors(int number)
		{
			int temp = number;

			while (temp > 0)
			{
				int sum = 0;
				int counter = 0;
				for (int i = 1; i <= temp; i++)
				{
					if (temp % i == 0)
					{
						counter += 1;
						sum += i;
					}

				}
				if (sum - 1 != temp || counter != 2)
					return 0;

				temp /= 10;
			}

			return number;


		}
		static void Main()
		{

			int num = Convert.ToInt32(Console.ReadLine());

			Console.WriteLine(GetSumOfDivisors(num) == num ? "YES" : "NO");
		}
	}
}