
public class VentasMen {
    private double[][] ventas;

    public VentasMen() {
        ventas = new double[12][3];
    }

    public void insertarVenta(int mes, int dpto, double monto) {
        if (mes >= 0 && mes < 12 && dpto >= 0 && dpto < 3) {
            ventas[mes][dpto] = monto;
        } else {
            System.out.println(" El mes o departamento está fuera de rango.");
        }
    }

    public Double buscarVenta(int mes, int dpto) {
        if (mes >= 0 && mes < 12 && dpto >= 0 && dpto < 3) {
            return ventas[mes][dpto];
        } else {
            System.out.println(" Consulta inválida, fuera del rango de la matriz.");
            return null;
        }
    }

    public void eliminarVenta(int mes, int dpto) {
        if (mes >= 0 && mes < 12 && dpto >= 0 && dpto < 3) {
            ventas[mes][dpto] = 0.0;
        } else {
            System.out.println(" No se puede eliminar, índice fuera de rango.");
        }
    }

    public void mostrarVentas() {
        String[] meses = { "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" };
        String[] dptos = { "Ropa", "Deportes", "Juguetería" };

        System.out.printf("%-12s | %-10s | %-10s | %-12s%n", "Mes", dptos[0], dptos[1], dptos[2]);
        System.out.println("----------------------------------------------------");

        for (int i = 0; i < ventas.length; i++) {
            System.out.printf("%-12s |", meses[i]);
            for (int j = 0; j < ventas[i].length; j++) {
                System.out.printf(" $%-9.2f |", ventas[i][j]);
            }
            System.out.println();
        }
    }

    // #AQUI HAGO LAS PRUEBAS DE QUE FUNCIONAN LOS MÉTODOS, LAS PONGO PARA QUE SE
    // VEA QUE FUNCIONAN LOS METODOS
    public static void main(String[] args) {
        VentasMen ventas = new VentasMen();

        ventas.insertarVenta(0, 0, 30000.0);
        ventas.insertarVenta(1, 2, 90500.0);
        ventas.insertarVenta(11, 1, 23000.0);

        System.out.println("Ventas Mensuales:");
        ventas.mostrarVentas();

        Double monto = ventas.buscarVenta(1, 2);
        if (monto != null) {
            System.out.printf("%nConsulta: Febrero - Juguetería: $%.2f%n", monto);
        }

        ventas.eliminarVenta(1, 2);
        System.out.println("\nVentas después de eliminar:");
        ventas.mostrarVentas();
    }
}