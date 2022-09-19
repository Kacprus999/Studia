package pierwszy;


public class MyThirdJavaApplication {

    public static void main(String[] args) {
        Person person1 = new Person(); // tworzymy obiekt
        person1.forename = "Jan"; // przypisujemy polu imiê wartoœæ
        person1.surname = "Kowalski";
        person1.age = 35;
        person1.introduceYourself(); // wywo³ujemy metodê
        person1.growOld(5); // metoda z parametrem
        person1.introduceYourself(); // jeszcze raz siê przedstawiamy z innym wiekiem
    }

}