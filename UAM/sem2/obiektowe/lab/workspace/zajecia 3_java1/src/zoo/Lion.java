package zoo;
public class Lion extends Animal implements Carnivore{

    @Override
    public void eatMeat(double weight) {
        eat(weight); // tutaj tak¿e s³owo super nie jest potrzebne bo nie ma konfliktu nazw
    }

}