package com.example.simulacion.;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TextArea;

import java.util.Random;

public class ConvolucionController {
    // Este es el método que se llamará al pulsar el botón.
    public static void ejecutar() {
        // Ejemplo: Simular una Distribución Erlang(k=2, λ=0.5) usando suma de Exponenciales.
        double lambda = 0.5;
        int k = 2; // k es el número de VA Exponenciales a sumar
        Random r = new Random();

        StringBuilder sb = new StringBuilder();
        sb.append("*** RESULTADO MÉTODO DE CONVOLUCIÓN ***\n\n");
        sb.append("Simulación de una Erlang(k=2, λ=0.5) sumando 2 Exponenciales.\n");
        sb.append("Fórmula: X = X1 + X2 (donde X_i ~ Exp(λ))\n\n");

        for (int i = 0; i < 5; i++) {
            // Se generan 2 variables uniformes (U1 y U2) para simular 2 VA Exponenciales (X1 y X2)
            double U1 = r.nextDouble();
            double U2 = r.nextDouble();

            // Simulación de VA Exponencial: X = - (1/λ) * ln(U)
            double X1 = -(1.0 / lambda) * Math.log(U1);
            double X2 = -(1.0 / lambda) * Math.log(U2);

            double X = X1 + X2;
            sb.append(String.format("X1=%.4f + X2=%.4f -> X=%.4f\n", X1, X2, X));
        }

        // Llama al método estático para mostrar el resultado en un Alert
        mostrarResultado("4. Método Convolución", sb.toString());
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
