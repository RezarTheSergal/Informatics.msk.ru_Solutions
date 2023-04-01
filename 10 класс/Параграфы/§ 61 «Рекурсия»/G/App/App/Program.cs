using System;

namespace Informatics
{

    class Program
    {
        static int EvenCounter(int _number)
        {
            if (_number / 10 < 1)
            {
                return _number;
            }

            return _number % 10 + EvenCounter(_number / 10);

        }

        static void Main()
        {
            Console.WriteLine(EvenCounter(int.Parse(Console.ReadLine())));

        }

    }
}