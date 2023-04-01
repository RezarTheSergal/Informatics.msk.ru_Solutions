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

            int min = int.MaxValue;
            for (int i = 0; i < help_data.Length; i++)
            {
                data[i] = int.Parse(help_data[i]);
                if (data[i] < min)
                {
                    min = data[i];
                }
            }

            for (int i = 0; i < data.Length; i++)
            {
                if (data[i] == min)
                {
                    Console.Write(i + 1 + " ");
                }
            }

        }

        static void Main()
        {
            PrintMaxNumbersAndCounter();
        }

    }
}