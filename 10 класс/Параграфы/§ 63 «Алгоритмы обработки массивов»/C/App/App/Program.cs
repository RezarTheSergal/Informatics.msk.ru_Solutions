using System;

namespace Informatics
{
    class Program
    {
        static void PrintMaxNumbersAndCounter()
        {
            int number = int.Parse(Console.ReadLine());

            int[] data = new int[number];

            string[] help_data = Console.ReadLine().Split();

            int counter = 1;
            int max = int.MinValue;
            for (int i = 0; i < help_data.Length; i++)
            {
                data[i] = int.Parse(help_data[i]);
                if (data[i] > max)
                {
                    max = data[i];
                    counter = 1;
                }
                else if (data[i] == max)
                {
                    counter += 1;
                }
            }

            Console.WriteLine(max + " " + counter);
        }

        static void Main()
        {
            PrintMaxNumbersAndCounter();
        }

    }
}