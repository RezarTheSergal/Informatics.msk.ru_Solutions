using System;

namespace Informatics
{

    class Program
    {
        static int EvenCounter(int _number)
        {
            if (_number < 1)
            {
                return 0;
            }

            int test = EvenCounter(_number / 10);

            if (_number % 10 > test)
            {

                return _number % 10;

            }
            else
            {
                return test;
            }


        }

        static void Main()
        {
            Console.WriteLine(EvenCounter(int.Parse(Console.ReadLine())));

        }

    }
}