public class Vector3D {
    private double x, y, z;
    public Vector3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    public Vector3D sumar(Vector3D o) {
        return new Vector3D(this.x + o.x, this.y + o.y, this.z + o.z);
    }
    public Vector3D multiplicar(double escalar) {
        return new Vector3D(this.x * escalar, this.y * escalar, this.z * escalar);
    }
    public double magnitud() {
        return Math.sqrt(x * x + y * y + z * z);
    }
    public double productoEscalar(Vector3D o) {
        return this.x * o.x + this.y * o.y + this.z * o.z;
    }
    public Vector3D productoVectorial(Vector3D o) {
        return new Vector3D(
            this.y * o.z - this.z * o.y,
            this.z * o.x - this.x * o.z,
            this.x * o.y - this.y * o.x
        );
    }
    public void imprimir() {
        System.out.print("(");
        imprimirValor(x);
        System.out.print(", ");
        imprimirValor(y);
        System.out.print(", ");
        imprimirValor(z);
        System.out.println(")");
    }
    private void imprimirValor(double valor) {
        if (valor == (int) valor) {
            System.out.print((int) valor);  
        } else {
            System.out.print(valor);  
        }
    }
    public static void main(String[] args) {
        Vector3D v1 = new Vector3D(8, 3, 11);
        Vector3D v2 = new Vector3D(4, 9, 3);

        System.out.print("Suma: ");
        v1.sumar(v2).imprimir();

        System.out.print("Multiplicacion por escalar: ");
        v1.multiplicar(2).imprimir();

        System.out.println("Magnitud de v1: " + v1.magnitud());
        System.out.println("Producto escalar: " + v1.productoEscalar(v2));

        System.out.print("Producto vectorial: ");
        v1.productoVectorial(v2).imprimir();
    }
}
