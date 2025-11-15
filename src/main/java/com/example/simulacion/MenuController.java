package com.example.simulacion;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;

import java.io.IOException;

public class MenuController {
    private BorderPane rootPane; // Referencia al BorderPane principal

    // Llamado por HelloApplication
    public void setRootPane(BorderPane pane) {
        this.rootPane = pane;
        // Carga el Ejercicio 1 al inicio
        cargarContenido(DiscretaController.class, "1. V.A. Discretas");
    }

    // --- Métodos de Navegación (Botones) ---
    @FXML
    private void cargarDiscreta() {
        DiscretaController.ejecutar();
    }

    @FXML
    private void cargarContinua() {
        ContinuaController.ejecutar();
    }

    @FXML
    private void cargarInversa() {
       InversaController.ejecutar();
    }

    @FXML
    private void cargarConvolucion() {
       ConvolucionController.ejecutar();
    }

    @FXML
    private void cargarComposicion() {
        ComposicionController.ejecutar();
    }

    @FXML
    private void cargarEspecial() {
        EspecialController.ejecutar();
    }

    @FXML
    private void cargarPruebas() {
        PruebasController.ejecutar();
    }


    private void cargarContenido(Class<?> controllerClass, String titulo) {
        try {
            // SOLUCIÓN: Usar "/" para buscar el archivo en la raíz de la carpeta 'resources' (classpath).
            // Esto soluciona el error 'Location is not set' que se propaga a loader.load() (línea 77).
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/ejercicio-content.fxml"));

            // Inyectamos el controlador de LÓGICA (DiscretaController, etc.) ANTES de cargar el FXML
            loader.setControllerFactory(c -> {
                try {
                    return controllerClass.getDeclaredConstructor().newInstance();
                } catch (Exception e) {
                    // El error en consola si falla la inyección de controlador
                    throw new RuntimeException("Error al instanciar el controlador: " + controllerClass.getName(), e);
                }
            });

            Node ejercicioUI = loader.load(); // Línea 77 - Ahora no debe fallar

            // Actualizar el título del ejercicio
            Object controllerInstance = loader.getController();
            if (ejercicioUI instanceof javafx.scene.layout.VBox) {
                // Asume que el Label es el primer componente del VBox de ejercicio-content.fxml
                Label tituloLabel = (Label) ((javafx.scene.layout.VBox) ejercicioUI).getChildren().get(0);
                tituloLabel.setText(titulo);
            }

            if (rootPane != null) {
                rootPane.setCenter(ejercicioUI);
            }
        } catch (IOException e) {
            e.printStackTrace();
            // Mensaje en consola si el FXML no se encuentra o hay otro problema de IO
            System.err.println("Error al cargar el contenido del ejercicio.");
        }
    }
}
