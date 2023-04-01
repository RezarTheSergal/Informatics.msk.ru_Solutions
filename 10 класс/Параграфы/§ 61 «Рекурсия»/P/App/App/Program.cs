using System;

class Program
{
    static bool IsPowerOfTwo(double _num)
    {
        if (_num == 1)
        {
            return true;
        }

        if (_num % 2 != 0 || _num < 2)
        {
            return false;
        }

        if (_num > 1)
        {
            return IsPowerOfTwo(_num / 2);
        }

        return false;
    }
    static void Main()
    {
        long number = long.Parse(Console.ReadLine());

        Console.WriteLine(IsPowerOfTwo(number) ? "YES" : "NO");
    }
}