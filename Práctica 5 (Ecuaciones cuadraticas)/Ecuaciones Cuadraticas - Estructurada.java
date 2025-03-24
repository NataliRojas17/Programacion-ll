import java.util.Scanner;

public class EcuacionesCuadraticas {
    public static double getDiscriminante(double a, double b, double c) {
        return (b * b) - (4 * a * c);
    }

    public static double getRaiz1(double a, double b, double discriminante) {
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }

    public static double getRaiz2(double a, double b, double discriminante) {
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Ingrese a, b, c: ");
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();
        double discriminante = getDiscriminante(a, b, c);

        if (discriminante > 0) {
            System.out.printf("La ecuación tiene dos raíces %.6f y %.5f", getRaiz1(a, b, discriminante), getRaiz2(a, b, discriminante));
        } else if (discriminante == 0) {
            System.out.printf("La ecuación tiene una raíz %d", (int)getRaiz1(a, b, discriminante));
        } else {
            System.out.println("La ecuación no tiene raíces reales");
        }
        input.close();
    }
}









