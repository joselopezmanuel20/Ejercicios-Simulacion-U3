package com.example.simulacion;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TextArea;

import java.util.Random;

public class InversaController {
    // Este es el método que se llamará al pulsar el botón.
    public static void ejecutar() {
        // Simulación de la Distribución Exponencial Exp(λ=0.5)
        double lambda = 0.5;
        Random r = new Random();

        StringBuilder sb = new StringBuilder();
        sb.append("*** RESULTADO TRANSFORMADA INVERSA ***\n\n");
        sb.append("Simulación de 5 valores de una Exponencial (λ=0.5).\n");
        sb.append("Fórmula: X = - (1/λ) * ln(U)\n\n");

        for (int i = 0; i < 5; i++) {
            double U = r.nextDouble(); // Genera U ~ U(0, 1)
            // Transformada Inversa: X = G^-1(U)
            double X = -(1.0 / lambda) * Math.log(U);
            sb.append(String.format("U%d=%.4f -> X%d=%.4f\n", i + 1, U, i + 1, X));
        }

        // Llama al método estático para mostrar el resultado en un Alert
        mostrarResultado("3. Transf. Inversa", sb.toString());
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
