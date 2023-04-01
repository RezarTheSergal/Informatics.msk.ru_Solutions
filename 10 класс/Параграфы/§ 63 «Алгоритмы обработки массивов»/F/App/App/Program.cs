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

            int index = -1;
            int shuffle;

            for (int i = 0; i < number; i++)
            {
                data[i] = int.Parse(help_data[i]);
            }

            for (int j = 0; j < number; j++)
            {
                int min = int.MaxValue;
                for (int i = j; i < number; i++)
                {
                    if (data[i] < min)
                    {
                        min = data[i];
                        index = i;
                    }
                }

                shuffle = data[j];
                data[j] = data[index];
                data[index] = shuffle;

            }

            for (int i = 0; i < 3; i++)
            {
                Console.Write(data[i] + " ");
            }

        }

        static void Main()
        {
            PrintMaxNumbersAndCounter();
        }

    }
}