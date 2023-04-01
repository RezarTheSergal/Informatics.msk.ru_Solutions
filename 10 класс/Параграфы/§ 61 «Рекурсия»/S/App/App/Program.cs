using System;

namespace Informatics
{

    class Program
    {
        static int Max(int _max, int number, int i)
        {
            if (number != 0)
            {
                number = Convert.ToInt32(Console.ReadLine());
                if (number != 0) _max = _max < number ? number : _max;

                return Max(_max, number, i += 1);
            }
            else
            {
                if (i == 1 && number == 0) return 0;

                return _max;
            }
        }

        static void Main()
        {
            Console.WriteLine(Max(int.MinValue, int.MinValue, 0));

        }

    }
}