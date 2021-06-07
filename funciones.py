
#Funcion para obtener la lista completa de los estudiantes que aprobaron y los que no
def obtener_estudiantes(estudiantes):
    respuesta = ""
    numero = 1
    for estudiante in estudiantes:
        respuesta += f"{numero}. El estudiante {estudiante['nombre']} {estudiante['apellidos']} "
        respuesta += f"obtuvo una nota de {estudiante['nota']} y tiene un estado de "
        if int(estudiante['nota']) > 70:
            respuesta += f"aprobado"       
        else:
            respuesta += f"reprobado" 
        respuesta += '\n'
        numero += 1

    return respuesta


#Funcion para agregar nuevos estudiantes
def agregar_estudiante(nombre, apellidos, nota, estudiantes):
    nuevo_estudiante = {
        'nombre': nombre,
        'apellidos': apellidos, 
        'nota': int(nota)
    }
    estudiantes.append(nuevo_estudiante)

#Funcion para remover estudiante
def remover_estudiante(numero, estudiantes):    
    posicion = numero - 1
    estudianteEliminado = estudiantes[posicion]
    estudiantes.pop(posicion)    
    return estudianteEliminado

#Funcion para limpiar consola segun OS
def limpiar_consola():
    import os
    if os.name == "posix" or os.name == "mac":
        os.system("clear")
    elif os.name == "ce" or os.name == "dos" or os.name == "nt":
        os.system("cls")


#Funcion para identificar si es numero
def identificar_si_numero(var):
    if var[0] == ('-', '+'):
        return var[1:].isdigit()
    else:
        return var.isdigit()


