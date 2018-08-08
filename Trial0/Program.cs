using System;
using System.Collections.Generic;
using System.Linq;

namespace Trial0
{
    class Program
    {
        static void Main(string[] args)
        {
            var MyList = new List<string>() {"a", "b", "c", "d"};
            Console.WriteLine("Hello World!");

            MyList
                .Where((item) => item != "c")
                .Select((item) => item.ToUpper())
                .ToList()
                .ForEach(Console.WriteLine);
        }
    }
}
