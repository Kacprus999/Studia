package zoo;

public abstract class Animal {

    private String name;
    private int age;
    private double weight;

    public Animal() {
        System.out.println("Tworz� zwierz� bez imienia...");
    }

    public Animal(String name) {
        this.name = name;
        System.out.println("Tworz� zwierz� o imieniu " + name);
    }

    /**
     * Nazwyam zwierz�
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Starzeje si�, wi�c m�j wiek wzrasta...
     */
    public void growOld(int age) {
        this.age += age;
    }

    /**
     * Jem wi�c staj� si� ci�szy
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