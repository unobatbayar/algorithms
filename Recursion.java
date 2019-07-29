/*
Recusion algorithm, simplified
@author unobatbayar
*/
class Recursion {
    public static void main (String[] p) { 
        int test = 4;
        System.out.println(fact(test)); //prints 24

    }
    static int fact(int n ){
        if(n == 1) return 1;
        return n*fact(n-1);
    }
}