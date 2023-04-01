using System;

namespace Informatics
{
    class Program
    {
        static string HexTranslator(int _digit)
        {

            if (_digit == 35)
            {
                return "Z";
            }
            else if (_digit == 34)
            {
                return "Y";
            }
            else if (_digit == 33)
            {
                return "X";
            }
            else if (_digit == 32)
            {
                return "W";
            }
            else if (_digit == 31)
            {
                return "V";
            }
            else if (_digit == 30)
            {
                return "U";
            }
            else if (_digit == 29)
            {
                return "T";
            }
            else if (_digit == 28)
            {
                return "S";
            }
            else if (_digit == 27)
            {
                return "R";
            }
            else if (_digit == 26)
            {
                return "Q";
            }
            else if (_digit == 25)
            {
                return "P";
            }
            else if (_digit == 24)
            {
                return "O";
            }
            else if (_digit == 23)
            {
                return "N";
            }
            else if (_digit == 22)
            {
                return "M";
            }
            else if (_digit == 21)
            {
                return "L";
            }
            else if (_digit == 20)
            {
                return "K";
            }
            else if (_digit == 19)
            {
                return "G";
            }
            else if (_digit == 18)
            {
                return "I";
            }
            else if (_digit == 17)
            {
                return "H";
            }
            else if (_digit == 16)
            {
                return "G";
            }
            else if (_digit == 15)
            {
                return "F";
            }
            else if (_digit == 14)
            {
                return "E";
            }
            else if (_digit == 13)
            {
                return "D";
            }
            else if (_digit == 12)
            {
                return "C";
            }
            else if (_digit == 11)
            {
                return "B";
            }
            else if (_digit == 10)
            {
                return "A";
            }
            else
            {
                return _digit.ToString();
            }
        }
        static void Translate(long _decimal, int _system)
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
            long temp = _decimal;
            while (temp > 0)
            {
                counter += 1;
                temp /= _system;
            }

            int[] answer = new int[counter];
            for (int i = 0; i < counter; i++)
            {
                answer[i] = (int)(_decimal % _system == 0 ? 0 : _decimal % _system);
                _decimal /= _system;
            }

            PrintReversed(answer);
        }
        static void PrintReversed(int[] array)
        {
            for (int i = array.Length - 1; i >= 0; i--)
            {
                Console.Write(HexTranslator(array[i]));
            }
        }
        static void Main()
        {
            string queue = Console.ReadLine();
            long first_value = Convert.ToInt64(queue.Split()[0]);
            int second_value = Convert.ToInt32(queue.Split()[1]);

            Translate(first_value, second_value);
        }
    }
}