package pierwszy;

import static java.lang.System.out;

public class Person {

    /**
     * Trzy pola naszej klasy
     */
    public String forename;
    public String surname;
    public int age;

    /**
     * Metoda przedstaw si� wy�wietlaj�ca w konsoli napis
     */
    public void introduceYourself() {
        System.out.println("Nazywam si� " + forename + " " + surname + ". Mam " + age + " lat.");
    }
    public int growOld(int years) {
        age += years;
        return age;
    }
    public Person() {

    }
    public Person(String initForename, String initSurname, int initAge) {
        forename = initForename;
        surname = initSurname;
        age = initAge;
    }

}