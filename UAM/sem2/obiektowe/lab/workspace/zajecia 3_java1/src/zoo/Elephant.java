package zoo;

public class Elephant extends Animal implements Herbivore {

    /**
     * S�o� je troch� inaczej
     */
    @Override
    public void eat(double weight) {
        super.eat(1 / 2 * weight);
    }

    @Override
    public void eatPlant(double weight) {
        eat(weight); // Nie ma s�owa super, u�ywamy metody eat z klasy Elephant!!!
    }

}