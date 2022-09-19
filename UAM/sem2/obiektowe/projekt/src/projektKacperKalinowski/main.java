package projektKacperKalinowski;

import java.io.PrintWriter;
import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class main {

    public static boolean chckPsl(String str){
        int[] waga={1,3,7,9,1,3,7,9,1,3};
        int wynik=0;
        
        for(int i=0;i<10;i++){
            wynik+=Integer.parseInt(str.substring(i,i+1))*waga[i];
        }
        
        int sprawdz=Integer.parseInt(str.substring(10,11));
        wynik%=10;
        wynik=10-wynik;
        wynik%=10;
        
        if(wynik==sprawdz)
            return true;
        else
            return false;
    }

    public static boolean liczby(String x)
    {
        for (int i = 0; i < 11; i++) {
            if (!Character.isDigit(x.charAt(i))) {
                return false;
            }
        }
        return true;
    }
    public static void main (String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        String pesel;
        String[] pesele = new String[100];
        String imieInazwisko;
        String[] imionaInazwiska = new String[100];
        String miejscowosc;
        String[] miejscowosci = new String[100];
        String ifexit = "";
        int i = 0;
        int a = 0;

        File file = new File("plik.txt");
        boolean czyUtworzony = file.createNewFile();
        if(czyUtworzony) {
            do {
                System.out.println("Podaj pesel: ");
                pesel = scan.nextLine();
                for (int j = 0; j < i; j++)
                    if (pesel.equals(pesele[j])) {
                        a = j;
                        i -= 1;
                    }
                System.out.println("Podaj imie i nazwisko: ");
                imieInazwisko = scan.nextLine();
                System.out.println("Podaj miejsce zamieszkania: ");
                miejscowosc = scan.nextLine();
                if (pesel.length() == 11) {
                    if (liczby(pesel)) {
                        if (chckPsl(pesel)) {
                            pesele[a] = pesel;
                            imionaInazwiska[a] = imieInazwisko;
                            miejscowosci[a] = miejscowosc;
                            System.out.println("Jesli chcesz zakonczyc wpisz: Exit. Jesli nie to nacisnij enter i kontynuuj.");
                            ifexit = scan.nextLine();
                        } else {
                            System.out.println("Niepoprawny pesel, podaj dane jeszcze raz");
                            i -= 1;
                            System.out.println("Jesli chcesz zakonczyc wpisz: Exit. Jesli nie to nacisnij enter i kontynuuj.");
                            ifexit = scan.nextLine();
                        }
                    } else {
                        System.out.println("Niepoprawny pesel, podaj dane jeszcze raz");
                        i -= 1;
                        System.out.println("Jesli chcesz zakonczyc wpisz: Exit. Jesli nie to nacisnij enter i kontynuuj.");
                        ifexit = scan.nextLine();
                    }
                } else {
                    System.out.println("Niepoprawny pesel, podaj dane jeszcze raz");
                    i -= 1;
                    System.out.println("Jesli chcesz zakonczyc wpisz: Exit. Jesli nie to nacisnij enter i kontynuuj.");
                    ifexit = scan.nextLine();
                }
                i += 1;
                a = i;
            } while ((!ifexit.equals("Exit")) && (!ifexit.equals("exit")));

            PrintWriter writer = new PrintWriter(file);
            for (int j = 0; j < i; j++) {
                writer.println(pesele[j] + "  " + imionaInazwiska[j] + "  " + miejscowosci[j]) ;
            }
            writer.close();
        }
        else
            System.out.println("Nie udalo sie utworzyc pliku");
    }
}
