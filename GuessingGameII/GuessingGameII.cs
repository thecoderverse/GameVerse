using System;
using System.IO;

class GuessingGameII {
    
    public static string readSettings()
    {
        if(File.Exists("settings.dat"))
        {
            string[] settingLines=File.ReadAllLines("settings.dat");
            if (settingLines.Length>0) return settingLines[0].Split(":")[1];
            else return "1-100";
        }
        else 
        {
            using (StreamWriter writer = new StreamWriter("settings.dat"))
            {
                writer.WriteLine("numberRange:1-100");
            }
            return "1-100";
        }
    }
    
    public static string writeSettings(int min, int max)
    {
        if(File.Exists("settings.dat"))
        {
            using (StreamWriter writer = new StreamWriter("settings.dat"))
            {
                writer.WriteLine($"numberRange:{min}-{max}");
            }
        }
        else
        {
            using (StreamWriter writer = new StreamWriter("settings.dat"))
            {
                writer.WriteLine($"numberRange:{min}-{max}");
            }
        }
        return "Saved";
    }
    
    public static void playAgain()
    {
        Console.Write("Would you like to play again? [Y]es / [N]o / [M]ain Menu > ");
        string a=Console.ReadLine().ToLower();
        if (a=="y") game();
        else if (a=="m") start();
        else Console.WriteLine("Thank you!");
    }
    
    public static void drawTitle()
    {
        Random rnd=new Random();
        Console.WriteLine(new string('_',25));
        Console.WriteLine("");
        for(int i=0;i<15;i++) Console.Write(rnd.Next(0,9)+" ");
        Console.WriteLine("");
        Console.WriteLine("       Guessing Game");
        for(int i=0;i<15;i++) Console.Write(rnd.Next(0,9)+" ");
        Console.WriteLine("");
    }
    
    public static string drawMainMenu()
    {
        drawTitle();
        Console.WriteLine("");
        Console.WriteLine("1 - Play Game");
        Console.WriteLine("2 - Settings");
        Console.WriteLine("3 - Exit");
        Console.WriteLine("");
        Console.Write("Select > ");
        string a=Console.ReadLine();
        return a;
    }
    
    public static void drawSettingMenu()
    {
        drawTitle();
        int min,max;
        Console.WriteLine("");
        Console.WriteLine("Please enter guess range");
        Console.Write("Min:");
        while(!int.TryParse(Console.ReadLine(), out min))
        {
            Console.WriteLine("This is not valid input. Please enter a number:");
            Console.Write("Min:");
        }
        do
        {
            Console.Write("Max:");
            while(!int.TryParse(Console.ReadLine(), out max))
            {
                Console.WriteLine("This is not valid input. Please enter a number:");
                Console.Write("Max:");
            }
            if(max<min) Console.WriteLine($"The maximum number must be greater than the {min}");
        }while(max<min);
        
        string a=writeSettings(min,max);
        Console.WriteLine(a);
        Console.Write("Please press to enter go to the main menu");
        Console.ReadLine();
        
        start();
    }
    
    public static void game()
    {
        Random rnd = new Random();
        string numberRange=readSettings();
        int min=Convert.ToInt32(numberRange.Split("-")[0]);
        int max=Convert.ToInt32(numberRange.Split("-")[1]);
        
        while(true)
        {
            int guessNumber = rnd.Next(min,max);
            Console.Write($"Could the number you have in mind be {guessNumber} ? [Y]es / Try [B]ig / Try [S]mall  > ");
            string a=Console.ReadLine().ToLower();
            if (a.ToLower()=="y")
            {
                Console.WriteLine("Eureka!!! =)");
                break;
            }
            else if (a.ToLower()=="b") 
                min=guessNumber+1;
            else if(a.ToLower()=="s")
                max=guessNumber-1;
            else 
                Console.WriteLine("I'm waiting for you to give me a clue.");
            
            if(min==max) 
            {
                Console.WriteLine("I think you're cheating. This game ends here.");
                break;
            }
        }
        playAgain();
    }
    
    public static void start()
    {
        string a=drawMainMenu();
        if (a=="1") game();
        else if(a=="2") drawSettingMenu();
        else Console.WriteLine("Good Bye!");
    }
    
    static void Main() {
        start();
  }
}
