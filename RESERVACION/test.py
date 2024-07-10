from models import *

# Medicos
medico1 = Medico('21078054-1', 'Ana', 'Pérez')
medico2 = Medico('21078055-3', 'Luis', 'González')
medico3 = Medico('21078056-K', 'María', 'López')
medico4 = Medico('21078057-4', 'Carlos', 'Martínez')
medico5 = Medico('21078058-9', 'Elena', 'García')

# Pacientes
paciente1 = Paciente('12312332-2', 'Laura', 'Díaz')
paciente2 = Paciente('12312333-3', 'Jorge', 'Méndez')

# Secretarias
secretaria1 = Secretaria('12256591-5', 'Beatriz', 'Herrera')
secretaria2 = Secretaria('12256592-1', 'Marta', 'Ruiz')
secretaria3 = Secretaria('12256593-7', 'Clara', 'Fernández')

# Guardar Informacion
MEDICOS.append(medico1)
MEDICOS.append(medico2)
MEDICOS.append(medico3)
MEDICOS.append(medico4)
MEDICOS.append(medico5)

PACIENTES.append(paciente1)
PACIENTES.append(paciente2)

SECRETARIAS.append(secretaria1)
SECRETARIAS.append(secretaria2)
SECRETARIAS.append(secretaria3)

# TESTING 

# Crear Reservacion
secretaria1.crearReserva('09/07/2024', (medico1.nombre, medico1.apellido), "DISPONIBLE")
secretaria1.crearReserva('10/07/2024', (medico2.nombre, medico2.apellido), "DISPONIBLE")
secretaria2.crearReserva('12/07/2024', (medico4.nombre, medico4.apellido), "DISPONIBLE")
secretaria3.crearReserva('14/07/2024', (medico5.nombre, medico5.apellido), "DISPONIBLE")

paciente1.listarReservacion()
paciente1.pacienteReservar(0)
paciente2.pacienteReservar(3)
paciente1.listarReservacion()


