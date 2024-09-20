import threading
import time

# Función para un hilo normal
def tarea_hilo(nombre, duracion):
    print(f"Hilo {nombre} iniciando.")
    time.sleep(duracion)
    print(f"Hilo {nombre} finalizado.")

# Función para un hilo demonio
def tarea_demonio():
    while True:
        print("Hilo demonio en ejecución...")
        time.sleep(2)

# Crear hilos
hilo1 = threading.Thread(target=tarea_hilo, args=("1", 3))
hilo2 = threading.Thread(target=tarea_hilo, args=("2", 5))

# Crear hilo demonio
hilo_demonio = threading.Thread(target=tarea_demonio)
hilo_demonio.daemon = True  # Convertir en hilo demonio

# Iniciar hilos
hilo_demonio.start()
hilo1.start()
hilo2.start()

# Esperar a que los hilos normales terminen
hilo1.join()
hilo2.join()

print("Programa finalizado.")
