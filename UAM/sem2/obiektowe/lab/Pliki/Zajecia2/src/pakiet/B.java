package pakiet;

public class B extends A{
	
	public String pole = "Jestem obiektwem w klasie B";
	
	@Override
	public void wypisz() {
		
		this.a= 9;
		this.b= 0;
		this.d= 4;
		
		System.out.println("Metoda klasy B");
	}

}
