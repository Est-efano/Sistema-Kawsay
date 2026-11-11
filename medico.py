class Medico: 

    def __init__(self, codigo_M, nombres, apellidos, especialidad):
        self._codigo_M = codigo_M
        self._nombres = nombres
        self._apellidos = apellidos
        self._especialidad = especialidad     

    # GETTERS
    @property
    def codigo_M(self):
        return self._codigo_M
    @property
    def nombres(self):
        return self._nombres
    @property
    def apellidos(self):
        return self._apellidos    
    @property
    def especialidad(self):
        return self._especialidad    
    # SETTER
    @codigo_M.setter
    def codigo_M(self, valor):
        self._codigo_M = valor
    @nombres.setter
    def nombres(self, valor):
        self._nombres = valor
    @apellidos.setter
    def apellidos(self, valor):
        self._apellidos = valor        
    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = valor

    def resumen(self):
        return f"{self._codigo_M} - Dr. {self._nombres} {self._apellidos} - ESPECIALIDAD: {self._especialidad}"            
                