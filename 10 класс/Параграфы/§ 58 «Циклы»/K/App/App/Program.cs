using System;
using System.Collections.Generic;
using System.Linq;

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

            if (_number % 10 % 2 == 0)
            {

                return 1 + EvenCounter(_number / 10);

            }

            return EvenCounter(_number / 10);

        }

        static void Main()
        {
            Console.WriteLine(EvenCounter(int.Parse(Console.ReadLine())));

        }

    }
}