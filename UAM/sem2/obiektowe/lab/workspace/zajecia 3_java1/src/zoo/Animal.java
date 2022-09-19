package zoo;

public abstract class Animal {

    private String name;
    private int age;
    private double weight;

    public Animal() {
        System.out.println("Tworzê zwierzê bez imienia...");
    }

    public Animal(String name) {
        this.name = name;
        System.out.println("Tworzê zwierzê o imieniu " + name);
    }

    /**
     * Nazwyam zwierzê
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Starzeje siê, wiêc mój wiek wzrasta...
     */
    public void growOld(int age) {
        this.age += age;
    }

    /**
     * Jem wiêc stajê siê ciê¿szy
     */
    public void eat(double weight) {
        this.weight += 3 / 4 * weight;
    }

	public void eatPlant(double weight) {
		// TODO Auto-generated method stub
		
	}

	public void eatMeat(double weight) {
		// TODO Auto-generated method stub
		
	}

}