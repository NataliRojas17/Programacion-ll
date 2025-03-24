import java.util.Scanner;

public class Estadisticas {
    // promedio
    public static double promedio(double[] numeros) {
        double suma = 0;
        for (double num : numeros) {
            suma = suma + num;
        }
        return suma / numeros.length;
    }
    // desviación estándar
    public static double desviacion(double[] numeros, double promedio) {
        double suma = 0;
        int n = numeros.length;
        for (double num : numeros) {
            suma = suma + Math.pow(num - promedio, 2);
        }
        return Math.sqrt(suma / (n - 1));
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double[] numeros = new double[10];

        System.out.println();
        for (int i = 0; i < 10; i++) {
            numeros[i] = input.nextDouble();
        }

        double promedio = promedio(numeros);
        double desviacion = desviacion(numeros, promedio);

        System.out.printf("El promedio es %.2f%n", promedio);
        System.out.printf("La desviación estándar es %.5f", desviacion);

        input.close();
    }
}
