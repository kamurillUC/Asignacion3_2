import funciones


estudiantes = [
     {
        'nombre': 'Kevin',
        'apellidos': 'Murillo Rojas',
        'nota': 70
    },

     {
        'nombre': 'Daniela',
        'apellidos': 'Madrigal Vargas',
        'nota': 100
    },

    {
        'nombre': 'Pablo',
        'apellidos': 'Lizano Acosta',
        'nota': 95
    },

    {
        'nombre': 'Anthony',
        'apellidos': 'Soto Vargas',
        'nota': 71
    },

    {
        'nombre': 'Niel',
        'apellidos': 'DeGrasse Tyson',
        'nota': 98
    }
]

bandera = 0

while bandera == 0:

    funciones.limpiar_consola()
    print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
    print(f"Menú de opciones:")
    print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
    print(f"1. Ver lista de estudiantes\n2. Agregar nuevo estudiante\n3. Remover estudiante\n4. Limpiar lista de estudiantes\n5. Salir")    
    print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
    respuesta = input("Digite su opción: ")

    if respuesta == "1":  

        funciones.limpiar_consola()
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"1. Ver lista de estudiantes")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(funciones.obtener_estudiantes(estudiantes))
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        respuesta = input("Presione ENTER para continuar...") 

    elif respuesta == "2":      

        funciones.limpiar_consola()  
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"2. Agregar nuevo estudiante")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        nombre = input("Nombre: ")
        primer_apellido = input("Primer Apellido: ")
        segundo_apellido = input("Segundo Apellido: ")
        while bandera == 0:            
            nota = input("Nota: ")
            if funciones.identificar_si_numero(nota) == False:
                print(">< >< >< >< >< Por favor ingresar un número >< >< >< >< ><")
            else:
                break           
        
        apellidos = f"{primer_apellido} {segundo_apellido}"
        funciones.agregar_estudiante(nombre, apellidos, nota, estudiantes)
        print(">< >< >< >< >< Estudiante agregado >< >< >< >< ><") 
        respuesta = input("Presione ENTER para continuar...")   

    elif respuesta == "3":      

        funciones.limpiar_consola()  
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"3. Remover estudiante")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")        
        print(funciones.obtener_estudiantes(estudiantes))
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")        

        while bandera == 0:            
            posicion = input("Número de estudiante: ") 
            if funciones.identificar_si_numero(posicion) == False:
                print(">< >< >< >< >< Por favor ingresar un número >< >< >< >< ><")
            else:
                numero = int(posicion)
                break                 
          
        estudianteEliminado = funciones.remover_estudiante(numero, estudiantes)   
                    
        print(f">< >< >< >< >< El estudiante {estudianteEliminado['nombre']} {estudianteEliminado['apellidos']} fue removido >< >< >< >< ><") 
        
        respuesta = input("Presione ENTER para continuar...")  

    elif respuesta == "4":      

        funciones.limpiar_consola()  
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"4. Limpiar lista de estudiantes")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        respuesta = input("¿Está seguro que quiere eliminar todos los estudiantes?(Si/No)")

        if respuesta.lower() == 'si':
            estudiantes.clear()
            print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
            print(">< >< >< >< >< Todos los estudiantes fueron removidos >< >< >< >< ><")             
        else:
            print(">< >< >< >< >< Ningun estudiante fue removido >< >< >< >< ><") 
        print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")       
        respuesta = input("Presione ENTER para continuar...")        
    else:
        funciones.limpiar_consola()  
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"GitHub: kamurillUC")        
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        break
