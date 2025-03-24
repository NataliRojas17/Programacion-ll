import java.util.Scanner;

class EcuacionesCuadraticas {
    private double a, b, c;
    
    public EcuacionesCuadraticas(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    
    public double getDiscriminante() {
        return (b * b) - (4 * a * c);
    }
    
    public double getRaiz1() {
        double discriminante = getDiscriminante();
        if (discriminante < 0);
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }

    public double getRaiz2() {
        double discriminante = getDiscriminante();
        if (discriminante < 0);
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }
    
    public void resultado() {
        double discriminante = getDiscriminante();
        if (discriminante > 0) {
            System.out.printf("La ecuación tiene dos raíces %.6f y %.5f", getRaiz1(), getRaiz2());
        } else if (discriminante == 0) {
            System.out.printf("La ecuación tiene una raíz %d", (int)getRaiz1());
        } else {
            System.out.println("La ecuación no tiene raíces reales");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Ingrese a, b, c: ");
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();
        
        EcuacionesCuadraticas ecuacion = new EcuacionesCuadraticas(a, b, c);
        ecuacion.resultado();
        
        input.close();
    }
}
