package pierwszy;

import java.util.Random;
public class punkty {
    static void fillPoint(punkt p){
        Random rand = new Random();
        p.setX(rand.nextDouble());
        p.setY(rand.nextDouble());
        p.setZ(rand.nextDouble());
    }
     
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        System.out.println("ello");
        punkt [] tablica = new punkt[4];
        for(int i=0;i<4;i++){
            tablica[i]=new punkt();
        }
        for(int i=0;i<5;i++){
            fillPoint(tablica[i]);
            System.out.println("point radius = "+ tablica[i].getR());
        }
    }
}