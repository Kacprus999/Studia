package pierwszy;

import java.util.Scanner;

/*
	public class MyFirstJavaApplication {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Proszê podaj swoje imiê:");
        String forename = scanner.nextLine();

        System.out.println("Proszê podaj swoje nazwisko:");
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

        System.out.println(x == y); // czy x jest równe y
        System.out.println(x != y); // czy x jest ró¿ne od y

        System.out.println(x > y); // czy x jest wiêksze od y
        System.out.println(x >= y); // czy x jest wiêksze lub równe y

        System.out.println(x < y); // czy x jest mniejsze od y
        System.out.println(x <= y); // czy x jest mniejsze lub równe y
        
        x = 10;
        y = 5;

        if(x > y){
            System.out.println("x jest wiêksze od y");
        }
        
        if(x > y){
            System.out.println("x jest wiêksze od y");
        } else if (x < y) {
            System.out.println("x jest mniejsze od y");
        } else {
            System.out.println("x jest równe y");
        }
        
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Podaj proszê liczbê wiêksz¹ od 100:");
        var number = scanner.nextDouble();

        while (number <= 100) {
            System.out.println("Liczba nie jest wiêksza od 100, podaj jeszcze raz:");
            number = scanner.nextDouble();
        }

        scanner.close();

        System.out.println("Dziêkujê! Poda³eœ liczbê: " + number);
    
        Scanner scanner1 = new Scanner(System.in);

        double number1;
        do {
            System.out.println("Podaj proszê liczbê wiêksz¹ od 100:");
            number1 = scanner1.nextDouble();
        } while (number1 <= 100);

        scanner1.close();

        System.out.println("Dziêkujê! Poda³eœ liczbê: " + number1);
     
        
        var i = 1;
        while (i <= 10) {
        	System.out.println(i++);
        }
    
        for (var j = 1; j <= 10; j++) {
            System.out.println(j);
        }
    
    }
}