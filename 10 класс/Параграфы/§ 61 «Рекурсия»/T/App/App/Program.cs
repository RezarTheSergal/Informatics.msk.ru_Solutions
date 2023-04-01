using System;
using System.Linq;
using System.Collections.Generic;

namespace Informatics
{
    class Program
    {
        static int MaxCount(List<int> array, int i = 0, int _max = int.MinValue, int number = int.MinValue)
        {
            if (number != 0)
            {
                number = Convert.ToInt32(Console.ReadLine());
                if (number != 0) _max = _max < number ? number : _max;
                array.Add(number);
                return MaxCount(array, i += 1, _max, number);
            }
            else
            {
                if (i == 1 && number == 0) return 0;

                return array.Where(n => n == _max).Count(); ;
            }
        }

        static void Main()
        {
            Console.WriteLine(MaxCount(new List<int>()));

        }

    }
}