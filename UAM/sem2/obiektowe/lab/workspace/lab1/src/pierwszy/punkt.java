package pierwszy;

public class punkt {
    double x;
    double y;
    double z;
    public punkt(){
        x = 0;
        y = 0;
        z = 0;
    }
    public double getX() {
        return x;
    }
    public void setX(double x) {
        this.x = x;
    }
    public double getY() {
        return y;
    }
    public void setY(double y) {
        this.y = y;
    }
    public double getZ() {
        return z;
    }
    public void setZ(double z) {
        this.z = z;
    }
    public double getR(){
        return Math.sqrt(x*x+y*x+z*z);
    }
}