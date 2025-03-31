public class AlgebraVectorial {
    private double x, y, z;

    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double productoPunto(AlgebraVectorial o) {
        return this.x * o.x + this.y * o.y + this.z * o.z;
    }

    public AlgebraVectorial productoCruz(AlgebraVectorial o) {
        return new AlgebraVectorial(
            this.y * o.z - this.z * o.y,
            this.z * o.x - this.x * o.z,
            this.x * o.y - this.y * o.x
        );
    }

    public double magnitud() {
        return Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z);
    }

    public AlgebraVectorial proyeccion(AlgebraVectorial o) {
        double magO = o.magnitud();
        if (magO == 0 || this.productoPunto(o) == 0) return null;  // Condición corregida
        double escala = this.productoPunto(o) / (magO * magO);
        return new AlgebraVectorial(escala * o.x, escala * o.y, escala * o.z);
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ", " + z + ")";
    }

    public static void main(String[] args) {
        AlgebraVectorial a = new AlgebraVectorial(1, 2, 3);
        AlgebraVectorial b = new AlgebraVectorial(-2, 1, 0);

        System.out.println("Producto escalar = " + a.productoPunto(b));
        System.out.println("Producto Vectorial = " + a.productoCruz(b));
        System.out.println("Proyección de a sobre b = " + a.proyeccion(b));
    }
}
