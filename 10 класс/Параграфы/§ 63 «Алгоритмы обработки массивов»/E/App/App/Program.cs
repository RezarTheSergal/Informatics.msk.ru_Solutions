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
            int max = int.MinValue;
            for (int i = 0; i < help_data.Length; i++)
            {
                data[i] = int.Parse(help_data[i]);
                if (data[i] > 0 && data[i] % 2 == 0)
                {
                    if (data[i] < min)
                    {
                        min = data[i];
                    }
                    else if (data[i] > max)
                    {
                        max = data[i];
                    }
                }

            }

            if (min == int.MaxValue && max == int.MinValue) { Console.WriteLine("-1 -1"); }
            else { Console.WriteLine(min + " " + max); }

        }

        static void Main()
        {
            PrintMaxNumbersAndCounter();
        }

    }
}