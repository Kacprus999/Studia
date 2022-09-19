package zoo;
import java.util.ArrayList;
import java.util.List;


public class ZooApplication {

    public static void main(String[] args) {

        Elephant elephant1 = new Elephant();
        elephant1.setName("Hadoop");
        elephant1.eat(7000);
        elephant1.growOld(11);

        Elephant elephant2 = new Elephant();
        elephant2.setName("Dumboo");
        elephant2.eat(6000);
        elephant2.growOld(77);

        Lion lion1 = new Lion();
        lion1.setName("Simba");
        lion1.eat(100); // mo¿emy tak
        lion1.eatMeat(100); // lub tak
        // lion1.eatPlant(100); // ale nie tak...
        lion1.growOld(24);

        Parrot parrot1 = new Parrot();
        parrot1.setName("Ara");
        parrot1.eatPlant(1);
        parrot1.growOld(5);

        List<Elephant> elephants = new ArrayList<>();
        elephants.add(elephant1);
        elephants.add(elephant2);

        List<Animal> animals = new ArrayList<>();
        animals.add(elephant1);
        animals.add(elephant2);
        animals.add(lion1);
        animals.add(parrot1);

        List<Herbivore> herbivores = new ArrayList<>();
        herbivores.add(elephant1);
        herbivores.add(elephant2);
        herbivores.add(parrot1); // papuga jest ro¿lino¿erc¹!
        // herbivores.add(lion1); // tak nie mo¿na!

        System.out.println("Liczba s³oni: " + elephants.size());
        System.out.println("Liczba roœlino¿erców: " + herbivores.size());
        System.out.println("Liczba zwierz¹t: " + animals.size());
    }

}
