public class FigurasGeometricas {
    public static double area(double radio) { // Círculo
        return Math.PI * radio * radio;
    }

    double area(double base, double altura) { // Rectángulo
        return base * altura;
    }

    double area(double b, float h) { // Triángulo rectángulo
        return (b * h) / 2;
    }

    double area(double lado1, double lado2, double alto) { // Trapecio
        return ((lado1 + lado2) * alto) / 2;
    }

    double area(float lado, double apotema) { // Pentágono regular
        return (5 * lado * apotema) / 2;
    }


    public static void main(String[] args) {
        FigurasGeometricas f1 = new FigurasGeometricas();
        FigurasGeometricas f2 = new FigurasGeometricas();
        FigurasGeometricas f3 = new FigurasGeometricas();
        FigurasGeometricas f4 = new FigurasGeometricas();
        FigurasGeometricas f5 = new FigurasGeometricas();

        System.out.println("Círculo: " + f1.area(3.0)); 
        System.out.println("Rectángulo: " + f2.area(4.0, 6.0)); 
        System.out.println("Triángulo Rectángulo: " + f3.area(5.0,8)); 
        System.out.println("Trapecio: " + f4.area(6.0, 4.0, 5.0));
        System.out.println("Pentágono: " + f5.area(7, 3.0)); 
    }
}