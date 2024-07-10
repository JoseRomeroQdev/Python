PACIENTES = []
MEDICOS = [] 
SECRETARIAS = []
RESERVACIONES = []

class Persona:
    def __init__(self, rut, nombre, apellido, rol):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol

class Secretaria(Persona):
    def __init__(self, rut, nombre, apellido):
        super().__init__(rut, nombre, apellido, "Secretaria")

    def listarPacientes(self):
        print('LISTA DE PACIENTES')
        for x, paciente in enumerate(PACIENTES, start=1):
            print(f'{x}) {paciente.nombre} {paciente.apellido}')

    def listarSecretarias(self):
        print('LISTA DE SECRETARIAS')
        for x, secretaria in enumerate(SECRETARIAS, start=1):
            print(f'{x}) {secretaria.nombre} {secretaria.apellido}')

    def listarMedicos(self):
        print('LISTA DE MÉDICOS')
        for x, medico in enumerate(MEDICOS, start=1):
            print(f'{x}) {medico.nombre} {medico.apellido}')

    def crearReserva(self, fecha, medico, estado="DISPONIBLE"):
        RESERVACIONES.append([fecha, medico, estado])
        print('Reservación Creada')
    
    def listarReservaciones(self):
        print('LISTA DE RESERVACIONES')
        for x, reserva in enumerate(RESERVACIONES, start=1):
            print(f'{x}) Fecha: {reserva[0]}, Médico: {reserva[1]}, Estado: {reserva[2]}')

class Medico(Persona):
    def __init__(self, rut, nombre, apellido):
        super().__init__(rut, nombre, apellido, "Medico")
        
    def listarReservaciones(self):
        print('LISTA DE RESERVACIONES')
        for x, reserva in enumerate(RESERVACIONES, start=1):
            print(f'{x}) Fecha: {reserva[0]}, Médico: {reserva[1]}, Estado: {reserva[2]}')

class Paciente(Persona):
    def __init__(self, rut, nombre, apellido):
        super().__init__(rut, nombre, apellido, "Paciente")
    
    def listarReservaciones(self):
        print('LISTA DE RESERVACIONES')
        for x, reserva in enumerate(RESERVACIONES, start=1):
            print(f'{x}) Fecha: {reserva[0]}, Médico: {reserva[1]}, Estado: {reserva[2]}')

    def pacienteReservar(self, id):
        if 0 <= id < len(RESERVACIONES):
            if RESERVACIONES[id][2] == "DISPONIBLE":
                RESERVACIONES[id][2] = "NO DISPONIBLE"
                print('Reservación realizada correctamente')
            else:
                print('La reservación ya no está disponible')
        else:
            print('ID de reservación incorrecto')
