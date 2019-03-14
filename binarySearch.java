import java.util.*;

/**  search algorithm -> binary search	
 About bubblesort: speed O(log2n)
 @author unobatbayar
 Thanks to HackerRank's binary search tutorial
**/

class binarySearch{
    public static void main(String[] args){
        String title = "Welcome to Binary Search Algorithm! \n";
        print(title + "Enter sorted data set");
        String input = getString();
        String[] string_data = input.split("\\s+");

        int[] data = new int[string_data.length];
        for(int i = 0; i <string_data.length; i++){
            data[i] = Integer.parseInt(string_data[i]);
        }
        print("Enter the number we're searching for: ");
        int x = Integer.parseInt(getString());
        print("Did we find the number in the dataset? " + binarySearchIterative(data, x));
    }

    public static boolean binarySearchIterative(int[] data, int x){
        int left = 0;
        int right = data.length - 1;
        while(left < right){
            int mid = left + ((right - left)/2);
            if(data[mid] == x) return true;
            else if (x <data[mid]) right = mid = 1;
            else left = mid + 1;
        }
        return false;

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


