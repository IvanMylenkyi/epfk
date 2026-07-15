while (true)
{
    Console.WriteLine("\nMenu:");
    Console.WriteLine("1. Show numbers from 1 to 100.");
    Console.WriteLine("2. Show only even numbers from 1 to 50.");
    Console.WriteLine("3. Enter 10 numbers and calculate their sum.");
    Console.WriteLine("4. Enter numbers until 0 is entered, and calculate the average.");
    Console.WriteLine("5. Show the multiplication table for a number.");
    Console.WriteLine("0. Exit.");

    string choice = Console.ReadLine();

    if (choice == "0") break;

    switch (choice)
    {
        case "1":
            for (int i = 1; i <= 100; i++)
            {
                Console.Write(i + " ");
            }
            Console.WriteLine();
            break;

        case "2":
            for (int i = 2; i <= 50; i += 2)
            {
                Console.Write(i + " ");
            }
            Console.WriteLine();
            break;

        case "3":
            int sum = 0;
            for (int i = 0; i < 10; i++)
            {
                sum += Convert.ToInt32(Console.ReadLine());
            }
            Console.WriteLine("Sum: " + sum);
            break;

        case "4":
            int input;
            int totalSum = 0;
            int count = 0;

            while (true)
            {
                input = Convert.ToInt32(Console.ReadLine());
                if (input == 0) break;

                totalSum += input;
                count++;
            }

            if (count > 0)
            {
                double average = (double)totalSum / count;
                Console.WriteLine("Average: " + average);
            }
            break;

        case "5":
            int number = Convert.ToInt32(Console.ReadLine());

            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine($"{number} * {i} = {number * i}");
            }
            break;
    }
}