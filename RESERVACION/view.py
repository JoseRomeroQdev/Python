from models import *

while True:
    print("""
    SISTEMA DE RESERVACIÓN MÉDICA
        1) CREAR RESERVACIÓN
        2) LISTAR RESERVACIONES
        3) LISTAR MÉDICOS
        4) LISTAR PACIENTES
        5) LISTAR SECRETARIAS
        6) AGREGAR PACIENTE
        7) AGREGAR MÉDICO
        8) AGREGAR SECRETARIA
        9) SALIR
        """)
    choice = input("Seleccione una opción: ")
        
    if choice == "1":
        rut_secretaria = input("Ingrese el RUT de la secretaria: ")
        nombre_secretaria = input("Ingrese el nombre de la secretaria: ")
        apellido_secretaria = input("Ingrese el apellido de la secretaria: ")
        secretaria = Secretaria(rut_secretaria, nombre_secretaria, apellido_secretaria)
        fecha = input("Ingrese la fecha de la reservación (YYYY-MM-DD): ")
        medico = input("Ingrese el nombre del médico: ")
        secretaria.crearReserva(fecha, medico)
        
    elif choice == "2":
        rut_secretaria = input("Ingrese el RUT de la secretaria: ")
        nombre_secretaria = input("Ingrese el nombre de la secretaria: ")
        apellido_secretaria = input("Ingrese el apellido de la secretaria: ")
        secretaria = Secretaria(rut_secretaria, nombre_secretaria, apellido_secretaria)
        secretaria.listarReservaciones()
        
    elif choice == "3":
        rut_secretaria = input("Ingrese el RUT de la secretaria: ")
        nombre_secretaria = input("Ingrese el nombre de la secretaria: ")
        apellido_secretaria = input("Ingrese el apellido de la secretaria: ")
        secretaria = Secretaria(rut_secretaria, nombre_secretaria, apellido_secretaria)
        secretaria.listarMedicos()
        
    elif choice == "4":
        rut_secretaria = input("Ingrese el RUT de la secretaria: ")
        nombre_secretaria = input("Ingrese el nombre de la secretaria: ")
        apellido_secretaria = input("Ingrese el apellido de la secretaria: ")
        secretaria = Secretaria(rut_secretaria, nombre_secretaria, apellido_secretaria)
        secretaria.listarPacientes()
        
    elif choice == "5":
        rut_secretaria = input("Ingrese el RUT de la secretaria: ")
        nombre_secretaria = input("Ingrese el nombre de la secretaria: ")
        apellido_secretaria = input("Ingrese el apellido de la secretaria: ")
        secretaria = Secretaria(rut_secretaria, nombre_secretaria, apellido_secretaria)
        secretaria.listarSecretarias()
        
    elif choice == "6":
        rut = input("Ingrese el RUT del paciente: ")
        nombre = input("Ingrese el nombre del paciente: ")
        apellido = input("Ingrese el apellido del paciente: ")
        paciente = Paciente(rut, nombre, apellido)
        PACIENTES.append(paciente)
        print("Paciente agregado correctamente")
        
    elif choice == "7":
        rut = input("Ingrese el RUT del médico: ")
        nombre = input("Ingrese el nombre del médico: ")
        apellido = input("Ingrese el apellido del médico: ")
        medico = Medico(rut, nombre, apellido)
        MEDICOS.append(medico)
        print("Médico agregado correctamente")
        
    elif choice == "8":
        rut = input("Ingrese el RUT de la secretaria: ")
        nombre = input("Ingrese el nombre de la secretaria: ")
        apellido = input("Ingrese el apellido de la secretaria: ")
        secretaria = Secretaria(rut, nombre, apellido)
        SECRETARIAS.append(secretaria)
        print("Secretaria agregada correctamente")
        
    elif choice == "9":
        break
        
    else:
        print("Opción no válida. Por favor, intente de nuevo.")