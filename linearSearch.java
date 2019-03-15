import java.util.*;

/**  search algorithm -> linear search	
 About linear search: Worst-case performance O(n)
Best-case performanceO(1)
Average performance	O(n)
Worst-case space complexity	O(1) iterative
@author unobatbayar
**/

class linearSearch{
    public static void main(String[] args){
        String title = "Welcome to Linear Search Algorithm! \n";
        print(title + "Enter data set");
        String input = getString();
        String[] string_data = input.split("\\s+");

        int[] data = new int[string_data.length];
        for(int i = 0; i <string_data.length; i++){
            data[i] = Integer.parseInt(string_data[i]);
        }
        print("Enter the number we're searching for: ");
        int x = Integer.parseInt(getString());
        int[] result = simpleLinearSearch(data, x);
        int total_searches = result[1];
        String found = "no.";
        if(result[0] == 1) found = "yes";
        print("Found: " + found + 
        "\n Total search: " + total_searches + " Data set: "+ data.length);
    }

    public static int[] simpleLinearSearch(int[] data, int x){
        int[] output = {0, 0};
        for(int i = 0; i <data.length; i++){
            output[1] = i;
            if(data[i] == x){
                output[0] = 1;
                break;
            }
        }
        //because int i started from 0, we add to see true value
        output[1]++;
        return output;
    }

    public static void print(String message){
        System.out.println(message);
    }

    public static String getString()
    {
        Scanner scanner = new Scanner(System.in);  
        return scanner.nextLine();  
    }
}


