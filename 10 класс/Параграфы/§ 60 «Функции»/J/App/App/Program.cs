using System;
using System.Collections.Generic;

namespace Informatics
{
    class Program
    {
        static IEnumerable<int> StaysTheSame(int diapStart, int diapEnd)
        {

            for (int i = diapStart; i <= diapEnd; i++)
            {
                int counter = 0;

                for (int j = 2; j < 10; j++)
                {
                    if (SumOfDigets(i * j) == SumOfDigets(i))
                    {
                        counter += 1;

                        if (counter >= 8)
                        {
                            yield return i;
                        }
                    }
                }
            }


        }
        static int SumOfDigets(int defaultNumber)
        {
            int sum = 0;

            while (defaultNumber > 0)
            {
                sum += defaultNumber % 10;
                defaultNumber /= 10;
            }
            return sum;
        }

        static void Main(string[] args)
        {
            string numStr = Console.ReadLine();
            int num = Convert.ToInt32(numStr.Split()[0]);
            int num2 = Convert.ToInt32(numStr.Split()[1]);

            foreach (var number in StaysTheSame(num, num2))
            {
                Console.Write($"{number} ");
            }

        }
    }
}