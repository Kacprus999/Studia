package pierwszy;

import java.util.Scanner;

/*
	public class MyFirstJavaApplication {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Prosz� podaj swoje imi�:");
        String forename = scanner.nextLine();

        System.out.println("Prosz� podaj swoje nazwisko:");
        String surname = scanner.nextLine();

        scanner.close();

        System.out.println("Witaj " + forename + " " + surname);
    }

}
*/
public class MyFirstJavaApplication {

    public static void main(String[] args) {

        double x = 10;
        double y = 2;

        var result = x + y;
        System.out.println(result);
        result = x - y;
        System.out.println(result);
        result = x * y;
        System.out.println(result);
        result = x / y;
        System.out.println(result);
        result = x % y;
        System.out.println(result);

        x = x + y;
        System.out.println(x);
        x = x - y;
        System.out.println(x);
        x = x * y;
        System.out.println(x);
        x = x / y;
        System.out.println(x);
 
        x += y;
        System.out.println(x);
        x -= y;
        System.out.println(x);
        x *= y;
        System.out.println(x);
        x /= y;
        System.out.println(x);
      
        x = 10;
        System.out.println(x);
        x++;
        System.out.println(x);
        x--;
        System.out.println(x);
        
        x = 10;
        System.out.println(x);
        System.out.println(x++);
        System.out.println(x--);
        System.out.println(x);
        
        x = 10;
        System.out.println(x);
        System.out.println(++x);
        System.out.println(--x);
        System.out.println(x);
        
        x = 10;
        y = 5;

        System.out.println(x == y); // czy x jest r�wne y
        System.out.println(x != y); // czy x jest r�ne od y

        System.out.println(x > y); // czy x jest wi�ksze od y
        System.out.println(x >= y); // czy x jest wi�ksze lub r�wne y

        System.out.println(x < y); // czy x jest mniejsze od y
        System.out.println(x <= y); // czy x jest mniejsze lub r�wne y
        
        x = 10;
        y = 5;

        if(x > y){
            System.out.println("x jest wi�ksze od y");
        }
        
        if(x > y){
            System.out.println("x jest wi�ksze od y");
        } else if (x < y) {
            System.out.println("x jest mniejsze od y");
        } else {
            System.out.println("x jest r�wne y");
        }
        
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Podaj prosz� liczb� wi�ksz� od 100:");
        var number = scanner.nextDouble();

        while (number <= 100) {
            System.out.println("Liczba nie jest wi�ksza od 100, podaj jeszcze raz:");
            number = scanner.nextDouble();
        }

        scanner.close();

        System.out.println("Dzi�kuj�! Poda�e� liczb�: " + number);
    
        Scanner scanner1 = new Scanner(System.in);

        double number1;
        do {
            System.out.println("Podaj prosz� liczb� wi�ksz� od 100:");
            number1 = scanner1.nextDouble();
        } while (number1 <= 100);

        scanner1.close();

        System.out.println("Dzi�kuj�! Poda�e� liczb�: " + number1);
     
        
        var i = 1;
        while (i <= 10) {
        	System.out.println(i++);
        }
    
        for (var j = 1; j <= 10; j++) {
            System.out.println(j);
        }
    
    }
}