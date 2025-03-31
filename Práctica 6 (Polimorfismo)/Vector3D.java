public class Vector3D {
    private double x, y;

    public Vector3D(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double productoEscalar(Vector3D o) {
        return this.x * o.x + this.y * o.y;
    }

    public double productoCruzado(Vector3D o) {
        return this.x * o.y - this.y * o.x;
    }

    public Vector3D proyeccionSobre(Vector3D b) {
        double escalar = this.productoEscalar(b) / b.productoEscalar(b);
        return new Vector3D(b.x * escalar, b.y * escalar);
    }

    public void imprimir() {
        System.out.print("(" + (int)x + "," + (int)y + ")");
    }

    public static void main(String[] args) {
        Vector3D a = new Vector3D(2, 5);
        Vector3D b = new Vector3D(4, 10);

        System.out.println("Producto escalar = " + a.productoEscalar(b));
        System.out.println("Producto cruzado = " + a.productoCruzado(b));
        System.out.print("Proyección de a sobre b: ");
        a.proyeccionSobre(b).imprimir();
        System.out.println();
    }
}
