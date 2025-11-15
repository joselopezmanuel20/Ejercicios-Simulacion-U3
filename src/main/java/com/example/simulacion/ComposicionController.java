package com.example.simulacion;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TextArea;

import java.util.Random;

public class ComposicionController {
    // Este es el método que se llamará al pulsar el botón.
    public static void ejecutar() {
        // Lógica del método de composición (copiada de tu código)
        Random r = new Random();

        StringBuilder sb = new StringBuilder();
        sb.append("*** RESULTADO MÉTODO DE COMPOSICIÓN ***\n\n");
        sb.append("Simulación de una VA mixta (50% Exp(1), 50% Exp(5)).\n");
        sb.append("Regla: Generar U1. Si U1 < 0.5, usa Exp(1). Si U1 >= 0.5, usa Exp(5).\n\n");

        for (int i = 0; i < 5; i++) {
            double U1 = r.nextDouble();
            double U2 = r.nextDouble();
            double X;
            String distribucion;

            if (U1 < 0.5) {
                X = - (1.0 / 1.0) * Math.log(U2);
                distribucion = "Exp(1)";
            } else {
                X = - (1.0 / 5.0) * Math.log(U2);
                distribucion = "Exp(5)";
            }
            sb.append(String.format("U1=%.4f -> Usa %s -> X=%.4f\n", U1, distribucion, X));
        }

        // Llamamos al método estático para mostrar el Alert
        mostrarResultado("5. Método Composición", sb.toString());
    }

    // Método auxiliar (como en tus ejemplos)
    private static void mostrarResultado(String titulo, String contenido) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Resultado de Ejercicio");
        alert.setHeaderText(titulo);
        alert.setContentText(contenido);
        alert.showAndWait();
    }
}
