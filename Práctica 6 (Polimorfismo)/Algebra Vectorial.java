public class AlgebraVectorial {
    private double x, y, z;

    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public AlgebraVectorial(double x, double y) {
        this(x, y, 0);
    }

    public AlgebraVectorial sumar(AlgebraVectorial o) {
        return new AlgebraVectorial(this.x + o.x, this.y + o.y, this.z + o.z);
    }

    public AlgebraVectorial restar(AlgebraVectorial o) {
        return new AlgebraVectorial(this.x - o.x, this.y - o.y, this.z - o.z);
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

    public boolean esPerpendicular(AlgebraVectorial o) {
        return this.productoPunto(o) == 0;
    }

    public boolean esParalelo(AlgebraVectorial o) {
        return this.productoCruz(o).magnitud() == 0;
    }

    public AlgebraVectorial proyeccion(AlgebraVectorial o) {
        double escala = this.productoPunto(o) / (o.magnitud() * o.magnitud());
        return new AlgebraVectorial(escala * o.x, escala * o.y, escala * o.z);
    }

    public double componente(AlgebraVectorial o) {
        return this.productoPunto(o) / o.magnitud();
    }

    @Override
    public String toString() {
        return x + ", " + y + ", " + z ;
    }

    public static void main(String[] args) {
        AlgebraVectorial a = new AlgebraVectorial(6, -3, 9);
        AlgebraVectorial b = new AlgebraVectorial(4, 2, -6);

        System.out.println("¿Son perpendiculares? " + a.esPerpendicular(b));
        System.out.println("¿Son paralelos? " + a.esParalelo(b));
        System.out.println("Proyeccion de a sobre b: " + a.proyeccion(b));
        System.out.println("Componente de a en b: " + a.componente(b));
    }
}

