package com.example.simulacion;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TextArea;

public class ContinuaController {
    public static void ejecutar() {
        // --- Lógica de V.A. Continuas ---
        double a = 5.0, b = 15.0; // Uniforme U(5, 15)
        double esperanza = (a + b) / 2.0;
        double varianza = Math.pow(b - a, 2) / 12.0;

        String resultado = String.format(
                "*** RESULTADO V.A. CONTINUAS ***\n\n" +
                        "Ejemplo: Distribución Uniforme U(%.1f, %.1f)\n" +
                        "E[X] (Esperanza) = %.3f\n" +
                        "Var(X) (Varianza) = %.3f", a, b, esperanza, varianza);

        // Llama al método estático para mostrar el resultado en un Alert
        mostrarResultado("2. V.A. Continuas", resultado);
    }

    // Método auxiliar (copiado de tus ejemplos)
    private static void mostrarResultado(String titulo, String contenido) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Resultado de Ejercicio");
        alert.setHeaderText(titulo);
        alert.setContentText(contenido);
        alert.showAndWait();
    }
}
