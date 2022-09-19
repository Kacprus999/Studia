package zoo;

public class Elephant extends Animal implements Herbivore {

    /**
     * S³oñ je trochê inaczej
     */
    @Override
    public void eat(double weight) {
        super.eat(1 / 2 * weight);
    }

    @Override
    public void eatPlant(double weight) {
        eat(weight); // Nie ma s³owa super, u¿ywamy metody eat z klasy Elephant!!!
    }

}