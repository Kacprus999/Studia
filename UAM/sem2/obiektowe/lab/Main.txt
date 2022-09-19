package com.company;

import java.io.PrintWriter;
import java.util.Scanner;
import java.io.File;
import java.io.IOException;
public class Main {

    public static boolean checkPesel(String str){
        int[] wagi={1,3,7,9,1,3,7,9,1,3};
        int suma=0;
        for(int i=0;i<10;i++){
            suma += Integer.parseInt(str.substring(i,i+1))*wagi[i];
        }
        int kontrolna=Integer.parseInt(str.substring(10,11));
        suma %=10;
        suma=10-suma;
        suma%=10;
        if(suma==kontrolna)
            return true;
        else
            return false;
    }

    public static boolean onlyDigits(String str)
    {
        for (int i = 0; i < 11; i++) {
            if (!Character.isDigit(str.charAt(i))) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args)throws IOException {
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
                System.out.println("Podaj imię i nazwisko: ");
                imieInazwisko = scan.nextLine();
                System.out.println("Podaj miejscowość: ");
                miejscowosc = scan.nextLine();
                if (pesel.length() == 11) {
                    if (onlyDigits(pesel)) {
                        if (checkPesel(pesel)) {
                            pesele[a] = pesel;
                            imionaInazwiska[a] = imieInazwisko;
                            miejscowosci[a] = miejscowosc;
                            System.out.println("Jeśli chcesz zakończyć wpisywanie danych, wpisz : Exit ");
                            ifexit = scan.nextLine();
                        } else {
                            System.out.println("Podałeś zły pesel, prosze podać dane jeszcze raz");
                            i -= 1;
                            System.out.println("Jeśli chcesz zakończyć wpisywanie danych, wpisz : Exit ");
                            ifexit = scan.nextLine();
                        }
                    } else {
                        System.out.println("Podałeś zły pesel, prosze podać dane jeszcze raz");
                        i -= 1;
                        System.out.println("Jeśli chcesz zakończyć wpisywanie danych, wpisz : Exit ");
                        ifexit = scan.nextLine();
                    }
                } else {
                    System.out.println("Podałeś zły pesel, prosze podać dane jeszcze raz");
                    i -= 1;
                    System.out.println("Jeśli chcesz zakończyć wpisywanie danych, wpisz : Exit ");
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
