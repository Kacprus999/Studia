package pierwszy;


public class MyThirdJavaApplication {

    public static void main(String[] args) {
        Person person1 = new Person(); // tworzymy obiekt
        person1.forename = "Jan"; // przypisujemy polu imi� warto��
        person1.surname = "Kowalski";
        person1.age = 35;
        person1.introduceYourself(); // wywo�ujemy metod�
        person1.growOld(5); // metoda z parametrem
        person1.introduceYourself(); // jeszcze raz si� przedstawiamy z innym wiekiem
    }

}