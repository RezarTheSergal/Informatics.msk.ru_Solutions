using System;

namespace Informatics
{
	class Program
	{
		static int GetSumOfDivisors(int a)
		{
			int sum = 0;

			for (int i = 1; i < a; i++)
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

			int num = Convert.ToInt32(Console.ReadLine());

			Console.WriteLine(GetSumOfDivisors(num) == num ? "YES" : "NO");
		}
	}
}