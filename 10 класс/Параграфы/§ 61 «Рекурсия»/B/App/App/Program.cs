using System;
using System.Linq;
namespace Informatics
{
    class Program
    {
        static void Translate(int _decimal, int _system)
        {
            if (_decimal == 0)
            {
                Console.WriteLine(0);
                return;
            }

            if (_decimal < 0)
            {
                _decimal = -_decimal;
                Console.Write('-');
            }

            int counter = 0;
            int temp = _decimal;
            while (temp > 0)
            {
                counter += 1;
                temp /= _system;
            }

            int[] answer = new int[counter];
            for (int i = 0; i < counter; i++)
            {
                answer[i] = _decimal % _system == 0 ? 0 : _decimal % _system;
                _decimal /= _system;
            }

            PrintReversed(answer);
        }
        static void PrintReversed(int[] array)
        {
            for (int i = array.Length - 1; i >= 0; i--)
            {
                Console.Write(array[i]);
            }
        }
        static void Main()
        {
            Translate(Convert.ToInt32(Console.ReadLine()), 8);
        }
    }
}