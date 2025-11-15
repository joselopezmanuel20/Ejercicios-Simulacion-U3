package com.example.simulacion;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TextArea;

import java.util.Random;

public class EspecialController {
    // Este es el método que se llamará al pulsar el botón.
    public static void ejecutar() {
        // Ejemplo: Simulación de Poisson (λ=3) usando suma de tiempos Exponenciales
        double lambda = 3.0; // Tasa de eventos por unidad de tiempo
        Random r = new Random();

        StringBuilder sb = new StringBuilder();
        sb.append("*** RESULTADO PROCEDIMIENTOS ESPECIALES ***\n\n");
        sb.append("Simulación de una Poisson (λ=3) contando eventos en el tiempo T=1.\n");
        sb.append("Método: Suma de Exponenciales (Tiempos entre llegadas).\n\n");

        for (int i = 0; i < 3; i++) {
            double tiempoAcumulado = 0.0;
            int contador = -1; // Comienza en -1 porque el último tiempo sumado excede el límite
            while (tiempoAcumulado <= 1.0) {
                double U = r.nextDouble();
                // Tiempo entre llegadas ~ Exp(λ) (Fórmula de la inversa)
                double t = -(1.0 / lambda) * Math.log(U);
                tiempoAcumulado += t;
                contador++;
            }
            sb.append(String.format("Muestra %d: Eventos en t=1.0: %d\n", i + 1, contador));
        }

        // Llama al método estático para mostrar el resultado en un Alert
        mostrarResultado("6. Procedimientos Esp.", sb.toString());
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
