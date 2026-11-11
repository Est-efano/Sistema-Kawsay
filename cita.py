class Cita:    
    def __init__(self, codigo_C, paciente, medico, fecha, hora):
        self._codigo_C = codigo_C
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._hora = hora
        
        

    # GETTERS
    @property
    def codigo_C(self):
        return self._codigo_C
    @property
    def paciente(self):
        return self._paciente
    @property
    def medico(self):
        return self._medico
    @property
    def fecha(self):
        return self._fecha
    @property
    def hora(self):
        return self._hora
    
    
    # Setters
    @codigo_C.setter
    def codigo_C(self, valor):
        self._codigo = valor
    @paciente.setter
    def paciente(self, valor):
        self.paciente = valor
    @medico.setter
    def medico(self, valor):
        self._medico = valor
    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor
    @hora.setter
    def hora(self, valor):
        self._hora = valor
    
       
    def resumen(self):
              return f"{self._codigo_C} - Paciente: {self._paciente.nombres} {self._paciente.apellidos} con el Dr. {self._medico.nombres} {self._medico.apellidos} Fecha: {self._fecha} Hora: {self._hora} " 
    
   