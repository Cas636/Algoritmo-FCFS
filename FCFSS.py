import threading
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
from queue import Queue

# Lista para almacenar los procesos
procesos = []
procesos_lock = threading.Lock()

# Cola para manejar los procesos
cola_procesos = Queue()

# Variable global para almacenar el tiempo de llegada del último proceso
ultimo_tiempo_llegada = 0

# Generar un proceso aleatorio
def generar_proceso():
    global ultimo_tiempo_llegada
    global procesos
    
    # Asegurarse de que el tiempo de llegada sea mayor o igual al último
    tiempo_llegada = random.randint(ultimo_tiempo_llegada, ultimo_tiempo_llegada + 5)
    
    # Asegurarse de que el tiempo de llegada no sea menor al último
    if tiempo_llegada < ultimo_tiempo_llegada:
        tiempo_llegada = ultimo_tiempo_llegada
    
    rafaga = random.randint(1, 9)
    
    # Actualizar el tiempo de llegada del último proceso
    ultimo_tiempo_llegada = tiempo_llegada
    
    return {"tiempo_llegada": tiempo_llegada, "rafaga": rafaga}

# Hilo que genera procesos continuamente
def generador_de_procesos():
    global procesos
    while len(procesos) < 5:  # Genera un máximo de 5 procesos
        nuevo_proceso = generar_proceso()
        with procesos_lock:  # Usar el Lock para asegurar acceso seguro a las estructuras
            procesos.append(nuevo_proceso)
            cola_procesos.put(nuevo_proceso)
        #print(f"Proceso generado: {nuevo_proceso}")
        time.sleep(random.uniform(2, 4))  # Espera aleatoria entre 1 y 3 segundos
    #print("Generación de procesos completada.")

# Simulación de ejecución de procesos
def ejecutar_procesos():
    global procesos
    tiempo_actual = 0
    tabla = []
    gantt = []
    procesados = 0  # Contador de procesos ejecutados

    while not cola_procesos.empty() or plt.fignum_exists(1):
        try:
            #print(f"Procesos en cola: {cola_procesos.qsize()}, Procesos restantes: {len(procesos)}")

            if not cola_procesos.empty():
                proceso = cola_procesos.get()
                tiempo_llegada = proceso["tiempo_llegada"]
                rafaga = proceso["rafaga"]

                # Calcular tiempos
                tiempo_comienzo = max(tiempo_actual, tiempo_llegada)
                tiempo_final = tiempo_comienzo + rafaga  
                tiempo_retorno = tiempo_final - tiempo_llegada 
                tiempo_espera = tiempo_retorno - rafaga

                # Agregar a la tabla
                tabla.append({
                    "T. Llegada": tiempo_llegada,
                    "Ráfaga": rafaga,
                    "T. Comienzo": tiempo_comienzo,
                    "T. Final": tiempo_final,  
                    "T. Retorno": tiempo_retorno,
                    "T. Espera": tiempo_espera
                })

                # Actualizar tiempo actual
                tiempo_actual = tiempo_final

                # Actualizar Gantt con identificador del proceso
                gantt.append((procesados, tiempo_comienzo, tiempo_final, tiempo_llegada))
                procesados += 1

                # Eliminar el proceso de la lista 'procesos'
                with procesos_lock:
                    procesos.remove(proceso)

        except ValueError as e:
            print(e)
            continue

        # Mostrar la tabla
        df = pd.DataFrame(tabla)
        print(df)

        # Generar diagrama de Gantt
        generar_diagrama_gantt(gantt, tabla)


# Crear la figura global para el diagrama de Gantt
fig, ax = plt.subplots(figsize=(19, 9))  # Ancho: 16 pulgadas, Alto: 10 pulgadas


def generar_diagrama_gantt(gantt, tabla):
    ax.clear()  # Limpiar el contenido del gráfico

    # Dibujar barras del diagrama de Gantt
    for proceso, inicio, fin, llegada in gantt:
        ax.broken_barh([(inicio, fin - inicio)], (10 + proceso * 10, 9), facecolors="tab:purple")
        ax.text((inicio + fin) / 2, 15 + proceso * 10, f"P{proceso}", ha="center", va="center", color="white")

        # Dibujar línea punteada desde tiempo de llegada hasta el inicio
        if llegada < inicio:  # Solo dibujar si hay tiempo de espera
            ax.plot([llegada, inicio], [14 + proceso * 10, 14 + proceso * 10], linestyle="--", color="gray")

    # Ajustar el espacio para incluir la tabla
    ax.set_position([0.1, 0.5, 0.8, 0.4])  # Ajusta los valores según el nuevo tamaño


    # Dibujar la tabla
    if tabla:
        df = pd.DataFrame(tabla)
        ax_table = plt.gca().table(
            cellText=df.values,
            colLabels=df.columns,
            cellLoc="center",
            loc="bottom",
            bbox=[0, -0.9, 1, 0.7],  # [x, y, width, height]
        )
        ax_table.auto_set_font_size(False)
        ax_table.set_fontsize(10)
        ax_table.scale(1, 1.5)

    # Configurar el gráfico
    ax.set_ylim(5, 25 + len(gantt) * 10)
    ax.set_xlim(0, max(fin for _, _, fin, _ in gantt) + 1)
    ax.set_xlabel("Tiempo")
    ax.set_yticks([])
    ax.set_title("Diagrama de Gantt")
    plt.pause(0.1)


# Crear y ejecutar hilos
hilo_generador = threading.Thread(target=generador_de_procesos)
hilo_generador.start()

# Habilitar modo interactivo
plt.ion()

# Ejecutar los procesos
ejecutar_procesos()

# Desactivar modo interactivo y mostrar gráfico final
plt.ioff()
plt.show()
