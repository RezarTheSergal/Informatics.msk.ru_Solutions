using System;

namespace Informatics
{
    class Program
    {
        static int EqualNumbersCounter()
        {
            int number = int.Parse(Console.ReadLine());

            int[] data = new int[number];
            string[] help_data = Console.ReadLine().Split();

            int find_x = int.Parse(Console.ReadLine());

            int counter = 0;
            for (int i = 0; i < help_data.Length; i++)
            {
                data[i] = int.Parse(help_data[i]);
                if (data[i] == find_x)
                {
                    counter += 1;
                }
            }

            return counter;
        }

        static void Main()
        {


            Console.WriteLine(EqualNumbersCounter());
        }

    }
}