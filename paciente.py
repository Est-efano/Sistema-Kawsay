
class Paciente:

    def __init__(self, codigo_P, nombres, apellidos, edad):
        self._codigo_P = codigo_P
        self._nombres = nombres
        self._apellidos = apellidos
        self._edad = edad
    
    def validar_edad(edad):
        if (edad < 0 or edad > 120):
            print("La edad debe ser un número entero entre 0 y 120.")
        return edad   

    # GETTERS
    @property
    def codigo_P(self):
        return self._codigo_P
    @property
    def nombres(self):
        return self._nombres
    @property
    def apellidos(self):
        return self._apellidos
    @property
    def edad(self):
        return self._edad

    # SETTERS
    @codigo_P.setter
    def codigo_P(self, valor):
        self.codigo_P = valor
    @nombres.setter
    def nombres(self, valor):
        self.nombres = valor
    @apellidos.setter
    def apellidos(self, valor):
        self.apellidos = valor
    @edad.setter
    def edad(self, valor):
        self.edad = valor
        
    
    def resumen(self):
        return f"{self._codigo_P} - {self._nombres} - {self._apellidos} - {self._edad}" 
    
    
