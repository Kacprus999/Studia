package zoo;

public class Parrot extends Animal implements Herbivore{

    @Override
    public void eatPlant(double weight) {
        eat(weight);
    }

}