using System;

class Program
{
    static bool IsSimple(long _num, int itterator = 2)
    {
        if (_num < Math.Pow(itterator, 2))
        {
            return true;
        }
        if ((double)_num / itterator == _num / itterator)
        {
            return false;
        }
        return IsSimple(_num, itterator + 1);
    }
    static void Main()
    {
        long number = long.Parse(Console.ReadLine());

        Console.WriteLine(IsSimple(number) ? "YES" : "NO");
    }
}