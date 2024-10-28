estudiantes = {}
asignaturas = {}
notas = {}
porcentajes = {}
umbral_aprobacion = 0.6

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    id_estudiante = len(estudiantes) + 1
    estudiantes[id_estudiante] = nombre
    print(f"Estudiante {nombre} registrado con ID {id_estudiante}.")

def registrar_asignatura():
    nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
    id_asignatura = len(asignaturas) + 1
    asignaturas[id_asignatura] = nombre_asignatura

    exam_parcial = float(input("Ingrese el porcentaje del examen parcial: ")) / 100
    exam_final = float(input("Ingrese el porcentaje del examen final: ")) / 100
    trabajos = float(input("Ingrese el porcentaje de trabajos: ")) / 100
    participacion = float(input("Ingrese el porcentaje de participación: ")) / 100

    porcentajes[id_asignatura] = {
        "examen_parcial": exam_parcial,
        "examen_final": exam_final,
        "trabajos": trabajos,
        "participacion": participacion
    }
    print(f"Asignatura {nombre_asignatura} registrada con ID {id_asignatura}.")

def ingresar_notas():
    id_estudiante = int(input("Ingrese el ID del estudiante: "))
    id_asignatura = int(input("Ingrese el ID de la asignatura: "))
    
    if id_estudiante in estudiantes and id_asignatura in asignaturas:
        nota_examen_parcial = float(input("Ingrese la nota del examen parcial: "))
        nota_examen_final = float(input("Ingrese la nota del examen final: "))
        nota_trabajos = float(input("Ingrese la nota de trabajos: "))
        nota_participacion = float(input("Ingrese la nota de participación: "))
        
        notas.setdefault(id_estudiante, {})[id_asignatura] = {
            "examen_parcial": nota_examen_parcial,
            "examen_final": nota_examen_final,
            "trabajos": nota_trabajos,
            "participacion": nota_participacion
        }
        print("Notas ingresadas correctamente.")
    else:
        print("Estudiante o asignatura no encontrados.")
    return id_asignatura,id_estudiante
def calcular_promedio(id_estudiante, id_asignatura):
    if id_estudiante in notas and id_asignatura in notas[id_estudiante]:
        nota = notas[id_estudiante][id_asignatura]
        pesos = porcentajes[id_asignatura]
        promedio = (nota["examen_parcial"] * pesos["examen_parcial"] +
                    nota["examen_final"] * pesos["examen_final"] +
                    nota["trabajos"] * pesos["trabajos"] +
                    nota["participacion"] * pesos["participacion"])
        return promedio
    return None

def generar_reporte():
    id_estudiante = int(input("Ingrese el ID del estudiante: "))
    estudiantes=id_estudiante*[0]
    print(f"Reporte para {estudiantes[id_estudiante]}")
    
    for id_asignatura, nombre_asignatura in asignaturas.items():
        promedio = calcular_promedio(id_estudiante, id_asignatura)
        if promedio is not None:
            estado = "Aprobado" if promedio >= umbral_aprobacion else "Reprobado"
            print(f"Asignatura: {nombre_asignatura}, Promedio: {promedio:.2f}, Estado: {estado}")
        else:
            print(f"Asignatura: {nombre_asignatura}, No se han ingresado notas.")

def listado_estudiantes():
    print("Listado de estudiantes y sus promedios:")
    for id_estudiante, nombre in estudiantes.items():
        print(f"Estudiante ID: {id_estudiante}, Nombre: {nombre}")

def estadisticas_curso():
    print("Estadísticas del curso:")
    for id_asignatura, nombre_asignatura in asignaturas.items():
        total_estudiantes = len(estudiantes)
        total_aprobados = 0
        mejor_nota = float('-inf')
        peor_nota = float('inf')
        
        for id_estudiante in estudiantes.keys():
            promedio = calcular_promedio(id_estudiante, id_asignatura)
            if promedio is not None:
                if promedio >= umbral_aprobacion:
                    total_aprobados += 1
                mejor_nota = max(mejor_nota, promedio)
                peor_nota = min(peor_nota,promedio)
registrar_estudiante()
registrar_asignatura()
id_asignatura,id_estudiante=ingresar_notas()
calcular_promedio(id_asignatura,id_estudiante)
generar_reporte()
listado_estudiantes()
estadisticas_curso()