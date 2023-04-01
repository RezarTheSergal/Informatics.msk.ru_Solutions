using System;

namespace Informatics
{
	class Program
	{
		static int GetSumOfDivisors(int a)
		{
			int sum = 0;

			for (int i = 1; i <= a; i++)
			{
				if (a % i == 0)
				{

					sum += i;
				}
			}
			return sum;


		}
		static void Main(string[] args)
		{
			string numStr = Console.ReadLine();
			int num = Convert.ToInt32(numStr.Split()[0]);
			int num2 = Convert.ToInt32(numStr.Split()[1]);

			Console.WriteLine(GetSumOfDivisors(num) == GetSumOfDivisors(num2) ? "YES" : "NO");
		}
	}
}