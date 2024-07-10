PACIENTES = []
MEDICOS = [] 
SECRETARIAS = []
RESERVACION = []

class Persona:
    def __init__(self, rut, nombre, apellido, rol):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol

class Secretaria(Persona):
    def __init__(self, rut, nombre, apellido):
        super().__init__(rut, nombre, apellido, "Secretaria")

    def listarPacientes():
        print('LISTA DE PACIENTES')
        x=0
        for i in PACIENTES:
            x = x + 1
            print(f'{x}) {i.nombre} {i.apellido}')

    def listarSecretarias():
        print('LISTA DE SECREATARIAS')
        x=0
        for i in SECRETARIAS:
            x = x + 1
            print(f'{x}) {i.nombre} {i.apellido}')

    def listarMedicos(self):
        print('LISTA DE MEDICOS')
        x=0
        for i in MEDICOS:
            x = x + 1
            print(f'{x}) {i.nombre} {i.apellido}')

    def crearReserva(self, fecha, medico, estado):
        self.fecha = fecha
        self.medico = medico
        self.estado = estado
        RESERVACION.append([self.fecha,self.medico,self.estado])
        print('Reservacion Creada')

class Medico(Persona):
    def __init__(self, rut, nombre, apellido):
        super().__init__(rut, nombre, apellido, "Medico") 
    
    def listarReservacion(self):
        print('LISTA DE RESERVACION')
        x=0
        for i in RESERVACION:
            x = x + 1
            print(f'{x}) {i}')


class Paciente(Persona):
    def __init__(self, rut, nombre, apellido):
        super().__init__(rut, nombre, apellido, "Paciente")
    
    def listarReservacion(self):
        print('LISTA DE RESERVACION')
        x=0
        for i in RESERVACION:
            x = x + 1
            print(f'{x}) {i}')

    def pacienteReservar(self, id):
        RESERVACION[id][2] = "NO DISPONIBLE"
        print('Reservado Correctamente')
 
