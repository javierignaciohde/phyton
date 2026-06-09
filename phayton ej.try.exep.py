#Gestor de Notas Universitarias
# Tupla con las materias válidas
# Usamos tupla (no lista) porque las materias NO deben modificarse en tiempo de ejecución
MATERIAS = ("Matematica", "Fisica", "Programacion", "Quimica", "Ingles")

# Diccionario global de estudiantes
# Estructura: { "nombre": { "Materia": [nota1, nota2, ...] } }
estudiantes = {}

def registrar_estudiante(nombre):
    try:
        # strip() elimina espacios, si queda vacío el nombre no es válido
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        
        # No permitimos registrar el mismo estudiante dos veces
        if nombre in estudiantes:
            raise ValueError(f"'{nombre}' ya está registrado.")
        
        # Creamos un diccionario por comprensión:
        # para cada materia en MATERIAS, asignamos una lista vacía de notas
        estudiantes[nombre] = {materia: [] for materia in MATERIAS}
        print(f"Estudiante '{nombre}' registrado.")

    except ValueError as e:
        print(f"Error: {e}")

def agregar_nota(nombre, materia, nota):
    try:
        # Verificamos que el estudiante exista en el diccionario
        if nombre not in estudiantes:
            raise KeyError(f"Estudiante '{nombre}' no encontrado.")
        
        # Verificamos que la materia esté dentro de las permitidas (la tupla)
        if materia not in MATERIAS:
            raise ValueError(f"Materia '{materia}' no válida. Opciones: {MATERIAS}")

        # Convertimos la nota a float (por si llega como texto)
        nota = float(nota)
        
        # La nota debe estar en el rango válido del sistema vigesimal (0-20)
        if not (0 <= nota <= 20):
            raise ValueError(f"La nota debe estar entre 0 y 20.")

        # Accedemos al diccionario del estudiante y agregamos la nota a la materia
        # estudiantes[nombre] -> dict de materias
        # estudiantes[nombre][materia] -> lista de notas de esa materia
        estudiantes[nombre][materia].append(nota)
        print(f"Nota {nota} agregada a {nombre} en {materia}.")

    except KeyError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

def boletin(nombre):
    try:
        if nombre not in estudiantes:
            raise KeyError(f"Estudiante '{nombre}' no encontrado.")

        print(f"\n=== Boletín de {nombre} ===")
        
        # .items() nos da pares (clave, valor) del diccionario
        # materia = nombre de la materia, notas = lista de notas
        for materia, notas in estudiantes[nombre].items():
            if len(notas) == 0:
                # Si la lista está vacía, no hay notas que promediar
                promedio = "Sin notas"
            else:
                # sum(notas) suma todos los elementos de la lista
                # len(notas) cuenta cuántas notas hay
                promedio = f"{sum(notas)/len(notas):.1f}"
            
            # :15 alinea el nombre de la materia en 15 caracteres
            print(f"  {materia:15}: {promedio}")

    except KeyError as e:
        print(f"Error: {e}")

registrar_estudiante("Javier")
registrar_estudiante("Javier")

agregar_nota("Javier", "Programacion", 18)
agregar_nota("Javier", "Programacion", 15)
agregar_nota("Javier", "Matematica",   12)
agregar_nota("Javier", "Arte",         17)
agregar_nota("Javier", "Fisica",       25)
agregar_nota("Carlos", "Fisica",       14)

boletin("Javier")
boletin("Carlos")