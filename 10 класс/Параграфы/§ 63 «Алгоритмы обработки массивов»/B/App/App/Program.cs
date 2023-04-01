using System;

namespace Informatics
{
    class Program
    {
        static void PrintEqualNumbersIndex()
        {
            int number = int.Parse(Console.ReadLine());

            int[] data = new int[number];

            string[] help_data = Console.ReadLine().Split();

            int find_x = int.Parse(Console.ReadLine());

            bool flag = true;
            for (int i = 0; i < help_data.Length; i++)
            {
                data[i] = int.Parse(help_data[i]);
                if (data[i] == find_x)
                {
                    flag = false;
                    Console.Write(i + 1 + " ");
                }
            }

            if (flag)
                Console.WriteLine(-1);

        }

        static void Main()
        {
            PrintEqualNumbersIndex();
        }

    }
}