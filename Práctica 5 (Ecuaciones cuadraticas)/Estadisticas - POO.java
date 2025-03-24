import java.util.Scanner;
class Estadistica {
    private double[] numeros;
    public Estadistica(double[] numeros) {
        this.numeros = numeros;
    }
    // promedio
    public double promedio() {
        double suma = 0;
        for (double num : numeros) {
            suma = suma + num;
        }
        return suma / numeros.length;
    }

    // desviación estándar
    public double desviacionestandar() {
        double promedios = promedio();
        double suma = 0;
        int n = numeros.length;

        for (double num : numeros) {
            suma = suma + Math.pow(num - promedios, 2);
        }
        return Math.sqrt(suma / (n - 1));
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double[] numeros = new double[10];

        System.out.println();
        for (int i = 0; i < 10; i++) {
            numeros[i] = input.nextDouble();
        }

        Estadistica estadistica = new Estadistica(numeros);
        double promedios = estadistica.promedio();
        double desviacion = estadistica.desviacionestandar();

        System.out.printf("El promedio es %.2f%n", promedios);
        System.out.printf("La desviación estándar es %.5f%n", desviacion);

        input.close();
    }
}
