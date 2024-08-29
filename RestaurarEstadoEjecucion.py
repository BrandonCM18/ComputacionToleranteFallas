import pickle
import time

class Tarea:
    def __init__(self, id_tarea, descripcion):
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.completada = False
    
    def ejecutar(self):
        print(f"Ejecutando tarea {self.id_tarea}: {self.descripcion}")
        time.sleep(2)  # Simula una tarea que toma tiempo
        self.completada = True
        print(f"Tarea {self.id_tarea} completada")

class SistemaTareas:
    def __init__(self):
        self.cola_tareas = []
        self.tareas_en_progreso = None
        self.tareas_completadas = []
    
    def agregar_tarea(self, tarea):
        self.cola_tareas.append(tarea)
    
    def siguiente_tarea(self):
        if self.cola_tareas:
            self.tareas_en_progreso = self.cola_tareas.pop(0)
            return self.tareas_en_progreso
        return None
    
    def ejecutar_tarea_actual(self):
        if self.tareas_en_progreso:
            self.tareas_en_progreso.ejecutar()
            self.tareas_completadas.append(self.tareas_en_progreso)
            self.tareas_en_progreso = None
    
    def guardar_estado(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self, f)
        print(f"Estado del sistema guardado en {archivo}")

    @staticmethod
    def cargar_estado(archivo):
        with open(archivo, 'rb') as f:
            return pickle.load(f)

# Crear el sistema de tareas
sistema = SistemaTareas()

# Agregar algunas tareas
sistema.agregar_tarea(Tarea(1, "Analizar datos"))
sistema.agregar_tarea(Tarea(2, "Generar informe"))
sistema.agregar_tarea(Tarea(3, "Enviar informe"))

# Ejecutar una tarea
tarea_actual = sistema.siguiente_tarea()
sistema.ejecutar_tarea_actual()

# Guardar el estado actual
sistema.guardar_estado('sistema_tareas.pkl')

# Cargar y continuar
sistema_restaurado = SistemaTareas.cargar_estado('sistema_tareas.pkl')
print("\n--- Estado restaurado ---\n")

# Continuar con la siguiente tarea
tarea_actual = sistema_restaurado.siguiente_tarea()
if tarea_actual:
    sistema_restaurado.ejecutar_tarea_actual()

# Guardar el estado nuevamente
sistema_restaurado.guardar_estado('sistema_tareas.pkl')
