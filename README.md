﻿# Simulador de Procesos con Diagrama de Gantt

Este proyecto implementa un simulador de procesos que utiliza hilos para generar y ejecutar procesos de manera concurrente. El programa muestra un diagrama de Gantt dinámico y una tabla con los tiempos calculados para cada proceso.

## Características

- **Generación dinámica de procesos**: Los procesos se generan aleatoriamente con tiempos de llegada y ráfagas.
- **Simulación de ejecución**: Los procesos se ejecutan simulando tiempos de espera y ejecución.
- **Diagrama de Gantt interactivo**: Se muestra un diagrama de Gantt en tiempo real con identificadores de procesos y líneas punteadas indicando tiempos de espera.
- **Tabla dinámica**: Una tabla actualizada dinámicamente muestra los tiempos de llegada, ráfaga, comienzo, final, retorno y espera de cada proceso.

## Requisitos

- Python 3.7 o superior
- Librerías:
  - `threading`
  - `random`
  - `time`
  - `pandas`
  - `matplotlib`

Puedes instalar las librerías necesarias ejecutando:

```bash
pip install pandas matplotlib
```

## Creación de un Entorno Virtual

Para evitar conflictos con otras dependencias, se recomienda usar un entorno virtual:

1. Crea el entorno virtual:
   ```bash
   python -m venv venv
   ```
2. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Instala las dependencias en el entorno virtual:
   ```bash
   pip install pandas matplotlib
   ```

## Estructura del Proyecto

- **`generar_proceso`**: Genera procesos aleatorios con tiempos de llegada y ráfagas.
- **`generador_de_procesos`**: Un hilo que genera procesos continuamente hasta alcanzar un máximo de 5 procesos.
- **`ejecutar_procesos`**: Simula la ejecución de procesos, calcula los tiempos y actualiza el diagrama de Gantt y la tabla.
- **`generar_diagrama_gantt`**: Genera y actualiza el diagrama de Gantt y la tabla dentro de la misma ventana.

## Cómo Ejecutar

1. Clona o descarga este repositorio.
2. Asegúrate de tener instaladas las dependencias requeridas.
3. Activa el entorno virtual si lo creaste (opcional).
4. Ejecuta el archivo principal:
   ```bash
   python FCFSS.py
   ```

## Interacción

- **Ventana del diagrama de Gantt**: Muestra el progreso de la ejecución de los procesos en tiempo real.
- **Tabla dinámica**: Aparece debajo del diagrama y se actualiza con cada proceso ejecutado.

## Ejemplo de Salida

- **Diagrama de Gantt**: Barras de colores que representan los procesos y líneas punteadas que indican tiempos de espera.

### Imagen de Ejemplo

![Salida](Figure_1.png "Ejemplo")

- **Tabla**:
  ```
   T. Llegada  Ráfaga  T. Comienzo  T. Final  T. Retorno  T. Espera
  ```

---

## Licencia

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.

You are free to:

Share — copy and redistribute the material in any medium or format.

Adapt — remix, transform, and build upon the material.

Under the following terms:

Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

NonCommercial — You may not use the material for commercial purposes.

ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

Read more about this license at CC BY-NC-SA 4.0.
