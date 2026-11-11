from cita import Cita
from paciente import Paciente
from medico import Medico

#CREAR MEDICOS
medico_01 = Medico("M001", "Donald", "Trump", "Medicina General")
medico_02 = Medico("M002", "Jorge", "Chicana", "Medicina General")
medico_03 = Medico("M003", "Jeffrey", "Epstein", "Pediatria")
medico_04 = Medico("M004", "Adolf", "Hitler", "Psiquiatria")
medico_05 = Medico("M005", "Mia", "Khalifa", "Oftalmologia")
medico_06 = Medico("M006", "Stephen", "Hawking", "Neurologia")

contador = 0

def registrar_paciente():
    while True: 
        print("\n ===== REGISTRAR PACIENTE =====")
        nombres = input("Ingrese su nombre: ")
        apellidos = input("Ingrese sus apellidos: ")
        edad = int(input("Ingrese su edad: "))
        while edad < 0 or edad > 120:
            Paciente.validar_edad(edad)
            edad = int(input("Ingrese su edad: "))

        paciente = Paciente("P001", nombres, apellidos, edad)
        print("Paciente registrado:", paciente.resumen())

        print("\n====== MEDICOS DISPONIBLES ======")
        print("1.", medico_01.resumen())
        print("2.", medico_02.resumen())
        print("3.", medico_03.resumen())
        print("4.", medico_04.resumen())
        print("5.", medico_05.resumen())
        print("6.", medico_06.resumen())

        opcion = int(input("Elija el médico (1-6): "))
        if opcion == 1:
            medico_elegido = medico_01
        elif opcion == 2:
            medico_elegido = medico_02
        elif opcion == 3:
            medico_elegido = medico_03
        elif opcion == 4:
            medico_elegido = medico_04
        elif opcion == 5:
            medico_elegido = medico_05
        else:
            medico_elegido = medico_06

        fecha = input("Ingrese fecha de la cita (DD/MM/AAAA): ")
        hora = input("Ingrese la hora de la cita: ")
        cita = Cita(f"C00{contador}" , paciente, medico_elegido, fecha, hora)
        print("\n====== CITA REGISTRADA ======")
        print(cita.resumen())
        
        
        nueva_cita = input("Deseas registrar una nueva cita (Si = S, No = N): ")
        if nueva_cita == "N":
            break
        
    
registrar_paciente()          



