package Konstruktory;

class Insekt {
	 final int i = 9;
	 final int j=1;

	Insekt(int a) {
		System.out.println("Teraz wykonuje konstruktor Insekt!");
		System.out.println("i =" + i + " ,j=" + j);
	}

	private static int x1 = print("statyczna zmienna Insekta zainicjalizowana");

	public  String nazwa() {
		return "Insecta";
	}

	static int print(String s) {
		System.out.println(s);
		return 47;
	}
}

class Pszczola extends Insekt {
	private int k = print("Zmienna Pszczoly zainicjalizowana");
	
	public Pszczola() {
		super(3);
		System.out.println("Teraz wykonuje konstruktor Pszczoly!");
		System.out.println("k = " + k);
		System.out.println("j = " + j);
		k = 23;
		System.out.println("k = " + k);
	}
	public Pszczola(int b) {
		super(3);
	}
	public String nazwa() {
		return "Apis";
	}

	private static int x2 = print("statyczna zmienna Pszczoly zainicjalizowana");
}

public class Konstruktory {

	public static void main(String[] args) {
		System.out.println("Pszczola tworzymy obiekt");
		Pszczola b1 = new Pszczola();
		Pszczola b2 = new Pszczola();
		System.out.println(b1.nazwa());
	}

}
