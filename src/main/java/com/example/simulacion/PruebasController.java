package com.example.simulacion;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TextArea;

import java.util.Arrays;
import java.util.Random;

public class PruebasController {
    // Este es el método que se llamará al pulsar el botón.
    public static void ejecutar() {
        // Ejemplo: Prueba de Kolmogorov-Smirnov (KS) para Uniformidad.
        // Generar 10 números R_i y probar si son U(0, 1).
        int N = 10;
        double[] R = new double[N];
        Random r = new Random();
        for (int i = 0; i < N; i++) {
            R[i] = r.nextDouble();
        }
        Arrays.sort(R);

        // Cálculo de D+ y D- (parte de la estadística KS)
        double D_plus = 0.0;
        double D_minus = 0.0;
        for (int i = 0; i < N; i++) {
            // i_N es F(x_i)
            double i_N = (double) (i + 1) / N;
            // i_1_N es F(x_{i-1})
            double i_1_N = (double) i / N;

            // D+ = max(i/N - R_i)
            D_plus = Math.max(D_plus, i_N - R[i]);

            // D- = max(R_i - (i-1)/N)
            D_minus = Math.max(D_minus, R[i] - i_1_N);
        }
        double D = Math.max(D_plus, D_minus);

        String resultado = String.format(
                "*** RESULTADO PRUEBAS ESTADÍSTICAS ***\n\n" +
                        "Ejemplo: Estadística de la prueba de Kolmogorov-Smirnov (KS).\n" +
                        "Se probaron %d números aleatorios para uniformidad.\n" +
                        "D+ (Máxima diferencia positiva) = %.4f\n" +
                        "D- (Máxima diferencia negativa) = %.4f\n" +
                        "Estadístico D = %.4f\n\n" +
                        "Nota: Si D es mayor que el valor crítico (ej. 0.409 para N=10, α=0.05), se rechaza la uniformidad.",
                N, D_plus, D_minus, D);

        // Llama al método estático para mostrar el resultado en un Alert
        mostrarResultado("7. Pruebas Estadísticas", resultado);
    }

    // Método auxiliar para mostrar el resultado en un Alert
    private static void mostrarResultado(String titulo, String contenido) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Resultado de Ejercicio");
        alert.setHeaderText(titulo);
        alert.setContentText(contenido);
        alert.showAndWait();
    }
}
