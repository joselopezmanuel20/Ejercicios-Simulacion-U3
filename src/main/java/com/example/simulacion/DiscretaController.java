package com.example.simulacion;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TextArea;

import java.util.Map;

public class DiscretaController {
    // Este método reemplaza al initialize() que tenías
    public static void ejecutar() {
        Map<Integer, Double> pmf = Map.of(0, 0.1, 1, 0.3, 2, 0.4, 3, 0.2);
        double esperanza = 0.0, ex2 = 0.0;

        for (var e : pmf.entrySet()) {
            esperanza += e.getKey() * e.getValue();
            ex2 += (e.getKey() * e.getKey()) * e.getValue();
        }
        double varianza = ex2 - esperanza * esperanza;

        String resultado = String.format(
                "*** RESULTADO V.A. DISCRETAS ***\n\n" +
                        "Ejemplo: PMF de X (0.1, 0.3, 0.4, 0.2)\n" +
                        "E[X] (Esperanza) = %.3f\n" +
                        "Var(X) (Varianza) = %.3f", esperanza, varianza);

        mostrarResultado("1. V.A. Discretas", resultado); // Muestra el Alert
    }

    // Método auxiliar para mostrar el resultado en un Alert (copiado de tu ejemplo)
    private static void mostrarResultado(String titulo, String contenido) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Resultado de Ejercicio");
        alert.setHeaderText(titulo);
        alert.setContentText(contenido);
        alert.showAndWait();
    }
}
